#!/usr/bin/env python3
import mod_dirs
from multiprocessing import Pool
from subprocess import check_output
import re


def update_tf_module_docs(mod_dir):
    # run terraform-docs in docker. Invoke the Docker binary to avoid
    # external dependencies
    tf_docs_command = [
        "docker",
        "run",
        "--rm",
        "-v",
        "{0}:/tf-mod".format(mod_dir),
        "tmknom/terraform-docs:0.5.0",
        "md",
        "/tf-mod",
    ]
    print("[DOCS] {0}".format(mod_dir))
    # Generate the new input and output tables for this module.
    docs = check_output(tf_docs_command)
    with open("{0}/README.md".format(mod_dir), "r+") as f:
        # Use readlines instead of read so that we can intelligently truncate
        # for modules that have inputs, inputs and outputs, or only outputs.
        content = f.readlines()
        # Fine a header indicating auto-generated documentation.
        idx = get_first_match("## (?:Inputs|Outputs)", content)
        if idx:
            new_content = (
                content[0 : (idx - 1)]
                + ["\n"]
                + [x.decode() for x in docs.splitlines(True)]
            )
        else:
            new_content = content + ["\n"] + [x.decode() for x in docs.splitlines(True)]
        f.truncate(0)
        f.seek(0, 0)
        # We read an empty line at the bottom of the file, writelines will add
        # another, so we don't write the last list element (a blank line).
        f.writelines(new_content[0:-1])


def get_first_match(pattern, strings):
    for i, s in enumerate(strings):
        if re.match(pattern, s):
            return i


if __name__ == "__main__":
    # Multiprocessing for maximum speed!
    pool = Pool(processes=5)
    pool.map(update_tf_module_docs, mod_dirs.gather_module_dirs())

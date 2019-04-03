#!/usr/bin/env python3
import fnmatch
import os

if __name__ == "__main__":
    raise NameError("Can't invoke this module by itself!")


def gather_module_dirs(dir="."):
    # Some special directories to skip that we know aren't modules
    dirs_to_skip = [
        "./.git",
        "./.github",
        "./.vscode",
        "./scripts",
        "./helm/consul/consul-helm",
    ]

    # Accumulator
    module_dirs = []

    for dir_tuple in os.walk(dir):
        # Skip the repo root
        if dir_tuple[0] == ".":
            continue
        # Skip some other dirs
        if any(skip in dir_tuple[0] for skip in dirs_to_skip):
            continue
        # Skip if .tf files and a README aren't present.
        if not (
            fnmatch.filter(dir_tuple[2], "*.tf")
            and fnmatch.filter(dir_tuple[2], "README.md")
        ):
            continue
        # This must be a module folder
        module_dirs.append(os.path.abspath(dir_tuple[0]))
    return module_dirs

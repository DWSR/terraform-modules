#!/usr/bin/env python3
import mod_dirs
from multiprocessing import Pool
from subprocess import run
from os import path


def lint_tf_files(mod_dir):
    tf_lint_command = [
        "docker",
        "run",
        "--rm",
        "-v" "{0}:/tf-mod".format(mod_dir),
        "hashicorp/terraform:0.11.11",
        "fmt",
        "-list=false",
        "/tf-mod",
    ]
    print("[LINT] {0}".format(mod_dir))
    run(tf_lint_command)


if __name__ == "__main__":
    pool = Pool(processes=5)
    pool.map(lint_tf_files, mod_dirs.gather_module_dirs())

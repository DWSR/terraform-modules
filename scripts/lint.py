#!/usr/bin/env python3
import mod_dirs
from multiprocessing import Pool

TERRAFORM_VERSION = "0.11.13"


def lint_tf_files(mod_dir):
    print("[LINT] {0}".format(mod_dir))
    mod_dirs.run_oneshot_container(
      "hashicorp/terraform:{0}".format(TERRAFORM_VERSION),
      "fmt -list=false /tf-mod"
    )


if __name__ == "__main__":
    pool = Pool(processes=5)
    pool.map(lint_tf_files, mod_dirs.gather_module_dirs())

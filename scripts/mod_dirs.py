#!/usr/bin/env python3
import fnmatch
from os import path, walk
import docker

if __name__ == "__main__":
    raise NameError("Can't invoke this module by itself!")


def gather_module_dirs(dir="."):
    # Some special directories to skip that we know aren't modules
    dirs_to_skip = [
        "./.git",
        "./.github",
        "./.vscode",
        "./scripts",
    ]

    # Accumulator
    module_dirs = []

    for dir_tuple in walk(dir):
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
        module_dirs.append(path.abspath(dir_tuple[0]))
    return module_dirs


def run_oneshot_container(image, command, path_to_mount):
    """
    Runs a container that is removed after its execution is completed. The
    intended purpose behind this is to easily run binaries like
    `terraform-docs` without requiring that they be present on the host system.
    """
    docker_client = docker.from_env()
    container_opts = {"remove": True, "volumes": {path_to_mount: {"bind": "/tf-mod"}}}
    return docker_client.containers.run(image, command, **container_opts)

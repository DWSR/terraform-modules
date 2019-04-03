#!/usr/bin/env python3
from subprocess import run

if __name__ == "__main__":
    git_status_command = ["git", "status"]
    clean_msg = "nothing to commit, working tree clean"
    git_status = run(git_status_command, capture_output=True)
    if clean_msg not in str(git_status.stdout):
        err_msg = [
            "Working directory not clean.",
            "Ensure that you have added or stashed all changes.",
            "This may be caused by forgetting to lint or generate docs for",
            "modules.",
        ]
        print(str.join(" ", err_msg))
        exit(1)

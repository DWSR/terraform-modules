#!/usr/bin/env python3

from github import Github, GithubException
from os import environ
import argparse


def parse_args():
    """
    Does CLI argument parsing.
    """
    description = """
    Creates or updates a GitHub repository that is intended to by used as a
    push mirror for a GitLab project.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "name", type=str, help="The name of the repository to create."
    )
    parser.add_argument(
        "homepage_url",
        type=str,
        help="The URL to the GitLab project.",
    )
    parser.add_argument(
        "--description",
        type=str,
        dest="description",
        default="",
        help="The description of the repository",
    )
    parser.add_argument(
        "--private",
        dest="private",
        action='store_true',
        default=False,
        help="Whether the repository is private.",
    )
    return parser.parse_args()


def get_github_obj():
    """
    Returns a Github object that is used to interact with the GitHub v3 API
    """
    token = environ.get("GITHUB_TOKEN")
    return Github(token)


def create_or_update_github_repo(
    github, name, homepage_url, description="", private=True
):
    """
    Creates a GitHub repository that is intended to be used as a push mirror
    for a GitLab project.
    """
    repo_args = {
        'name': name,
        'description': description,
        'homepage': homepage_url,
        'private': private,
        'has_issues': False,
        'has_wiki': False,
        'has_downloads': False,
        'has_projects': False,
        'allow_merge_commit': False,
        'allow_squash_merge': True,
        'allow_rebase_merge': False,
    }
    try:
        repo = github.get_repo('dwsr/{0}'.format(name))
        print("Updating repository dwsr/{0}".format(name))
        repo.edit(**repo_args)
    except GithubException:
        print("Creating repository dwsr/{0}".format(name))
        github.get_user().create_repo(**repo_args, auto_init=False)


if __name__ == "__main__":
    if environ.get('GITHUB_TOKEN') is None:
        print("Must supply GitHub access token via GITHUB_TOKEN env.")
        exit(1)
    args = parse_args()
    g = get_github_obj()
    create_or_update_github_repo(
        g,
        name=args.name,
        homepage_url=args.homepage_url,
        description=args.description,
        private=args.private,
    )

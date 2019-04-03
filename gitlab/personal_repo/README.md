# Personal GitLab Repo

## Description

This module represents a GitLab repo used for my personal projects. It configures some opinionated
settings for repos (such as only allowing Rebase Merges). It also creates a GitHub repository that
will act as a push mirror for the GitLab project. The repository is created (and updated) via an
included Python3 script as the GitHub provider for Terraform does not support personal
repositories.

Currently, there is no API for creating push mirrors in GitLab. See
[this issue](https://gitlab.com/gitlab-org/gitlab-ce/issues/58580) for more details.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-----:|:-----:|
| description | A description of the repository | string | `` | no |
| issues\_enabled | Whether or not to enable issues on the repository. | string | `true` | no |
| name | The name of the repository. | string | - | yes |
| visibility\_level | The visibility of the repository. Must be `public`, `private`, or `internal`. | string | `private` | no |

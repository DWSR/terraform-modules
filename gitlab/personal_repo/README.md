# Personal GitLab Repo

## Description

This module represents a GitLab repo used for my personal projects. It configures some
opinionated settings for repos (such as only allowing Rebase Merges).

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-----:|:-----:|
| description | A description of the repository | string | `` | no |
| issues\_enabled | Whether or not to enable issues on the repository. | string | `true` | no |
| name | The name of the repository. | string | - | yes |
| visibility\_level | The visibility of the repository. Must be `public`, `private`, or `internal`. | string | `private` | no |

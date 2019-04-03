resource "gitlab_project" "proj" {
  # Actual dynamic settings
  name             = "${var.name}"
  description      = "${var.description}"
  visibility_level = "${var.visibility_level}"
  issues_enabled   = "${var.issues_enabled}"

  # Opinionation
  default_branch                                   = "master"
  merge_requests_enabled                           = true
  approvals_before_merge                           = true
  wiki_enabled                                     = false
  snippets_enabled                                 = true
  merge_method                                     = "rebase_merge"
  only_allow_merge_if_pipeline_succeeds            = true
  only_allow_merge_if_all_discussions_are_resolved = true
}

resource "gitlab_project" "proj" {
  # Actual dynamic settings
  name             = "${var.name}"
  description      = "${var.description}"
  visibility_level = "${var.visibility_level}"
  issues_enabled   = "${var.issues_enabled}"

  # Opinionation
  default_branch                                   = "master"
  merge_requests_enabled                           = true
  approvals_before_merge                           = 1
  wiki_enabled                                     = false
  snippets_enabled                                 = true
  merge_method                                     = "ff"
  only_allow_merge_if_pipeline_succeeds            = true
  only_allow_merge_if_all_discussions_are_resolved = true
}

resource "null_resource" "github_repo" {
  triggers {
    name             = "${var.name}"
    description      = "${var.description}"
    visibility_level = "${var.visibility_level}"
    gitlab_proj      = "${gitlab_project.proj.id}"
  }

  provisioner "local-exec" {
    command     = "python3 ./create_github_repo.py ${var.name} ${gitlab_project.proj.web_url} --description '${var.description}' ${var.visibility_level == "private" ? "--private" : "" }"
    working_dir = "${path.module}"
  }
}

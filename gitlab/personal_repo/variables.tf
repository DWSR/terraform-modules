variable "name" {
  type        = "string"
  description = "The name of the repository."
}

variable "description" {
  type        = "string"
  description = "A description of the repository"
  default     = ""
}

variable "visibility_level" {
  type        = "string"
  description = "The visibility of the repository. Must be `public`, `private`, or `internal`."
  default     = "private"
}

variable "issues_enabled" {
  type        = "string"
  description = "Whether or not to enable issues on the repository."
  default     = true
}

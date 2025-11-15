terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "2.5.2"
    }
  }
}

provider "local" {}

# Creates a simple output file using Terraform
resource "local_file" "project_info" {
  filename = "${path.module}/project_output.txt"
  content  = <<EOT
Project Name: Stock Market Prediction System
Terraform Status: Infrastructure Provisioned Successfully
EOT
}

terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "5.17.0" }
  }
}
variable "aws_profile" {
  type        = string
  description = "AWS CLI profile name"
  default     = "minisedric_dev"
} 



provider "aws" {
  profile = var.aws_profile
  region = "us-east-1"
}
data "external" "aws_region" {
  program = ["${path.module}/get-aws-region.sh", var.aws_profile]
}

output "aws_region" {
  value = data.external.aws_region.result["region"]
}
 


 
 
 
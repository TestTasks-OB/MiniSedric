
resource "aws_ecr_repository" "api" {
  name                 = "minisedric-lambda-api"
  image_tag_mutability = "MUTABLE"
  force_delete         = true

  image_scanning_configuration {
    scan_on_push = true
  }
}

# --- Build & push image --- 

locals {
  repo_url = aws_ecr_repository.api.repository_url
}

resource "null_resource" "image" {
  triggers = {
    hash = md5(join("-", [for x in fileset("", "./src/{*.py,*.txt,Dockerfile}") : filemd5(x)]))
  }

  provisioner "local-exec" {
    command = <<EOF
      aws ecr get-login-password --profile ${var.aws_profile} | docker login -u AWS  --password-stdin ${local.repo_url}
      docker build --platform linux/amd64 -t ${local.repo_url}:latest -f ../../DockerfileLambda ../..
      docker push ${local.repo_url}:latest
    EOF
  }
}

data "aws_ecr_image" "latest" {
  repository_name = aws_ecr_repository.api.name
  image_tag       = "latest"
  depends_on      = [null_resource.image]
}
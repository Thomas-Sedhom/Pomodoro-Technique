terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.9.3"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "pomodoro" {
  ami           = var.ami              # Reference the ami variable
  instance_type = var.instance_type    # Reference the instance_type variable
  availability_zone = "us-east-1a"     # This can also be made a variable if needed
  key_name     = var.key_name          # Reference the key_name variable

  tags = {
    Name = "pomodoro"
  }
}
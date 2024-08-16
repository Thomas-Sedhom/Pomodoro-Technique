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
  region  = "us-east-1"
}

resource "aws_instance" "pomodoro" {
  ami           = "ami-04a81a99f5ec58529" # Ubuntu 24.04 LTS (us-east-1)
  instance_type = "t2.micro"
  availability_zone = "us-east-1a"

  tags = {
    Name = "pomodoro"
  }
}

// terraform init 
// terraform apply

// terraform destroy
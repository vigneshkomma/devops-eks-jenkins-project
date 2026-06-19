variable "aws_region" {
  default = "eu-north-1"
}

variable "project_name" {
  default = "devops-app"
}

variable "instance_type" {
  default = "t3.micro"
}

variable "key_name" {
  description = "Exsisitng AWS EC2 key pair name"
  type        = string
}
provider "aws" {
  access_key                  = "test"
  secret_key                  = "test"
  region                      = "us-east-1"

  s3_use_path_style           = true
  skip_credentials_validation = true
  skip_requesting_account_id  = true
  skip_metadata_api_check     = true

  endpoints {
    s3  = "http://localhost:4566"
    iam = "http://localhost:4566"
    sts = "http://localhost:4566"
    sqs = "http://localhost:4566"
    sns = "http://localhost:4566"
    dynamodb = "http://localhost:4566"
    lambda = "http://localhost:4566"
    logs = "http://localhost:4566"
    cloudwatch = "http://localhost:4566"
  }
}

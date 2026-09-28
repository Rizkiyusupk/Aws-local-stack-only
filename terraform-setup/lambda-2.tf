resource "aws_lambda_function" "lambda-function-consumer" {
  filename          = "${path.module}/lambda_function_consumer.zip"
  function_name     = "lambda_function_consumer"
  role              = aws_iam_role.lambda-consumer-role.arn
  handler           = "lambda_function_consumer.lambda_handler"
  source_code_hash  = filebase64sha256("${path.module}/lambda_function_consumer.zip")
  runtime           = "python3.12"
  timeout           = 10

  environment {
    variables = {
      ENVIRONMENT         = "production"
      LOG_LEVEL           = "info"
      TELEGRAM_BOT_TOKEN  = var.telegram_bot_token
      TELEGRAM_CHAT_ID    = var.telegram_chat_id
    }
  }

  tags = {
    Environment = "production"
    Application = "example"
  }
}

variable "telegram_bot_token" {
  description = "Token dari @BotFather"
  type        = string
  sensitive   = true
}

variable "telegram_chat_id" {
  description = "Chat ID tujuan alert"
  type        = string
}

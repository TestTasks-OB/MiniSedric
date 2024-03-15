
resource "aws_iam_policy" "lambda_transcribe_policy" {
  name        = "LambdaTranscribeAccess"
  description = "Allow Lambda function to access  and use Transcribe"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = [
          "transcribe:StartTranscriptionJob",
          "transcribe:GetTranscriptionJob",
          "transcribe:ListTranscriptionJobs",
          "transcribe:DeleteTranscriptionJob"
        ]
        Resource = "*"
      }
    ]
  })
}
resource "aws_iam_role_policy_attachment" "lambda_transcribe_attach" {
  role       = aws_iam_role.lambda.name
  policy_arn = aws_iam_policy.lambda_transcribe_policy.arn
}


resource "aws_s3_bucket" "minisedric_store" {
  bucket = "minisedric-store-${substr(uuid(), 0, 8)}"
} 
resource "aws_iam_policy" "lambda_s3_access" {
  name        = "lambda_s3_access_policy"
  description = "Policy that allows lambda function to access S3 Bucket"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Action    = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject"
        ]
        Resource = [
          "${aws_s3_bucket.minisedric_store.arn}/*"
        ]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_s3_policy_attachment" {
  role       = aws_iam_role.lambda.name
  policy_arn = aws_iam_policy.lambda_s3_access.arn
}

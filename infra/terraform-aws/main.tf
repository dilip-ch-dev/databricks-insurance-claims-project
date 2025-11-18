provider "aws" {
  region = "us-east-2" # Match Databricks region
}

# S3 Bucket
resource "aws_s3_bucket" "claims" {
  bucket        = var.s3_bucket_name
  force_destroy = true
  tags = {
    Project = "databricks-claims"
    Owner   = "Dilip"
  }
}

# IAM Role for Databricks Access
resource "aws_iam_role" "databricks_s3_access" {
  name = "databricks-s3-access-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::414351767826:role/unity-catalog-prod-UCMasterRole-14S5ZJVKOTYTL"
        }
        Action = "sts:AssumeRole"
        Condition = {
          StringEquals = {
            "sts:ExternalId" = "0000"
          }
        }
      }
    ]
  })
  tags = {
    Project = "databricks-claims"
    Owner   = "Dilip"
  }
}

# Policy: Allow Databricks Role Full Access ONLY to Project Bucket
resource "aws_iam_policy" "databricks_bucket_access" {
  name        = "databricks-bucket-access-policy"
  description = "Allow Databricks access to S3 bucket only."
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Action = [
        "s3:ListBucket",
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      Resource = [
        aws_s3_bucket.claims.arn,
        "${aws_s3_bucket.claims.arn}/*"
      ]
    }]
  })
}

resource "aws_iam_role_policy_attachment" "attach_s3_policy" {
  role       = aws_iam_role.databricks_s3_access.name
  policy_arn = aws_iam_policy.databricks_bucket_access.arn
}

# ============================================
# KINESIS DATA STREAM FOR TELEMATICS
# ============================================

resource "aws_kinesis_stream" "telemetry" {
  name             = "insurance-telemetry-stream"
  shard_count      = 1
  retention_period = 24

  tags = {
    Project = "databricks-claims"
    Owner   = "Dilip"
    Purpose = "Real-time telematics ingestion"
  }
}

# ============================================
# IAM POLICY FOR KINESIS ACCESS
# ============================================

data "aws_iam_policy_document" "kinesis_read" {
  statement {
    effect = "Allow"
    actions = [
      "kinesis:GetRecords",
      "kinesis:GetShardIterator",
      "kinesis:DescribeStream",
      "kinesis:ListStreams"
    ]
    resources = [
      aws_kinesis_stream.telemetry.arn
    ]
  }
}

resource "aws_iam_policy" "kinesis_access" {
  name        = "databricks-kinesis-read-policy"
  description = "Allow Databricks to read from Kinesis telemetry stream"
  policy      = data.aws_iam_policy_document.kinesis_read.json
}

resource "aws_iam_role_policy_attachment" "attach_kinesis_policy" {
  role       = aws_iam_role.databricks_s3_access.name
  policy_arn = aws_iam_policy.kinesis_access.arn
}

output "kinesis_stream_arn" {
  value       = aws_kinesis_stream.telemetry.arn
  description = "ARN of Kinesis telemetry stream"
}

output "kinesis_stream_name" {
  value       = aws_kinesis_stream.telemetry.name
  description = "Name of Kinesis telemetry stream"
}
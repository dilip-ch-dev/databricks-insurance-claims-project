output "bucket_name" {
  value = aws_s3_bucket.claims.bucket
}

output "iam_role_arn" {
  value = aws_iam_role.databricks_s3_access.arn
}

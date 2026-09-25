provider "aws" {
  region = "us-east-1"
}

# 1. Create the Raw Input Bucket
resource "aws_s3_bucket" "raw" {
  bucket_prefix = "raw-media-tf-"
  force_destroy = true
}

# 2. Create the Processed Output Bucket
resource "aws_s3_bucket" "processed" {
  bucket_prefix = "processed-media-tf-"
  force_destroy = true
}

# 3. Create the SNS Topic
resource "aws_sns_topic" "alerts" {
  name = "media-processing-alerts-tf"
}

# 4. Subscribe Your Email
resource "aws_sns_topic_subscription" "email_sub" {
  topic_arn = aws_sns_topic.alerts.arn
  protocol  = "email"
  endpoint  = "<YOUR_EMAIL_HERE>" # Placeholder
}
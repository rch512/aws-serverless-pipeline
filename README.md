# aws-serverless-pipeline

## Event-Driven Serverless Media Pipeline
An asynchronous, event-driven pipeline built on AWS to automatically process object storage uploads. This project eliminates idle server costs by using serverless compute that scales from zero to concurrent execution exactly when an S3 event fires, routing success alerts to a pub/sub messaging topic.

## Architecture

![image alt](https://github.com/rch512/aws-serverless-pipeline/blob/49beb7b223c3090e22b07b926232b92fce4548c6/docs/ArchServerless.svg)

Amazon S3 (Input): Receives raw media uploads.

S3 Event Notifications: Triggers an execution event on object creation.

AWS Lambda: Extracts metadata, dynamically maps the destination bucket, and writes the output file.

Amazon S3 (Output): Stores the processed artifact.

Amazon SNS: Fans out a real-time completion alert to subscribed email endpoints.

## Core Architectural Decisions
Preventing Recursive Loops: Specifically separated the trigger source (raw-media bucket) from the destination (processed-media bucket). Writing back to the trigger bucket is an anti-pattern that causes infinite Lambda invocation loops.

Least-Privilege IAM: Execution role restricted to s3:GetObject on the raw bucket, s3:PutObject on the processed bucket, and sns:Publish on the exact topic ARN.

Stateless Routing: Boto3 dynamically maps the destination bucket based on the incoming event payload (src_bucket.replace("raw", "processed")) rather than hardcoding endpoints, making the code environment-agnostic.

## Observability & Verification
The pipeline was tested in us-east-1 and verified via CloudWatch logs.

### S3 Trigger & Event Routing

Below: The S3 source trigger successfully invoking the processor, and the decoupled processed file landing in the destination bucket.

![image alt](https://github.com/rch512/aws-serverless-pipeline/blob/f480a7e3067d1a7e4ea653e6471760ec3596786a/docs/02-s3-processed-output.png)

### CloudWatch Telemetry

Below: End-to-end execution completed in ~522 ms utilizing 100 MB of the allocated 128 MB memory footprint.

![image alt](https://github.com/rch512/aws-serverless-pipeline/blob/9cc1834d4d924421cf97fc530be2e5908533c6be/docs/03-cloudwatch-execution.png)

## Infrastructure as Code (IaC)
This project includes a foundational Terraform configuration (`terraform/main.tf`) to automate the provisioning of the AWS resources. 

By defining the environment as code, the pipeline is entirely reproducible and aligns with standard cloud engineering practices. The Terraform script is configured to automatically deploy:
* The `raw-media` input S3 bucket.
* The `processed-media` output S3 bucket.
* The Amazon SNS topic and the required email subscription for alerting.

### SNS Alert Delivery
Below: The resulting fan-out email notification confirming the precise file processed.

![image alt](https://github.com/rch512/aws-serverless-pipeline/blob/9cc1834d4d924421cf97fc530be2e5908533c6be/docs/04-sns-email-delivery.png)

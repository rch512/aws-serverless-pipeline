import json
import boto3

s3 = boto3.client('s3')
sns = boto3.client('sns')

# Replace with your actual AWS Account ID when deploying
sns_topic_arn = "arn:aws:sns:us-east-1:<YOUR_ACCOUNT_ID>:media-processing-alerts"


def lambda_handler(event, context):
    print("Received S3 Event:", json.dumps(event))

    for record in event.get('Records', []):
        src_bucket = record['s3']['bucket']['name']
        src_key = record['s3']['object']['key']

        dst_bucket = src_bucket.replace("raw", "processed")
        dst_key = f"processed_{src_key}.txt"

        content = f"Event-driven processing successful for file: {src_key}".encode('utf-8')

        # 1. Write to S3
        s3.put_object(
            Bucket=dst_bucket,
            Key=dst_key,
            Body=content
        )
        print(f"Wrote processed record to {dst_bucket}/{dst_key}")

        # 2. Send SNS Email
        sns.publish(
            TopicArn=sns_topic_arn,
            Subject="AWS Serverless Pipeline Success!",
            Message=f"File {src_key} was processed and saved to {dst_bucket}."
        )
        print(f"Sent SNS alert for {src_key}")

    return {"statusCode": 200, "body": "Processing and Notification Complete"}
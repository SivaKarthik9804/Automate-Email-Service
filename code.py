
import boto3
import os
import json

# Initialize AWS SES client
ses = boto3.client('ses', region_name=os.getenv("AWS_REGION", "us-east-1"))

def lambda_handler(event, context):
     """AWS Lambda function to send emails using Amazon SES."""
    
    sender_email = os.getenv("SENDER_EMAIL", "your-email@example.com")
    recipient_email = os.getenv("RECIPIENT_EMAIL", "recipient@example.com")
    
    subject = "Automated Email from AWS Lambda"
    body_text = "Hello,\n\nThis is an automated email sent from AWS Lambda using Amazon SES."
    
    try:
        response = ses.send_email(
            Source=sender_email,
            Destination={"ToAddresses": [recipient_email]},
            Message={
                "Subject": {"Data": subject},
                "Body": {"Text": {"Data": body_text}}
            }
        )
        return {"statusCode": 200, "body": json.dumps({"message": "Email sent successfully!", "MessageId": response['MessageId']})}
    
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}

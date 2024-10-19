import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Retrieve the bucket name and key of the uploaded file
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    logger.info(f"New image uploaded: {key} in bucket {bucket}")
    
    # Add image processing logic here
    
    return {
        'statusCode': 200,
        'body': 'Image processed successfully'
    }

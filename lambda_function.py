import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log the event details
    logger.info(f"Received event: {json.dumps(event)}")

    # Extract bucket name and object key (file name)
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    logger.info(f"New image added: {object_key} in bucket: {bucket_name}")

    return {
        'statusCode': 200,
        'body': json.dumps('Image processed successfully. Also Lambda Function Updated.')
    }

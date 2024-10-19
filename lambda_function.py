import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        logger.info(f"Received event: {event}")

        if 'Records' in event:
            # Get the bucket name and object key
            bucket = event['Records'][0]['s3']['bucket']['name']
            key = event['Records'][0]['s3']['object']['key']

            # Check if the file is an image based on file extension
            if key.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                logger.info(f"New image uploaded: {key} in bucket {bucket}")
                # Add your image processing logic here
                
                return {
                    'statusCode': 200,
                    'body': 'Image processed successfully'
                }
            else:
                logger.warning(f"Non-image file detected: {key}")
                return {
                    'statusCode': 400,
                    'body': 'File is not an image. Skipping processing.'
                }
        else:
            logger.warning("No 'Records' found in the event.")
            return {
                'statusCode': 400,
                'body': "No valid S3 records found."
            }

    except KeyError as e:
        logger.error(f"KeyError: {e}")
        return {
            'statusCode': 500,
            'body': f"Error processing event: {str(e)}"
        }
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {
            'statusCode': 500,
            'body': f"Unexpected error: {str(e)}"
        }

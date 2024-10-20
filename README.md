# AWS Lambda S3 Trigger and Deployment via CodePipeline

This repository contains the Lambda function that logs an S3 image upload and a buildspec.yml file to automate Lambda updates via AWS CodePipeline and CodeBuild.

## Files:
- `lambda_function.py`: The Lambda function code that logs image uploads to S3.
- `buildspec.yml`: Used by AWS CodeBuild to package and deploy the Lambda function automatically.

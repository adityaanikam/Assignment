import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = "my-pdf-storage"  # Replace with your S3 bucket name
    file_name = event.get('fileName', 'default.pdf')
    file_content = event.get('fileContent')  # Base64 encoded content

    if not file_content:
        return {
            'statusCode': 400,
            'body': 'No file content provided.'
        }

    # Decode the file content
    decoded_content = base64.b64decode(file_content)

    # Upload the file to S3
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=decoded_content)

    return {
        'statusCode': 200,
        'body': f"File '{file_name}' uploaded successfully to bucket '{bucket_name}'."
    }
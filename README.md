

# AWS Lambda Functions - Add Numbers & Store Files in S3

## Overview
This project contains two AWS Lambda functions:
1. **Add Two Numbers**: Adds two numbers provided in the event payload and returns the result.
2. **Upload to S3**: Uploads a base64-encoded file (e.g., PDF) to an S3 bucket.


## Instructions

### 1. Add Two Numbers Lambda Function

#### Deployment:
1. Navigate to the `add_two_numbers_lambda` folder.
2. Upload the `lambda_function.py` file to AWS Lambda.
3. Set up a test event with the following structure:

```json
{
  "num1": 5,
  "num2": 10
}
```

#### Output:
The result of adding `num1` and `num2` will be returned:

```json
{
  "statusCode": 200,
  "body": {
    "result": 15
  }
}
```

---

### 2. Upload to S3 Lambda Function

#### Deployment:
1. Navigate to the `upload_to_s3_lambda` folder.
2. Install the required dependency (`boto3`).
   - If deploying via a .zip package, run `pip install boto3 -t .`.
3. Upload the `lambda_function.py` file to AWS Lambda.
4. Assign an IAM role to the Lambda function with `AmazonS3FullAccess` policy.

#### Test Event:
Use the following JSON structure:

```json
{
  "fileName": "example.pdf",
  "fileContent": "BASE64_ENCODED_CONTENT"
}
```

#### Output:
The function uploads the file to the specified S3 bucket and returns:

```json
{
  "statusCode": 200,
  "body": "File 'example.pdf' uploaded successfully to bucket 'my-pdf-storage'."
}
```

---

## Notes
- Ensure the S3 bucket name is updated in the `lambda_function.py` file.
- Use API Gateway to expose these Lambda functions as HTTP endpoints if needed.

---

## License
This project is licensed under the MIT License.

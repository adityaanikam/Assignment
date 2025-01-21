def lambda_handler(event, context):
    # Extract numbers from the event object
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)

    # Add the numbers
    result = num1 + num2

    # Return the result
    return {
        'statusCode': 200,
        'body': {
            'result': result
        }
    }
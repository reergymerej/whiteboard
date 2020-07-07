import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin":"*",
            "Content-Type": "application/json"
        },
        'body': json.dumps([
            'https://jex-whiteboard.s3.amazonaws.com/IMG_3556.JPG',
        ])
    }

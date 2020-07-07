import json
import boto3

def get_images():
    client = boto3.client('s3')
    response = client.list_objects_v2(
        Bucket='jex-whiteboard',
    )
    images = []
    for ob in response.get('Contents', []):
        name = ob.get('Key')
        if name[0] is 'I':
            modified = ob.get('LastModified')
            images.append({
                'name': 'https://jex-whiteboard.s3.amazonaws.com/' + name,
                'modified': modified.timestamp(),
            })

    return images

def lambda_handler(event, context):
    images = get_images()
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin":"*",
            "Content-Type": "application/json"
        },
        'body': json.dumps(images)
    }

if __name__ == '__main__':
    result = lambda_handler(None, None)
    print(result)

import os
import json

def lambda_handler(event, context):
    data = {
        "client_id": os.environ["client_id"],
        "client_secret": os.environ["client_secret"],
        "user_agent": os.environ["user_agent"],
    }
    return {
        "statusCode": 200,
        "body": json.dumps(data),
    }
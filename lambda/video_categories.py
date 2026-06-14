import json
import requests
import boto3
from datetime import datetime

s3 = boto3.client("s3")

API_KEY = "YOUR_YOUTUBE_API_KEY"
BUCKET = "youtube-data-engineering-vaibhav-2026"

def lambda_handler(event, context):

    url = f"https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode=IN&key={API_KEY}"

    response = requests.get(url)
    data = response.json()

    filename = f"bronze/raw_statistics_reference_data/categories_{datetime.now()}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=filename,
        Body=json.dumps(data)
    )

    return {
        "statusCode": 200,
        "body": "Category Data Stored Successfully"
    }
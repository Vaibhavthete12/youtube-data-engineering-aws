import json
import requests
import boto3
from datetime import datetime

s3 = boto3.client("s3")

API_KEY = "YOUR_YOUTUBE_API_KEY"
BUCKET = "youtube-data-engineering-vaibhav-2026"

def lambda_handler(event, context):

    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode=IN&maxResults=10&key={API_KEY}"

    response = requests.get(url)
    data = response.json()

    filename = f"bronze/raw_statistics/videos_{datetime.now()}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=filename,
        Body=json.dumps(data)
    )

    return {
        "statusCode": 200,
        "body": "YouTube Data Stored Successfully"
    }
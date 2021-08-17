import boto3
import os
import praw

from get_sentiment_scores import get_scores

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb", region_name=os.environ["region"]) 
    reddit = praw.Reddit(
        user_agent=os.environ["user_agent"],
        client_id=os.environ["client_id"],
        client_secret=os.environ["client_secret"],
    )
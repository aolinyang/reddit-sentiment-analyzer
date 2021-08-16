import boto3
import praw

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1') 

    reddit = praw.Reddit(
        user_agent="Comment Extraction (by u/USERNAME)",
        client_id="VnhXWuKiqpPgk8OwwRdLzg",
        client_secret="S0UJSe6AdzdcBNH4JMsJAaOMhZc0Sw",
        #username="sentiment-analyzer",
        #password="Yh89%$tQ",
    )

    submissions = reddit.subreddit('learnpython').hot(limit=1)
    id36 = ""
    for submission in submissions:
        print(submission.name)
        id36 = submission.name

    table = dynamodb.Table("subreddit_sentiments")
    new_item = {
        "subreddit_name": "learnpython",
        "date": 1,
        "id": id36,
    }
    table.put_item(Item=new_item)
    
    return {
        'statusCode': 200,
        'body': id36,
    }
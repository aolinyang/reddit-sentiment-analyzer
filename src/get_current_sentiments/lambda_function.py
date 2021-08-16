import praw

def lambda_handler(event, context):
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
    
    return {
        'statusCode': 200,
        'body': id36
    }
import praw

dynamodb = boto3.resource('dynamodb', region_name=os.environ["region"]) 

reddit = praw.Reddit(
    user_agent=os.environ["user_agent"],
    client_id=os.environ["client_id"],
    client_secret=os.environ["client_secret"],
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

# return {
#     'statusCode': 200,
#     'body': id36,
#     "newFunc": True,
# }
import praw

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
    # num = 0
    # for top_level_comment in submission.comments:
    #     if isinstance(top_level_comment, praw.models.MoreComments):
    #         continue
    #     print(top_level_comment.body)
    #     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #     num += 1
    # print(num)
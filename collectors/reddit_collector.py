import praw, os
from dotenv import load_dotenv
load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_ID"),
    client_secret=os.getenv("REDDIT_SECRET"),
    user_agent="osint_lab"
)

def fetch_reddit(subreddit="technology", limit=10):
    results = []
    for post in reddit.subreddit(subreddit).hot(limit=limit):
        results.append({
            "platform": "reddit",
            "user": str(post.author),
            "timestamp": str(post.created_utc),
            "text": post.title + " " + post.selftext,
            "url": f"https://reddit.com{post.permalink}"
        })
    return results

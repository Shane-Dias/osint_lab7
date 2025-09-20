import tweepy
import os

def fetch_twitter(query, max_tweets=10):
    bearer_token = os.getenv('TWITTER_BEARER_TOKEN') 
    
    client = tweepy.Client(bearer_token=bearer_token)
    
    tweets = []
    try:
        response = client.search_recent_tweets(
            query=query,
            max_results=max_tweets,
            tweet_fields=['created_at', 'author_id', 'text', 'public_metrics']
        )
        
        if response.data:
            for tweet in response.data:
                tweets.append({
                    'platform': 'twitter',
                    'content': tweet.text,
                    'timestamp': tweet.created_at,
                    'author': f"user_{tweet.author_id}",
                    'url': f"https://twitter.com/user/status/{tweet.id}"
                })
    except Exception as e:
        print(f"Twitter API error: {e}")
    
    return tweets
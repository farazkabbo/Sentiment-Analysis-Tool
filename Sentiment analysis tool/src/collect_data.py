import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize API
auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)

def fetch_tweets(keyword, count=100):
    tweets = tweepy.Cursor(api.search, q=keyword, lang="en").items(count)
    return [tweet.text for tweet in tweets]

if __name__ == "__main__":
    tweets = fetch_tweets("PointClickCare", 100)
    print(tweets)

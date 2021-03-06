import os
import tweepy
from datetime import date

auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

api = tweepy.API(auth)

if __name__ == '__main__':
    api.update_status(f"Today is {date.today().strftime('%A')}")

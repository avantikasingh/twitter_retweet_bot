import tweepy
from datetime import datetime, timedelta
from os import environ

#set keys
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler('CONSUMER_KEY','CONSUMER_SECRET')
auth.set_access_token('ACCESS_KEY','ACCESS_SECRET')

# Create API Object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)             #wait if rate limit is exceeded

#Update Profile Description
#api.update_profile(description="Your one-stop place for all Programming Memes!")

#set since to yesterday's date
sinceDate = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

#Retweet tweets with #programmingmemes, #ProgrammingMemes, #devjokes or #DevJokes
#Filter out retweets
for tweet in tweepy.Cursor(api.search, q=('#programmingmemes OR #devjokes -filter:retweets'), lang='en', since=sinceDate).items():
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

#follow back everyone who follows you
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Follow Back :"+follower.screen_name)

from tweets.models import Phrase, Tweet, TweetTimeline

import datetime
import json

def organize_tweets():
    today = datetime.date.today()
    yesterday = datetime.date.today() - datetime.timedelta(days=1)

    tweets = Tweet.objects.filter(tweet_date__range=[yesterday, today])
    tweet_list = {}

    for tweet in tweets:
        key = tweet.phrase.id
        if key in tweet_list:
            tweet_list[key] += 1
        else:
            tweet_list[key] = 1

    print(tweet_list)
    save_timeline(datetime.datetime.now(), json.dumps(tweet_list))

def save_timeline(day, tweet_list):
    TweetTimeline(
        date_tweeted = day,
        days_tweets = tweet_list
    ).save()

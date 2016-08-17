from tweets.models import Phrase, Tweet, TweetTimeline

import datetime
import json

def organize_tweets():
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday_min = datetime.datetime.combine(yesterday, datetime.time.min)
    yesterday_max = datetime.datetime.combine(yesterday, datetime.time.max)

    tweets = Tweet.objects.filter(tweet_date__range=(yesterday_min, yesterday_max))
    tweet_list = {}

    for tweet in tweets:
        key = tweet.phrase.id
        if key in tweet_list:
            tweet_list[key] += 1
        else:
            tweet_list[key] = 1

    save_timeline(yesterday, json.dumps(tweet_list))

def save_timeline(day, tweet_list):
    TweetTimeline(
        date_tweeted = day,
        days_tweets = tweet_list
    ).save()

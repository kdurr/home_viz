from tweets.models import Phrase, Tweet, TweetTimeline

import datetime
import json

def organize_tweets():
    today = datetime.date.today()
    today_min = datetime.datetime.combine(today, datetime.time.min)
    today_max = datetime.datetime.combine(today, datetime.time.max)

    tweets = Tweet.objects.filter(tweet_date__range=(today_min, today_max))
    tweet_list = {}

    for tweet in tweets:
        key = tweet.phrase.id
        if key in tweet_list:
            tweet_list[key] += 1
        else:
            tweet_list[key] = 1

    save_timeline(datetime.datetime.now(), json.dumps(tweet_list))

def save_timeline(day, tweet_list):
    TweetTimeline(
        date_tweeted = day,
        days_tweets = tweet_list
    ).save()

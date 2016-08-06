from tweets.models import Phrase, Tweet
from home_viz import twitter

import time
import datetime
# NOTE: remove warnings
# from django.utils import timezone

def collect_tweets():
    phrases = Phrase.objects.all()

    for phrase in phrases:
        query = phrase.phrase_text + " -filter:retweets AND -filter:replies"
        search_results = twitter.search(q=query, count=100)
        phrase_results = search_results['statuses']
        for result in phrase_results:
            save_tweets(phrase, result)

def save_tweets(phrase, tweet_data):
    tweet_time = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(string_date,'%a %b %d %H:%M:%S +0000 %Y'))
    formatted_date = datetime.datetime.strptime(tweet_time, "%Y-%m-%d %H:%M:%S.%f")

    tweet_exists = Tweet.objects.filter(phrase = phrase, tweet_text = tweet_data['text'], tweet_date = formatted_date).exists()

    if tweet_exists == False:
        Tweet(
            phrase = phrase_id,
            tweet_text = tweet_data['text'],
            tweet_location = tweet_data['coordinates'] + ' ' + tweet_data['user']['location'],
            tweet_date = formatted_date
        ).save()

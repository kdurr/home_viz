from django.db import models

from home_viz import twitter

import time

def collect_tweets():
    phrases = Phrase.objects.all()

    for phrase in phrases:
        query = phrase.phrase_text + " -filter:retweets AND -filter:replies"
        search_results = twitter.search(q=query, count=100)
        phrase_results = search_results['statuses']
        for result in phrase_results:
            save_tweets(phrase.id, result)

def save_tweets(phrase_id, tweet_data):
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet_data['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
    tweet_exists = Tweet.objects.filter(phrase = phrase_id, tweet_text = tweet_data['text'], tweet_date = formatted_time).exists()

    if tweet_exists:
        Tweet(
            phrase = phrase_id,
            tweet_text = tweet_data['text'],
            tweet_location = tweet_data['coordinates'] + ' ' + tweet_data['user']['location'],
            tweet_date = formatted_time
        ).save()

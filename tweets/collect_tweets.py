from tweets.models import Phrase, Tweet
from home_viz import twitter

# from django.utils.timezone import now
from datetime import datetime
import time

def collect_tweets():
    phrases = Phrase.objects.all()

    for phrase in phrases:
        query = '"' + phrase.phrase_text + '"' + " -filter:retweets AND -filter:replies"
        search_results = twitter.search(q=query, count=100)
        phrase_results = search_results['statuses']
        for result in phrase_results:
            save_tweets(phrase, result)

def save_tweets(phrase, tweet_data):
    formatted_date = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet_data['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
    tweet_date = datetime.strptime(formatted_date, '%Y-%m-%d %H:%M:%S')

    tweet_exists = Tweet.objects.filter(phrase = phrase, tweet_text = tweet_data['text'], tweet_date = formatted_date).exists()

    if tweet_exists == False:
        # NOTE: use user location instead of coordinates? - tweet_data['user']['location']
        Tweet(
            phrase = phrase,
            tweet_text = tweet_data['text'],
            tweet_location = format_location(tweet_data['coordinates']),
            tweet_date = tweet_date
        ).save()

def format_location(location):
    if location is None:
        return ''
    else:
        return location

from tweets.models import Phrase, Tweet

def organize_tweets():
    # find tweets from within today's date
    # tweet.tweet_date
    # {phrase_id: days count}

    tweet_list = {}
    tweets = some query for today's tweets
    for tweet in tweets:



def save_timeline(day, tweet_list):
    TweetTimeline(
        date_tweeted = day,
        days_tweets = tweet_list
    ).save()

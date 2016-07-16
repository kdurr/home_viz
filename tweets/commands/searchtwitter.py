# from celery.decorators import task
# from celery.utils.log import get_task_logger
from twython import Twython
from tweets.models import Phrase as phrase, Tweet as tweet

# logger = get_task_logger(__name__)
twitter = Twython(TWITTER_APP_KEY, TWITTER_APP_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_SECRET_TOKEN)

# @task(name='search_twitter_task')
def search_twitter_task():
    phrases = phrase.objects.all()

    for phrase in phrases:
        phrase_text = phrase.phrase_text
        self._search_specific_phrase(phrase_text)


def _search_specific_phrase(phrase):
    search_results = twitter.search(q=phrase, count=100)
    search_results['statuses']
    # search_results['statuses'] each
    # ['statuses'][0]['text']
    # ['statuses'][0]['created_at']
    # ['statuses'][0]['coordinates']
    # save to Tweets table unless it already exists with that tweet_date and tweet_text

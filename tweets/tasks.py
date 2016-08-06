from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from tweets.collect_tweets import collect_tweets
from tweets.organize_tweets import organize_tweets

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/1')),
    name='pull_tweets',
    ignore_result=True
)
@periodic_task(
    run_every=(crontab(hour='23')),
    # run_every=(crontab(minute='*/1')),
    name='create_tweet_timeline',
    ignore_result=True
)

def task_pull_tweets():
    """pings twitter and saves tweets to database"""
    collect_tweets()
    logger.info("Pinged Twitter")

def task_create_tweet_timeline():
    """creating tweet timeline"""
    organize_tweets()
    logger.info("Created today's tweet timeline")

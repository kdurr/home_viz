# from django.contrib.postgres.fields import JSONField
from django.db import models

class Phrase(models.Model):
    phrase_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.phrase_text

class Tweet(models.Model):
    phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=200)
    tweet_location = models.CharField(max_length=200)
    tweet_date = models.DateTimeField('date tweeted')

    def __unicode__(self):
        return self.tweet_text

# class TweetTimeline(models.Model):
#     date_tweeted = models.DateTimeField('date tweeted')
#     days_tweets = JSONField()
#
#     # {phrase_id: days count}
#
#     def __unicode__(self):
#         return self.phrase_count

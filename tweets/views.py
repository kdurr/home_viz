from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    phrases = Phrase.objects.all()
    tweet_timeline = TweetTimeline.objects.order_by('date_tweeted')

    daily_tweets = {}

    for timeline in tweet_timeline:
        timeline_list = {}
        for phrase, count in timeline.days_tweets:
            text = Phrase.objects.filter(id=phrase).first().phrase_text
            timeline_list[text] = count

        daily_tweets[timeline.date_tweeted] = timeline_list


    return HttpResponse(daily_tweets, content_type='application/json')

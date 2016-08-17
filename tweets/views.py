from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import ast

def index(request):
    phrases = Phrase.objects.all()
    tweet_timeline = TweetTimeline.objects.order_by('date_tweeted')

    daily_tweets = {}

    for timeline in tweet_timeline:
        timeline_list = {}
        days_tweets = ast.literal_eval(timeline.days_tweets)
        for phrase, count in days_tweets:
            text = Phrase.objects.filter(id=int(phrase)).first().phrase_text
            timeline_list[text] = count

        daily_tweets[timeline.date_tweeted] = timeline_list


    return HttpResponse(daily_tweets, content_type='application/json')

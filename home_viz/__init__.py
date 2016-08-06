from __future__ import absolute_import

from .celery import app as celery_app
from twython import Twython

# NOTE: use these from settings (import os)
APP_KEY = 'NELO3vTdiseeZBqvarS6ETbgL'
APP_SECRET = '30WyVSqCwWcjNoq17JbV9aIJNEC2Z0ky4JuNd5pUAlg503gROy'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

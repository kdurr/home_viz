from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home_viz.settings')
app = Celery('home_viz')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    BROKER_URL=os.environ.get('REDIS_URL'),
    CELERY_RESULT_BACKEND=os.environ.get('REDIS_URL')
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

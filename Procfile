web: gunicorn home_viz.wsgi --log-file -
worker: celery worker --app=tasks.app

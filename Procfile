web: gunicorn home_viz.wsgi --log-file -
worker: celery -A home_viz worker -B -l info

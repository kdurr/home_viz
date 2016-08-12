web: gunicorn home_viz.wsgi --log-file -
worker: python manage.py celery worker -B -l info

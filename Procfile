web: gunicorn agency.wsgi --log-file -
release: python manage.py migrate
worker: python manage.py celery worker -B -l info
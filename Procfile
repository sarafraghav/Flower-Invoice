web: gunicorn agency.wsgi --log-file -
release: python manage.py migrate
worker: celery -A agency worker -l info
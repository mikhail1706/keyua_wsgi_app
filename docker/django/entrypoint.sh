#!/usr/bin/env bash
echo "Collectstatic"
python manage.py collectstatic --no-input
echo "Apply migrations"
python manage.py migrate
echo "Start server"
gunicorn keyua_wsgi_app.wsgi:application --bind 0.0.0.0:8000 --workers 2 --timeout 300
exec "$@"

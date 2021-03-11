#!/usr/bin/env bash
echo "Launch worker"
celery -A keyua_wsgi_app worker --beat -l INFO
exec "$@"

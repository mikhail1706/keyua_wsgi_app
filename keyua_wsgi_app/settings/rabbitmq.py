from os import getenv
from kombu import Queue, Exchange
from celery.schedules import crontab
from datetime import timedelta

MQ_TYPE = getenv('MQ_TYPE', 'amqp')
RABBITMQ_HOST = getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = getenv('RABBITMQ_PORT', '5672')
RABBITMQ_VHOST = getenv('RABBITMQ_VHOST', '/')
RABBITMQ_USER = getenv('RABBITMQ_USERNAME', 'guest')
RABBITMQ_PASSWORD = getenv('RABBITMQ_PASSWORD', 'guest')

CONNECTION = f'{MQ_TYPE}://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/{RABBITMQ_VHOST}'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_ALWAYS_EAGER = False
CELERY_IGNORE_RESULT = True
CELERY_TASK_RESULT_EXPIRES = 1
CELERYD_MAX_TASKS_PER_CHILD = 1
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'default'
CELERY_DEFAULT_ROUTING_KEY = 'default'

CELERY_BEAT_SCHEDULE = {
    'update_cities': {
        'task': 'keyua_wsgi_app.apps.cities.tasks.update_cities',
        'schedule': timedelta(seconds=10),
    },
}

CELERY_QUEUES = [
    Queue('default', Exchange('default'), routing_key='default')
]
CELERY_ROUTES = {
    'keyua_wsgi_app.apps.cities.tasks.*': {
        'exchange': 'default',
        'routing_key': 'default'
    },
}
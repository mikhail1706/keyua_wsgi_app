from split_settings.tools import include

include(
    'apps.py',
    'common.py',
    'database.py',
    'auth.py',
    'rabbitmq.py',
    'logger.py',
    'redis.py',
)
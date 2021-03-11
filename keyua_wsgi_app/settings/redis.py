from os import getenv

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(getenv('REDIS_HOST', '127.0.0.1'),
                       getenv('REDIS_PORT'))],
            'prefix': getenv('REDIS_PREFIX')
        },
    },
}
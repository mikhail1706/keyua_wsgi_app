import os
import dotenv

from celery import Celery
from django.conf import settings

dotenv.load_dotenv(dotenv.find_dotenv())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'keyua_wsgi_app.settings')

app = Celery('keyua1_1', broker=settings.CONNECTION, backend='rpc')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
import requests
from django.contrib.auth.models import User

from keyua_wsgi_app.settings.common import ASGI_APP_URL


class ApiManager:
    def __init__(self, data: dict):
        self.first_app_url = ASGI_APP_URL
        self.data = data

    def update_cities(self):
        city_id = self.data.get('city_id')
        users = list(User.objects.filter(cities=city_id).values_list('id', flat=True))
        self.data.update({'users': users})
        requests.post(f'{self.first_app_url}/api/cities/update/{city_id}/', json=self.data)





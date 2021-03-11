import requests

from keyua_wsgi_app.apps.cities.models import City
from keyua_wsgi_app.settings.common import OPENWEATHER_API_KEY


class OpenWeatherMapManager:
    def __init__(self):
        self.api_key = OPENWEATHER_API_KEY

    def update_cities(self):
        for city in City.objects.all():
            request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city.city}&appid={self.api_key}&units=metric'
            res = requests.post(request_url, {})
            if res.status_code == 200:
                res = res.json()
                city.temperature = res['main']['temp']
                city.save(update_fields=['temperature'])

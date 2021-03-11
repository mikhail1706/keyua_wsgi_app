from keyua_wsgi_app.apps.tools.openweather import OpenWeatherMapManager
from keyua_wsgi_app.celery import app


@app.task
def update_cities():
    OpenWeatherMapManager().update_cities()

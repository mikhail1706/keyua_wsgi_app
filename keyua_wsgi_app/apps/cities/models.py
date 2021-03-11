from django.db import models
from django.contrib.auth.models import User
from keyua_wsgi_app.apps.tools.websokcets import ApiManager


class City(models.Model):
    city = models.CharField(max_length=32)
    temperature = models.DecimalField(decimal_places=1, max_digits=5)
    users = models.ManyToManyField(User, related_name='cities', blank=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.city

    def save(self, **kwargs):
        super(City, self).save(**kwargs)

        ApiManager({
            'city_id': self.id,
            'city': self.city,
            'temperature': str(self.temperature),
        }).update_cities()


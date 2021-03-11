from django.contrib import admin

from .models import City


class CityAdmin(admin.ModelAdmin):
    fields = ('city', 'temperature', 'users')
    # readonly_fields = ('users', )
    list_display = ('city', 'temperature')


admin.site.register(City, CityAdmin)
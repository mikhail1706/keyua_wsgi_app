from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('keyua_wsgi_app.apps.dashboard.urls')),
    path('cities/', include('keyua_wsgi_app.apps.cities.urls')),
    path('users/', include('keyua_wsgi_app.apps.users.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
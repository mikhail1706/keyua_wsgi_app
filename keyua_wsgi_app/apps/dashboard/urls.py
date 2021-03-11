from django.urls import path, include

from .views import DashboardView, ReadmeView, YourCitiesAjaxView

ajax_url_patterns = [
    path('your_cities/', YourCitiesAjaxView.as_view())
]

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('readme_page/', ReadmeView.as_view(), name='readme'),
    path('ajax/', include(ajax_url_patterns))
]
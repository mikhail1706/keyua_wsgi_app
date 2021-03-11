from django.urls import path, include

from .views import CitiesAjaxView, SubscribeCityView, UnSubscribeView, CitiesView

ajax_urlpatterns = [
    path('', CitiesAjaxView.as_view()),
]


urlpatterns = [
    path('', CitiesView.as_view(), name='cities'),
    path('subscribe/<int:city_id>/', SubscribeCityView.as_view()),
    path('unsubscribe/<int:city_id>/', UnSubscribeView.as_view()),
    path('ajax/', include(ajax_urlpatterns))
]

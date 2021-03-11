from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import TemplateView, View

from .models import City


class CitiesView(LoginRequiredMixin, TemplateView):
    template_name = 'cities.html'


class CitiesAjaxView(LoginRequiredMixin, View):
    def get(self, request):
        res = list()
        all_cities = City.objects.all()

        for city in all_cities:
            res.append({
                'id': city.id,
                'city': city.city,
                'temperature': city.temperature,
                'subscribed': request.user in city.users.all()})
        return JsonResponse(res, safe=False)


class SubscribeCityView(LoginRequiredMixin, View):
    def get(self, request, city_id):
        result = {'success': True, 'msg': 'The city successful subscribed'}
        if request.user.cities.count() == 5:
            result['success'] = False
            result['msg'] = 'You can subscribe only 5 cities'
        else:
            request.user.cities.add(city_id)
        return JsonResponse(result)


class UnSubscribeView(LoginRequiredMixin, View):
    def get(self, request, city_id):
        request.user.cities.remove(city_id)
        return JsonResponse({'success': True, 'msg': 'Unsubscribed!'})

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import JsonResponse


class ReadmeView(TemplateView):
    template_name = 'readme.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class YourCitiesAjaxView(View):
    def get(self, request):
        res = list(request.user.cities.values('id', 'city', 'temperature'))
        return JsonResponse(res, safe=False)




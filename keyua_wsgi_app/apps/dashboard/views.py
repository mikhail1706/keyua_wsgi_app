from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from keyua_wsgi_app.settings.common import ASGI_APP_WS_URL


class ReadmeView(TemplateView):
    template_name = 'readme.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super(DashboardView, self).get_context_data(**kwargs)
        ctx['ASGI_APP_WS_URL'] = ASGI_APP_WS_URL
        return ctx


class YourCitiesAjaxView(LoginRequiredMixin, View):
    def get(self, request):
        res = list(request.user.cities.values('id', 'city', 'temperature'))
        return JsonResponse(res, safe=False)




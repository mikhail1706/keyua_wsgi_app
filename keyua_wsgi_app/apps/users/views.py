from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'django_registration/registration_form.html'
    success_url = reverse_lazy('login')

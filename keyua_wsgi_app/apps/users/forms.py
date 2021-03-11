from django.contrib.auth.models import User


class AdminUserCustomForm(RegistrationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']



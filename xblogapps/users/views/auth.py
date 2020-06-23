from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

from ..forms.auth import AuthenticationForm

TEMPLATE_URL = 'xblogapps/users/auth'


class AuthLogin(LoginView):
    template_name = f'{TEMPLATE_URL}/login.html'
    form_class = AuthenticationForm

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render(self.request, f'{TEMPLATE_URL}/active_session.html')
        return super(AuthLogin, self).get(*args, **kwargs)


class AuthLogout(LogoutView):
    pass

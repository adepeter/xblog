from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationBackend:
    def authenticate(self, request, username, password, **kwargs):
        if kwargs.get('email'):
            username = kwargs['email']
        if not username or not password:
            return None
        try:
            user = User.objects.get_by_email_or_username(username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

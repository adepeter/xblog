from django.contrib.auth import get_user_model
from django.views.generic import DetailView, UpdateView
from django.utils.translation import gettext_lazy as _

from ..forms.profile import ProfileEditForm

User = get_user_model()

TEMPLATE_URL = 'xblogapps/users/profile'


class Profile(DetailView):
    model = User
    template_name = f'{TEMPLATE_URL}/profile.html'
    context_object_name = 'profile'


class ProfileEdit(UpdateView):
    model = User
    form_class = ProfileEditForm
    query_pk_and_slug = True
    template_name = f'{TEMPLATE_URL}/profile_edit.html'

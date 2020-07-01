from django.urls import include, path
from ..views import profile

urlpatterns = [
    path('<int:id>/<slug:slug>/', include([
        path('', profile.Profile.as_view(), name='view_profile'),
        path('edit/', profile.ProfileEdit.as_view(), name='edit_profile'),
    ])),
]

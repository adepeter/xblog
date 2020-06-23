from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('graphql/', include('xblogapps.urls')),
    path('', include('xblogapps.urls', namespace='xblog')),
]

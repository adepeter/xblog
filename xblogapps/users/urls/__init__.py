from django.urls import include, path

app_name = 'users'

urlpatterns = [
    path('graphql/', include('xblogapps.users.graphql.urls')),
    path('auth/', include('xblogapps.users.urls.auth')),
    path('', include('xblogapps.users.urls.user')),
]

from django.urls import include, path

app_name = 'users'

urlpatterns = [
    # path('graphql/', include('gqlapps.users.graphql.urls')),
    # path('user/', include('gqlapps.users.urls.user')),
    path('', include('xblogapps.users.urls.user')),
]

from django.urls import include, path

urlpatterns = [
    path('graphql/', include('xblogapps.categories.graphql.urls')),

]

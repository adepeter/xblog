from django.urls import include, path
from django.views.generic import ListView

from .blogs.models import Article

app_name = 'xblog'

# urlpatterns = [
#     path('blogs/', include('gqlapps.blogs.urls')),
#     path('categories/', include('gqlapps.categories.urls')),
#     path('users/', include('gqlapps.users.urls')),
#     path('', include('gqlapps.categories.graphql.urls')),
# ]

class Homepage(ListView):
    paginate_by = 10
    model = Article
    template_name = 'xblogapps/index.html'
    context_object_name = 'articles'


urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('categories/', include('xblogapps.categories.urls')),
    path('blogs/', include('xblogapps.blogs.urls', namespace='blogs')),
    path('users/', include('xblogapps.users.urls', namespace='users')),
]
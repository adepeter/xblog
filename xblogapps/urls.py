from django.urls import include, path
from django.views.generic import TemplateView

from .blogs.models import Article

app_name = 'xblog'

# urlpatterns = [
#     path('blogs/', include('gqlapps.blogs.urls')),
#     path('categories/', include('gqlapps.categories.urls')),
#     path('users/', include('gqlapps.users.urls')),
#     path('', include('gqlapps.categories.graphql.urls')),
# ]

class Homepage(TemplateView):
    template_name = 'xblogapps/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context


urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    # path('categories/', include('xblogapps.categories.urls')),
    path('blogs/', include('xblogapps.blogs.urls', namespace='blogs')),
    path('users/', include('xblogapps.users.urls', namespace='users')),
]

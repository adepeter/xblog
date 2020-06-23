from django.urls import include, path

from ..blogs.views.article import ArticleList, ArticleRead

app_name = 'blogs'

# urlpatterns = [
#     path('graphql/', include('gqlapps.blogs.graphql.urls'))
# ]

urlpatterns = [
    path('<slug:category_slug>/', include([
        path('', ArticleList.as_view(), name='article_list'),
        path('<int:article_id>/<slug:article_slug>/', \
             ArticleRead.as_view(), name='article_read'),
    ])),
]

from django.urls import include, path

from ..blogs.views.article import ArticleList, ArticleRead
from ..blogs.views.post import ReplyPost

app_name = 'blogs'

urlpatterns = [
    path('graphql/', include('xblogapps.blogs.graphql.urls'))
]

urlpatterns += [
    path('<slug:category_slug>/', include([
        path('', ArticleList.as_view(), name='article_list'),
        path('<int:article_id>/<slug:article_slug>/', \
             ArticleRead.as_view(), name='article_read'),
        path('<slug:article_slug>/<int:parent_post_id>/reply-post/', ReplyPost.as_view(), \
             name='reply_post'),
    ])),
]

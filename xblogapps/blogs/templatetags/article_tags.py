from django import template
from django.db.models import Count

from ..models import Article

register = template.Library()


@register.simple_tag(name='newest_articles')
def latest_articles(items=5):
    return Article.objects.filter(
        is_hidden=False
    ).order_by('created')[:items]

@register.simple_tag(name='trending_articles')
def popular_articles(items=5):
    return Article.objects.filter(
        is_hidden=False
    ).annotate(
        count_posts=Count('posts')
    ).order_by('created')[:items]

from django import template

from ..models import Post

register = template.Library()


@register.simple_tag(name='list_posts')
def all_posts(items=5):
    return Post.objects.filter(
        is_hidden=False
    ).order_by('created')[:items]
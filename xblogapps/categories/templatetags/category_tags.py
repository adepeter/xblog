from django import template
from django.db.models import Count, Q

from ..models import Category

register = template.Library()

@register.simple_tag(name='list_categories')
def list_category():
    return Category.objects.filter(parent__isnull=False, is_lock=False)

@register.simple_tag(name='categories')
def categories_dropdown():
    categories = Category.objects.filter(
        Q(parent__isnull=True) |
        Q(parent__isnull=False, is_lock=True)
    )
    return categories
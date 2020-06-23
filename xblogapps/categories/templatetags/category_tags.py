from django import template

from ..models import Category

register = template.Library()

@register.simple_tag(name='list_categories')
def list_category():
    return Category.objects.filter(parent__isnull=False, is_lock=False)
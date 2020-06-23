from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Article, Post


class PostStackedInline(admin.StackedInline):
    model = Post
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'title', 'slug']
    # fields = [('title', 'slug'),]
    list_display = [
        'title',
        'id',
        'user',
        'slug',
        'category',
        'content',
        'total_posts',
        'is_hidden',
        'created',
        'modified',
        'is_locked'
    ]
    search_fields = ['title', 'user', 'slug', 'content']
    list_filter = ['is_hidden', 'user', 'category', 'is_locked']
    prepopulated_fields = {
        'slug': ('title',),
    }
    inlines = [PostStackedInline]

    def total_posts(self, obj):
        return obj.posts.count()
    total_posts.short_description = _('Total posts')

from django.db import models


class ArticleManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(
            is_hidden=False
        ).order_by('-modified')

    def get_articles(self):
        return super().get_queryset().order_by('-modified')
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.DO_NOTHING,
        related_name='posts_written',
        blank=True,
        null=True
    )
    article = models.ForeignKey(
        'blogs.Article',
        verbose_name=_('article'),
        on_delete=models.CASCADE,
        related_name='posts'
    )
    content = models.TextField()
    is_hidden = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.content[:10]

    def is_child(self):
        return bool(self.parent)

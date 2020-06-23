from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ...cores.utils import ImageHandler

image_hander = ImageHandler()


class Article(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.DO_NOTHING,
        related_name='articles_written'
    )
    category = models.ForeignKey(
        'categories.Category',
        verbose_name=_('category'),
        on_delete=models.CASCADE,
        related_name='articles',
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        unique=True
    )
    image = models.ImageField(
        upload_to=image_hander.upload_handler,
        blank=True,
        null=True
    )
    slug = models.SlugField(blank=True)
    # tags = ArrayField(models.SlugField(), blank=True, null=True)
    content = models.TextField(unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    is_hidden = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_article_image(self):
        image = image_hander.stringify_image_url(self.image)
        return image

    def get_absolute_url(self):
        kwargs = {
            'category_slug': self.category.slug,
            'article_id': self.id,
            'article_slug': self.slug
        }
        return reverse('xblog:blogs:article_read', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} just created a {self.title}'

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ...cores.utils import ImageHandler

from ..managers.user import UserManager

image_hander = ImageHandler()


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('e-mail'),
        unique=True
    )
    username = models.CharField(
        verbose_name=_('username'),
        max_length=20,
    )
    avatar = models.ImageField(
        verbose_name=_('Profile picture'),
        upload_to=image_hander.upload_handler,
        blank=True
    )
    slug = models.SlugField(blank=True)
    is_active = models.BooleanField(
        verbose_name=_('active status'),
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name=_('Is staff'),
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name=_('Is superuser'),
        default=False
    )
    firstname = models.CharField(
        verbose_name=_('First name'),
        max_length=50, blank=True
    )
    lastname = models.CharField(
        verbose_name=_('Last name'),
        max_length=50, blank=True
    )
    dob = models.DateField(
        verbose_name=_('Date of Birth'),
        blank=True,
        null=True
    )
    about = models.TextField(
        verbose_name=_('About Me'),
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(default=timezone.now)
    website = models.URLField(default='https://', blank=True)
    github = models.URLField(default='https://github.com/', blank=True)
    facebook = models.URLField(default='https://facebook.com/', blank=True)
    twitter = models.URLField(default='https://twitter.com/@', blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def display_age(self):
        if self.dob:
            now = timezone.now().date()
            years = now.year - self.dob.year

    def get_avatar_url(self):
        return image_hander.stringify_image_url(self.avatar, 'no_thumbnails.png')

    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'.title()

    def get_short_name(self):
        return self.username

    @property
    def get_display_name(self):
        if self.firstname or self.lastname:
            return self.get_full_name().rstrip()
        return self.username

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'username'],
                name='user_unique_email_username'
            )
        ]

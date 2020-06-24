from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.utils.html import format_html

MEDIA_ROOT = settings.MEDIA_ROOT


class ImageHandler:
    def upload_handler(self, instance, filename):
        random_int = timezone.now() - instance.created
        filename = str(random_int.microseconds) + '_' + filename
        instance_content_type = ContentType.objects.get_for_model(instance)
        app_name = instance_content_type.app_label
        instance_model = instance_content_type.model
        return f'{app_name}/{instance_model}/{filename}'

    def _image_display(self, obj, custom_image=None):
        if obj and hasattr(obj, 'url'):
            image = obj.avatar.url
        else:
            custom_image = custom_image if custom_image is not None else 'no_thumbnail.png'
            image = f'{MEDIA_ROOT}/{custom_image}'
        return image

    def display_image(self, obj, custom_image_url=None):
        image = self._image_display(obj, custom_image_url)
        return format_html('<img src="%(image_path)s" />' % {'image_path': image})

    def stringify_image_url(self, obj, custom_image=None):
        return self._image_display(obj, custom_image)

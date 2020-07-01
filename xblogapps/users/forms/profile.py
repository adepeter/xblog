from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ProfileEditForm.Meta.fields:
            self.fields[field].widget.attrs.update({
                'place_holder': _('Please enter your %s') % field,
                'class': 'form-control'
            })
    class Meta:
        model = User
        fields = [
            'email',
            'avatar',
            'firstname',
            'lastname',
            'dob',
            'about',
            'website',
            'facebook',
            'github',
            'twitter',
        ]

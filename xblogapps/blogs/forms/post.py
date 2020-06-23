from django import forms
from django.utils.translation import gettext_lazy as _

from ...users.models import User

from ..models import Post


class BasePostForm:

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.article = kwargs.pop('article')
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'cols': '58',
            'rows': '7',
            'class': 'sm-form-control',
            'placeholder': _('Enter yor reply'),
        })


class PostForm(BasePostForm, forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

    def save(self, commit=True):
        post = super().save(commit=False)
        post.user = self.request.user
        post.article = self.article
        if commit:
            post.save()
        return post


class AnonymousUserPostForm(BasePostForm, forms.Form):

    def __init__(self, *args, **kwargs):
        del kwargs['instance']
        super().__init__(*args, **kwargs)
        for field in list(self.fields):
            field_name = self.fields[field].label
            placeholder = f'Please enter your {field_name}'
            if field == 'content':
                continue
            self.fields[field].widget.attrs.update({
                'size': '22',
                'class': 'sm-form-control',
                'placeholder': _('%(field_name)s' % {'field_name': placeholder})
            })

    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    website = forms.URLField(required=False)
    content = forms.CharField(widget=forms.Textarea)

    def save(self, *args, **kwargs):
        email = self.cleaned_data['email']
        username = email[:email.index('@')]
        user = User(
            username=username,
            email=email,
            firstname=self.cleaned_data['first_name'],
            lastname=self.cleaned_data['last_name']
        )
        user.set_unusable_password()
        user.save()
        post = Post.objects.create(
            article=self.article,
            content=self.cleaned_data['content'],
            user=user
        )
        return post

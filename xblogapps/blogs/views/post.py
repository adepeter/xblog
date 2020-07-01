from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView

from ..viewmixins.post import BaseReplyPostMixin

from ..forms.post import ReplyPostForm
from ..models import Post

TEMPLATE_URL = 'xblogapps/blogs'


class ReplyPost(LoginRequiredMixin, BaseReplyPostMixin, CreateView):
    form_class = ReplyPostForm
    template_name = f'{TEMPLATE_URL}/reply_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = f'{TEMPLATE_URL}/delete_post.html'

    def get_success_url(self):
        return

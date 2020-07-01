from django.urls import reverse_lazy

from ..models import Post


class BasePostMixin:
    model = Post
    slug_url_kwarg = 'article_slug'
    query_pk_and_slug = True

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(article__category__slug=self.kwargs['category_slug'])

    def get_slug_field(self):
        return 'article__slug'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        kwargs['article'] = self.get_object()
        return kwargs

    def get_success_url(self):
        kwargs = {
            'category_slug': self.kwargs['category_slug'],
            'article_id': self.object.article.id,
            'article_slug': self.kwargs['article_slug'],
        }
        return reverse_lazy('xblog:blogs:article_read', kwargs=kwargs)


class BaseReplyPostMixin(BasePostMixin):
    pk_url_kwarg = 'parent_post_id'
    context_object_name = 'parent'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent'] = self.get_object()
        return context

    def get_form_kwargs(self):
        parent = self.get_object()
        kwargs = super().get_form_kwargs()
        kwargs['article'] = parent.article
        kwargs['parent'] = parent
        return kwargs

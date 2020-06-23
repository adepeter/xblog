from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from django.utils.translation import gettext_lazy as _

from ...categories.models import Category

from ..forms.post import PostForm, AnonymousUserPostForm
from ..models import Article

TEMPLATE_URL = 'xblogapps/blogs'


class ArticleList(SingleObjectMixin, ListView):
    slug_url_kwarg = 'category_slug'
    template_name = f'{TEMPLATE_URL}/article_list.html'
    query_pk_and_slug = False
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(Category.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object
        context['articles'] = self.get_queryset()
        return context

    def get_queryset(self):
        qs = self.object.articles
        return qs.all()

    def get_slug_field(self):
        return str('slug__iexact')


class ArticleRead(MultipleObjectMixin, CreateView):
    model = Article
    query_pk_and_slug = True
    pk_url_kwarg = 'article_id'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'posts'
    template_name = f'{TEMPLATE_URL}/article_read.html'

    def get(self, request, *args, **kwargs):
        self.article = self.get_object()
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)

    def get_object(self):
        article = super().get_object(self.get_thread())
        return article

    def get_thread(self):
        return self.model.objects.filter(
            category__slug__iexact=self.kwargs['category_slug']
        )

    def post(self, request, *args, **kwargs):
        self.object_list = None
        self.article = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.article
        return context

    def get_queryset(self):
        return self.article.posts.all()

    def get_form_class(self):
        if self.request.user.is_authenticated:
            return PostForm
        return AnonymousUserPostForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        kwargs['article'] = self.get_object()
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, _('Your post was successfulled added'))
        return super().form_valid(form)

    def get_success_url(self):
        kwargs = {
            'category_slug': self.kwargs['category_slug'],
            'article_id': self.kwargs['article_id'],
            'article_slug': self.kwargs['article_slug'],
        }
        return reverse_lazy('xblog:blogs:article_read', kwargs=kwargs)

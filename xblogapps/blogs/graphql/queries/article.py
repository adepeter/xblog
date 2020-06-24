import graphene
from django.shortcuts import get_object_or_404

from ...models import Article

from ..types.article import ArticleType


class ArticleQuery(graphene.ObjectType):
    articles = graphene.List(
        ArticleType,
        id=graphene.ID(),
        slug=graphene.String()
    )
    article = graphene.Field(
        ArticleType,
        category=graphene.String(),
        id=graphene.ID(),
        slug=graphene.String()
    )

    def resolve_articles(self, info, **kwargs):
        id, slug = kwargs.get('id'), kwargs.get('slug')
        if id and slug is not None:
            return Article.objects.filter(category__id=id, category__slug__iexact=slug)
        return Article.objects.all()

    def resolve_article(self, info, category, id, slug, **kwargs):
        return get_object_or_404(
            Article,
            category__slug__iexact=category,
            id=id,
            slug__iexact=slug
        )

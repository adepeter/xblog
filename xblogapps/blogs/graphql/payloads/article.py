from django.shortcuts import get_object_or_404

import graphene

from ....categories.models import Category

from ....blogs.models import Article

from ..inputs.article import ArticleCreateInput, ArticleEditInput, ArticleDeleteInput
from ..types.article import ArticleType


class ArticleCreatePayload(graphene.Mutation):
    article = graphene.Field(ArticleType)
    is_created = graphene.Boolean(default_value=False)

    class Arguments:
        input = ArticleCreateInput(required=True)

    def mutate(self, info, input):
        category = get_object_or_404(
            Category,
            id=input.category.id,
            slug__iexact=input.category.slug
        )
        new_article = Article.objects.create(
            category=category,
            title=input.article.title,
            slug=input.article.slug,
            user=info.context.user,
            content=input.article.content
        )
        is_created = True
        return ArticleCreatePayload(is_created=is_created, article=new_article)

class ArticleEditPayload(graphene.Mutation):
    article = graphene.Field(ArticleType)
    is_edited = graphene.Boolean(default_value=False)

    class Arguments:
        input = ArticleEditInput(required=True)

    def mutate(self, info, input):
        article = get_object_or_404(
            Article,
            category__slug__iexact=input.category,
            id=input.id,
            slug=input.slug
        )
        article.title = input.patch.title
        article.slug = input.patch.slug
        article.content = input.article.content
        article.save()
        is_edited = True
        return ArticleEditPayload(article=article, is_edited=is_edited)

class ArticleDeletePayload(graphene.Mutation):
    articles = graphene.List(ArticleType)

    class Arguments:
        input = ArticleDeleteInput(required=True)

    def mutate(self, info, input):
        article = get_object_or_404(
            Article,
            category__slug__iexact=input.category,
            id=input.id,
            slug=input.slug
        )
        article.delete()
        is_deleted = True
        return ArticleDeletePayload(
            is_deleted=is_deleted,
            articles=Article.objects.all()
        )
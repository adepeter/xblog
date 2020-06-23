import graphene

from ..payloads.article import (
    ArticleCreatePayload,
    ArticleDeletePayload,
    ArticleEditPayload
)


class ArticleMutation(graphene.ObjectType):
    article_create = ArticleCreatePayload.Field()
    article_delete = ArticleDeletePayload.Field()
    article_edit = ArticleEditPayload.Field()

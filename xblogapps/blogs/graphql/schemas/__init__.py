import graphene

from .article import ArticleSchemaQuery, ArticleSchemaMutation


class Query(ArticleSchemaQuery, graphene.ObjectType):
    pass


class Mutation(ArticleSchemaMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

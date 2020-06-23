import graphene
from graphene_django.types import DjangoObjectType

from ....categories.graphql.types import CategoryType
from ....users.graphql.types.user import UserType

from ...models import Article

from .post import PostType


class ArticleType(DjangoObjectType):
    category = graphene.Field(CategoryType)
    user = graphene.Field(UserType)
    posts = graphene.List(PostType)
    total_posts = graphene.Int(
        description='Returns total number of posts in an article'
    )

    class Meta:
        model = Article

    def resolve_posts(self, info, **kwargs):
        """All posts in a article"""
        return self.posts.all()

    def resolve_total_posts(self, info, **kwargs):
        """Total number of posts per article"""
        return self.posts.count()
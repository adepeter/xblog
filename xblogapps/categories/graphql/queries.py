import graphene

from ...categories.models import Category

from .types import CategoryType


class CategoryQuery(graphene.ObjectType):
    category = graphene.Field(CategoryType, id=graphene.ID(), slug=graphene.String())
    categories = graphene.List(CategoryType)

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_category(self, info, id, slug):
        return Category.objects.get(id=id, slug=slug)

import graphene


class BaseArticleInputMixin(graphene.InputObjectType):
    """Abstract input class supplied to lookup thread by ID and Slug"""
    id = graphene.ID()
    slug = graphene.String()


class CategoryFetchInput(BaseArticleInputMixin):
    """Abstract input class supplied to supply category id and slug"""


class BaseArticleCreateInput(graphene.InputObjectType):
    """New article abstract input class"""
    id = graphene.ID
    slug = graphene.String()
    title = graphene.String()
    content = graphene.String()


class ArticleCreateInput(graphene.InputObjectType):
    """Input to create new article"""
    category = CategoryFetchInput(
        description='A field that supplies ID and Slug of the Category the Article will'
                    'belong to'
    )
    article = BaseArticleCreateInput(
        description='New article fields'
    )


class ArticleEditInput(BaseArticleInputMixin):
    """Input for updating article"""
    category = graphene.String(
        description='Category slug'
    )
    patch = graphene.InputField(
        BaseArticleCreateInput,
        description='Fields to edit'
    )

class ArticleDeleteInput(BaseArticleInputMixin):
    """Input field for article deletion"""
    category = graphene.String(
        description='slug of category article belongs to'
    )
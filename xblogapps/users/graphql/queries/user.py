from django.contrib.auth import get_user_model

import graphene

from ..types.user import UserType

User = get_user_model()


class UserQueries(graphene.ObjectType):
    users = graphene.List(UserType)
    me = graphene.Field(UserType)
    user = graphene.Field(
        UserType,
        pk=graphene.Int(),
        id=graphene.ID(),
        slug=graphene.String()
    )

    def resolve_me(self, info):
        user = info.context.user
        return user

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, **kwargs):
        print('pk' in kwargs)
        if 'pk' in kwargs:
            id = kwargs.get('pk')
        slug = kwargs.get('slug')
        if id is not None and slug is not None:
            return User.objects.get(pk=id, slug__iexact=slug)
        return None

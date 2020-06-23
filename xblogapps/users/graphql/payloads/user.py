from django.contrib.auth import get_user_model

import graphene

from ..inputs.user import (
    UserCreateInput,
    # UserDeleteInput,
    # UserEditInput
)
from ..types.user import UserType

User = get_user_model()


class UserCreatePayload(graphene.Mutation):
    user = graphene.Field(UserType)
    is_created = graphene.Boolean()

    class Arguments:
        input = UserCreateInput(required=True)

    def mutate(self, info, input=None):
        user = User.objects.create_user(
            email=input.email,
            username=input.username,
            password=input.password
        )
        is_created = True
        return UserCreatePayload(user=user, is_created=is_created)


# class UserDeletePayload(graphene.Mutation):
#     users = graphene.List(UserType)
#     is_deleted = graphene.Boolean()
#
#     class Arguments:
#         input = UserDeleteInput(required=True)
#
#     def mutate(self, info, input=None):
#         pass
#
#     def resolve_users(self, info, **kwargs):
#         pass
#
#
# class UserEditPayload(graphene.Mutation):
#     user = graphene.Field(UserType)
#     is_edited = graphene.Boolean()
#
#     class Arguments:
#         input = UserEditInput(required=True)
#
#     def mutate(self, info, input=None):
#         pass

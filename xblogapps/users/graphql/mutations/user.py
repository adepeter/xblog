import graphene

from ..payloads.user import (
    UserCreatePayload,
    # UserDeletePayload,
    # UserEditPayload
)


class UserMutations(graphene.ObjectType):
    user_create = UserCreatePayload.Field()
    # user_delete = UserDeletePayload.Field()
    # user_edit = UserEditPayload.Field()

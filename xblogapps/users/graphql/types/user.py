from django.contrib.auth import get_user_model
from django.utils import timezone

import graphene
from graphene_django.types import DjangoObjectType

User = get_user_model()


class UserType(DjangoObjectType):
    age = graphene.Int()
    password = graphene.String()

    class Meta:
        model = User

    def resolve_password(self, info, **kwargs):
        if info.context.user == self:
            return self.password
        return

    def resolve_age(self, info, **kwargs):
        if self.dob is not None:
            now = timezone.now().date()
            diff = now.year - self.dob.year
            return diff
        return

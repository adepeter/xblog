import graphene


class BaseUserInputMixin(graphene.InputObjectType):
    id = graphene.ID()
    slug = graphene.String()


class UserCreateInput(graphene.InputObjectType):
    id = graphene.ID
    email = graphene.String()
    username = graphene.String()
    password = graphene.String()


class UserBasicPatchInput(graphene.InputObjectType):
    email = graphene.String()
    dob = graphene.Date()


class UserBasicEditInput(BaseUserInputMixin):
    patch = graphene.InputField(UserBasicPatchInput)


class UserPasswordChangePatchInput(graphene.InputObjectType):
    old_password = graphene.String()
    new_password = graphene.String()
    repeated_password = graphene.String()


class UserPasswordChangeEditInput(BaseUserInputMixin):
    patch = graphene.InputField(UserPasswordChangePatchInput)

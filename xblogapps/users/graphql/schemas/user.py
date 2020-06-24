import graphene

from ..mutations.user import UserMutations
from ..queries.user import UserQueries


class Query(UserQueries, graphene.ObjectType):
    pass


class Mutation(UserMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

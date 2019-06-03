from graphene import ObjectType, Schema
from instagraphql_django.users.schema import Query as UserQuery


class Query(UserQuery, ObjectType):
    """
    This class will inherit multiple Queries as we begin to add more apps
    """


schema = Schema(query=Query)


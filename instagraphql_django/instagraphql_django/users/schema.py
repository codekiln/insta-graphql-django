import graphene
from graphene_django import DjangoObjectType

from instagraphql_django.users.models import User


class UserType(DjangoObjectType):
    class Meta(object):
        model = User


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()


schema = graphene.Schema(query=Query)

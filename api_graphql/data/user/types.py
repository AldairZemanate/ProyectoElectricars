from graphene_django import DjangoObjectType
from graphene.relay import Node
from users.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields=['user_name']
        # {
        #     'user_name':['exact','icontains']
        # }
        interfaces=(Node,)
from graphene.types.objecttype import ObjectType

from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField
from .types import UserNode

from graphene_django.forms.mutation import DjangoModelFormMutation
from users.forms import UserModelForm




class Query(ObjectType):
    user=Node.Field(UserNode)
    all_users=DjangoFilterConnectionField(UserNode)
  
class userMutation(DjangoModelFormMutation):
    class Meta:
        form_class= UserModelForm

class Mutation(ObjectType):
    create_user= userMutation.Field()
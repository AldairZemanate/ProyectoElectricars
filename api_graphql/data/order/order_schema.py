from graphene.types.objecttype import ObjectType
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from orders.forms import OrderModelForm
from .types import OrderNode

class Query(ObjectType):
    oder=Node.Field(OrderNode)
    all_orders= DjangoFilterConnectionField(OrderNode)

class OrderMutation(DjangoModelFormMutation):
    class Meta:
        form_class= OrderModelForm


class Mutation(ObjectType):
    create_Order=OrderMutation.Field()

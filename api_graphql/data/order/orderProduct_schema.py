import imp
from graphene_django.forms.mutation import DjangoModelFormMutation
from orders.forms import OrderProductModelForm
from graphene.types.objecttype import ObjectType
from graphene.relay import Node
from .types import OrderProductNode
from graphene_django.filter import DjangoFilterConnectionField

class Query(ObjectType):
    orderProduct=Node.Field(OrderProductNode)
    all_orderProduct= DjangoFilterConnectionField(OrderProductNode)

class OrderProductMutation(DjangoModelFormMutation):
    class Meta:
        form_class=OrderProductModelForm
        
class Mutation(ObjectType):
    create_OrderProdutc=OrderProductMutation.Field()
from graphene_django import DjangoObjectType
from graphene.relay import Node
from products.models import Product


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields=['prod_name']
        interfaces=(Node,)
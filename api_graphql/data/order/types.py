from pyexpat import model
from orders.models import Order,OrderProduct
from graphene_django import DjangoObjectType
from graphene.relay import Node

class OrderNode(DjangoObjectType):
    class Meta:
        model = Order
        filter_fields={
            #especializacion de los filtros con diccionario
            'ord_state':['exact'],
            'ord_date':['exact']
        }
        interfaces=(Node,)

class OrderProductNode(DjangoObjectType):
    class Meta:
        model =OrderProduct
        filter_fields=['quantity',]
        interfaces=(Node,)
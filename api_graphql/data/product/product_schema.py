#define todo el comportamiento de un nodo de grafo mapeando directamente a un modelo de una app
from .types import ProductNode
from graphene.relay import Node
from graphene import ObjectType
from graphene_django.filter import DjangoFilterConnectionField

from graphene_django.forms.mutation import DjangoModelFormMutation
from products.forms import ProductModelForm

    
class Query(ObjectType):
    product= Node.Field(ProductNode)
    all_products=DjangoFilterConnectionField(ProductNode)


#djangomodelformmutation realizara tomando como base un formulario de modelo 
class ProductMutation(DjangoModelFormMutation):
    class Meta:
        form_class=ProductModelForm

#nodo de acceso
class Mutation(ObjectType):
    create_product=ProductMutation.Field()
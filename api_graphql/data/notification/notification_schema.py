from graphene.types.objecttype import ObjectType
from .types import NotificationNode
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from notifications.forms import NotificationModelForm

#mutaciones
from graphene_django.forms.mutation import DjangoModelFormMutation



class Query(ObjectType):
    notification = Node.Field(NotificationNode)
    all_notifications=DjangoFilterConnectionField(NotificationNode)

#mutaciones
class NotificationMutation(DjangoModelFormMutation):
    class Meta:
        form_class= NotificationModelForm

class Mutation(ObjectType):
    create_Notification=NotificationMutation.Field()

from graphene_django import DjangoObjectType
from graphene.relay import Node
from notifications.models import Notification
class NotificationNode(DjangoObjectType):
    class Meta:
        model = Notification
        filter_fields={
            'not_title':['exact']
        }
        interfaces=(Node,)
from graphene import ObjectType,Schema,String

#importacion para que me devuelva una lista

from .data.product.product_schema import Query as ProductQuery ,Mutation as ProductMutation
from .data.order.order_schema import Query as OrderQuery, Mutation as OrderMutation
from .data.order.orderProduct_schema import  Query as orderProductQuery,Mutation as OrderProductMutation
from .data.notification.notification_schema import Query as QueryNotification, Mutation as NotificationMutation
from .data.user.user_schema import Query as UserQuery, Mutation as MutationUser
from .auth_schema import Mutation as AuthMutation
#punto de acceso

class Query(ProductQuery,OrderQuery,QueryNotification,UserQuery,orderProductQuery):
    pass

class Mutation(ProductMutation,OrderMutation,NotificationMutation,AuthMutation,OrderProductMutation,MutationUser):
    pass
schema= Schema(query=Query,mutation=Mutation)
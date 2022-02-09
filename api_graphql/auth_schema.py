from graphene import ObjectType
import graphql_jwt

class Mutation(ObjectType):
    token_auth= graphql_jwt.ObtainJSONWebToken.Field()
    verity_token= graphql_jwt.Verify.Field()
    refresh_token=graphql_jwt.Refresh.Field()
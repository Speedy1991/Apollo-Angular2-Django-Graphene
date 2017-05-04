import graphene
from graphene_django import DjangoObjectType
from graphene import Node, relay
from .models import User, Email
from graphene_django.filter import DjangoFilterConnectionField


class EmailNode(DjangoObjectType):
    class Meta:
        model = Email
        interfaces = (Node, )


class UserNode(DjangoObjectType):
    emails = graphene.List(EmailNode)

    @graphene.resolve_only_args
    def resolve_emails(self):
        return Email.objects.filter(user=self)

    class Meta:
        model = User
        interfaces = (Node, )
        filter_fields = ("first_name", )


class AddUser(relay.ClientIDMutation):
    class Input:
        first_name = graphene.String(requiered=True)
        last_name = graphene.String(required=True)

    user = graphene.Field(UserNode)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        first_name = input.get("first_name")
        last_name = input.get("last_name")

        user = User.objects.create(first_name=first_name, last_name=last_name)

        return AddUser(user=user)


class Query(graphene.ObjectType):
    users = DjangoFilterConnectionField(UserNode)
    all_users = graphene.List(UserNode)

    email = Node.Field(EmailNode)
    emails = graphene.List(EmailNode)

    @graphene.resolve_only_args
    def resolve_all_users(self):
        return User.objects.all()

    @graphene.resolve_only_args
    def resolve_emails(self):
        return Email.objects.all()


class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

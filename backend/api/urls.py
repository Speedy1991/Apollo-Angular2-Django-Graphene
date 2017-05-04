from graphene_django.views import GraphQLView
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^$', csrf_exempt(GraphQLView.as_view())),
    url(r'graphiql/$', GraphQLView.as_view(graphiql=True)),
]
from rest_framework import routers
from django.urls import path, include
from . import views as news_view
from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', news_view.listing, name='listing'),
    path('paper/<int:id>', news_view.newspaper, name='listing'),
    # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

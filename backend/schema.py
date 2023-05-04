import graphene
from graphene_django import DjangoObjectType

from employees.models import Occupation


class OccupationType(DjangoObjectType):
    class Meta:
        model = Occupation
        fields = '__all__'


class Query(graphene.ObjectType):
    get_occupation = graphene.Field(OccupationType, occupation_id=graphene.ID())
    get_occupations = graphene.List(OccupationType)

    def resolve_get_occupation(self, info, occupation_id):
        return Occupation.objects.get(id=occupation_id)

    def resolve_get_occupations(self, info):
        return Occupation.objects.all()


schema = graphene.Schema(query=Query)

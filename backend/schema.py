import datetime
import graphene
from graphene_django import DjangoObjectType

from employees.models import Occupation


class OccupationType(DjangoObjectType):
    """Класс для связи с моделью Django."""

    class Meta:
        model = Occupation
        fields = '__all__'


class Query(graphene.ObjectType):
    """Класс для описания запросов."""

    get_occupation = graphene.Field(OccupationType, occupation_id=graphene.ID())
    get_occupations = graphene.List(OccupationType)

    def resolve_get_occupation(root, info, occupation_id):
        """
        При запросе getOccupation(occupation_id) отдает конкретную
        запись из БД.
        """

        return Occupation.objects.get(id=occupation_id)

    def resolve_get_occupations(root, info):
        """При запросе getOccupations отдает все записи из БД."""

        return Occupation.objects.all()


class OccupationMutation(graphene.Mutation):
    """Мутация для создания Occupation."""

    class Arguments:
        name = graphene.String(required=True)
        company_name = graphene.String(required=True)
        position_name = graphene.String(required=True)
        hire_date = graphene.Date(required=True)
        fire_date = graphene.Date()
        salary = graphene.Int(required=True)
        fraction = graphene.Int(required=True)
        base = graphene.Int(required=True)
        advance = graphene.Int(required=True)
        by_hours = graphene.Boolean(required=True)

    ok = graphene.Boolean()
    occupation = graphene.Field(OccupationType)

    def mutate(root,
               info,
               name,
               company_name,
               position_name,
               salary,
               fraction,
               base,
               advance,
               by_hours,
               hire_date,
               fire_date=None,):
        """Возвращает объект мутации с созданным occupation."""

        occupation = Occupation.objects.create(
            name=name,
            company_name=company_name,
            position_name=position_name,
            hire_date=hire_date,
            fire_date=fire_date,
            salary=salary,
            fraction=fraction,
            base=base,
            advance=advance,
            by_hours=by_hours
        )
        return OccupationMutation(occupation=occupation, ok=True)


class UpdateOccupationMutation(graphene.Mutation):
	"""Мутация для обновления Occupation."""

	class Arguments:
		id = graphene.ID()
		name = graphene.String()
		company_name = graphene.String()
		position_name = graphene.String()
		hire_date = graphene.Date()
		fire_date = graphene.String()
		salary = graphene.Int()
		fraction = graphene.Int()
		base = graphene.Int()
		advance = graphene.Int()
		by_hours = graphene.Boolean()

	ok = graphene.Boolean()
	occupation = graphene.Field(OccupationType)

	def mutate(root, info, id, **update_data):
		"""Возвращает объект мутации с обновленным occupation."""

		occupation = Occupation.objects.get(id=id)

		for key, value in update_data.items():
			if isinstance(update_data[key], bool):
				setattr(occupation, key, value)
			else:
				if update_data[key]:
					setattr(occupation, key, value)

		occupation.save()

		return UpdateOccupationMutation(occupation=occupation, ok=True)


class FireOccupationMutation(graphene.Mutation):
	"""Мутация для обновления Occupation."""

	class Arguments:
		id = graphene.Int()

	ok = graphene.Boolean()
	occupation = graphene.Field(OccupationType)

	def mutate(root, info, id):
		"""Возвращает объект мутации с обновленным occupation."""

		current_date = datetime.datetime.today()
		occupation = Occupation.objects.get(id=id)

		occupation = Occupation.objects.get(id=id)
		occupation.fire_date = current_date
		occupation.save(update_fields=['fire_date'])

		return FireOccupationMutation(occupation=occupation, ok=True)


class Mutation(graphene.ObjectType):
    add_occupation = OccupationMutation.Field()
    update_occupation = UpdateOccupationMutation.Field()
    fire_occupation = FireOccupationMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

from django.contrib import admin

from .models import Occupation


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'position_name',
        'hire_date',
        'fire_date',
        'salary',
        'fraction',
        'base',
        'advance',
        'by_hours'
    )
    search_fields = ('name',)

from django.contrib import admin

from .models import Occupation


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'position_name'
    )
    search_fields = ('name',)

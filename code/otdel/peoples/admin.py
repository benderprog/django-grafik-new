from django.contrib import admin
from .models import Person, Rank, Duty


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'rank',
        'full_name',
        'age',
        'job_title',
        'duty',
        'utk',
    )
    list_display_links = 'pk', 'full_name'


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    list_display_links = 'pk', 'name'


@admin.register(Duty)
class DutyAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
    )
    list_display_links = 'pk', 'name'

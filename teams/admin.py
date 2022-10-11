from django.contrib import admin
from .models import TeamTextSection, Team


# Register your models here.
class TeamTextSectionInline(admin.StackedInline):
    model = TeamTextSection


class TeamAdminView(admin.ModelAdmin):
    inlines = [TeamTextSectionInline]
    list_display = ('name', )

admin.site.register(Team, TeamAdminView)

from django.contrib import admin
from .models import TeamTextSection, Team


# Register your models here.
class TeamTextSectionInline(admin.StackedInline):
    model = TeamTextSection


class TeamAdminView(admin.ModelAdmin):
    inlines = [TeamTextSectionInline]
    list_display = ('name', )
    fields = ('name', 'contact_person', 'contact_person_function', 'contact_person_phone', 'contact_mail', 'website',
              'banner_picture', 'logo', 'slogan', 'team_picture')


admin.site.register(Team, TeamAdminView)

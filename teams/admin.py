from django.contrib import admin
from .models import TeamTextSection, Team, TeamFact


# Register your models here.
class TeamTextSectionInline(admin.StackedInline):
    model = TeamTextSection

class TeamFactInline(admin.TabularInline):
    model = TeamFact
    min_num = 3
    max_num = 4
    fields = ('icon', 'icon_html', 'value', 'context')
    readonly_fields = ('icon_html', )


class TeamAdminView(admin.ModelAdmin):
    inlines = [TeamFactInline, TeamTextSectionInline]
    list_display = ('name', )
    exclude = ('slug', )


admin.site.register(Team, TeamAdminView)

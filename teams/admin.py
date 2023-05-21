from django.contrib import admin
from .models import TeamTextSection, Team, TeamFact, TeamAccount


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
    fieldsets = [
        (None, {"fields": ["name", "slogan"]}),
        ("Contact details", {
            "fields": ["contact_person", "contact_person_function", "contact_person_phone", "contact_mail", "website"]
        }),
        ("Images", {
            "fields": ["front_page_picture", "banner_picture", "logo", "logo_svg", "main_color"]
        })
    ]

    def get_queryset(self, request):
        """
        Admin accounts can edit each team.
        Team accounts can edit their own team.
        Other accounts do not have any access.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'team_account'):
            return qs.filter(pk=request.user.team_account.team.pk)
        return qs.none()


admin.site.register(Team, TeamAdminView)
admin.site.register(TeamAccount)

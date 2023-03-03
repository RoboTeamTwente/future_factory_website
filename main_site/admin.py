from gettext import ngettext

from django.contrib import admin, messages

from main_site.models import Email
from teams.models import Team


class RecipientListFilter(admin.SimpleListFilter):
    """
    Allows to filter emails based on the recipient.
    This could also be done by just filtering on 'recipient', however general mails are marked as '-'
    (since they point to None) this filter will print Future Factory instead.
    """
    title = "Recipient"
    parameter_name = "recipient_custom"

    def lookups(self, request, model_admin):
        options = [('FF', 'Future Factory')]
        for team in Team.objects.all():
            options.append((team.pk, team.name))
        return options

    def queryset(self, request, queryset):
        if self.value() == 'FF':
            return queryset.filter(recipient=None)
        elif self.value() is not None:
            return queryset.filter(recipient__pk=self.value())


class ReadListFilter(admin.SimpleListFilter):
    title = "Read"
    parameter_name = "read"

    def lookups(self, request, model_admin):
        return (
            ('R', 'Read'),
            ('U', 'Unread'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'R':
            return queryset.filter(read=True)
        if self.value() == 'U':
            return queryset.filter(read=False)

class EmailModelAdmin(admin.ModelAdmin):
    readonly_fields = ('email_sender', 'receiver', 'message')
    fields = ('email_sender', 'receiver', 'message', 'read')
    list_display = ('email_sender', 'receiver', 'read')
    list_filter = (RecipientListFilter, ReadListFilter)
    actions = ['mark_as_read']

    @admin.action(description="Mark the selected emails as read")
    def mark_as_read(self, request, queryset):
        updated = queryset.update(read=True)
        self.message_user(request, ngettext(
            '%d email was successfully marked as read.',
            '%d emails were successfully marked as read.',
            updated,
        ) % updated, messages.SUCCESS)


admin.site.register(Email, EmailModelAdmin)

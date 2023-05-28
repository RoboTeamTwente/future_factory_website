from django.contrib import admin, messages
from django.utils.translation import ngettext

from events.models import Event


class EventModelAdmin(admin.ModelAdmin):
    ordering = ['-start']
    list_display = ('title', 'start', 'end', 'entire_day', 'visible')
    actions = ['hide_events', 'show_events']

    @admin.action(description="Mark the selected events as hidden")
    def hide_events(self, request, queryset):
        updated = queryset.update(visible=False)
        self.message_user(request, ngettext(
            '%d event is successfully marked as hidden.',
            '%d events are successfully marked as hidden.',
            updated
        ) % updated, messages.SUCCESS)

    @admin.action(description="Mark the selected events as visible")
    def show_events(self, request, queryset):
        updated = queryset.update(visible=True)
        self.message_user(request, ngettext(
            '%d event is successfully marked as visible.',
            '%d events are successfully marked as visible.',
            updated
        ) % updated, messages.SUCCESS)


admin.site.register(Event, EventModelAdmin)

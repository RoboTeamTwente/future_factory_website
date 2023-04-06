from django.contrib import admin

from events.models import Event


class EventModelAdmin(admin.ModelAdmin):
    ordering = ['-start']
    list_display = ('title', 'start', 'end', 'visible')


admin.site.register(Event, EventModelAdmin)

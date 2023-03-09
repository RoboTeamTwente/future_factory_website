from django.contrib import admin

from events.models import Event


class EventModelAdmin(admin.ModelAdmin):
    ordering = ['-date']
    list_display = ('title', 'date', 'visible')


admin.site.register(Event, EventModelAdmin)

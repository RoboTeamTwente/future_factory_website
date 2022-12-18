from django.contrib import admin

from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible')


admin.site.register(Event, EventAdmin)

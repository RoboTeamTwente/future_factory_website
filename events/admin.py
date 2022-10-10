from django.contrib import admin

from .models import *

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('summary', 'visible')

admin.site.register(Event, EventAdmin)

from django.contrib import admin
from main_site.models import PressPicture


class PressPictureModelAdmin(admin.ModelAdmin):
    fields = ('picture', 'image_preview')
    readonly_fields = ('image_preview', )


admin.site.register(PressPicture, PressPictureModelAdmin)

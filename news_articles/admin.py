from gettext import ngettext

from django.contrib import admin, messages

from .models import *


class ParagraphInline(admin.StackedInline):
    model = Paragraph
    min_num = 1


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'visible')
    actions = ['hide_events', 'show_events']
    ordering = ['-date']
    inlines = [ParagraphInline]

    @admin.action(description="Mark the selected news articles as hidden")
    def hide_events(self, request, queryset):
        updated = queryset.update(visible=False)
        self.message_user(request, ngettext(
            '%d news article is successfully marked as hidden.',
            '%d news articles are successfully marked as hidden.',
            updated
        ) % updated, messages.SUCCESS)

    @admin.action(description="Mark the selected news articles as visible")
    def show_events(self, request, queryset):
        updated = queryset.update(visible=True)
        self.message_user(request, ngettext(
            '%d news article is successfully marked as visible.',
            '%d news articles are successfully marked as visible.',
            updated
        ) % updated, messages.SUCCESS)


admin.site.register(NewsArticle, NewsArticleAdmin)

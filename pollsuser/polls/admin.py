from django.contrib import admin

from polls.models import Poll, Question


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = 'title', 'date_start', 'date_end', 'description',
    list_display_links = 'title',
    list_filter = 'title', 'date_start', 'date_end',

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = 'text_q', 'type_q',
    list_display_links = 'text_q',
    list_filter = 'text_q', 'type_q',

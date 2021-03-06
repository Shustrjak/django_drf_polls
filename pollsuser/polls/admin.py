from django.contrib import admin

from polls.models.answers import Answer
from polls.models.polls import Poll
from polls.models.questions import Question


class QuestionInlines(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = 'title', 'date_start', 'date_end', 'description',
    list_display_links = 'title',
    list_filter = 'title', 'date_start', 'date_end',
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Type', {'fields': ['description']}),
    ]
    inlines = [QuestionInlines]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    def short_text(self, obj: Answer):
        if len(obj.text) > 30:
            return f'{obj.text[:30]}...'
        return obj.text

    list_display = 'short_text', 'question_id', 'checked',
    list_display_links = 'short_text',
    list_filter = 'text',


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = 'text_q', 'type_question',
    list_display_links = 'text_q',
    list_filter = 'text_q', 'type_question',

    fieldsets = [
        (None, {'fields': ['text_q']}),
        ('Type', {'fields': ['type_question']}),
    ]
    inlines = [AnswerInline]

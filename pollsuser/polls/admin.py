from django.contrib import admin

from polls.models import Poll, TypeAnswer, TextQuestion, Answer, OneQuestion, ManyQuestion


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = 'title', 'date_start', 'date_end', 'description',
    list_display_links = 'title',
    list_filter = 'title', 'date_start', 'date_end',


# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = 'text_q', 'type_question',
#     list_display_links = 'text_q',
#     list_filter = 'text_q', 'type_question',


@admin.register(TextQuestion)
class TextQuestionAdmin(admin.ModelAdmin):
    list_display = 'text',
    list_display_links = 'text',
    list_filter = 'text',


@admin.register(OneQuestion)
class OneQuestionAdmin(admin.ModelAdmin):
    list_display = 'poll',
    list_display_links = 'poll',
    list_filter = 'poll',


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    def short_text(self, obj: Answer):
        if len(obj.text) > 30:
            return f'{obj.text[:30]}...'
        return obj.text

    list_display = 'short_text',
    list_display_links = 'short_text',
    list_filter = 'text',


@admin.register(TypeAnswer)
class TypeAnswerAdmin(admin.ModelAdmin):
    list_display = 'title',
    list_display_links = 'title',
    list_filter = 'title',


@admin.register(ManyQuestion)
class ManyQuestionAdmin(admin.ModelAdmin):
    list_display = 'poll', 'text_q',
    list_display_links = 'poll', 'text_q',
    list_filter = 'poll', 'text_q',

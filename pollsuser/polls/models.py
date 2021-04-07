from django.db import models

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    poll_id = models.IntegerField(blank=False, null=False)
    question_id = models.IntegerField(blank=False, null=False)
    text = models.CharField(max_length=500, default=None, blank=True, null=True)
    checked = models.BooleanField(default=None, blank=True, null=True)


class TypeAnswer(models.Model):
    ANSWER_CHOICES = [
        ('1', 'TextQuestion'),
        ('2', 'OneQuestion'),
        ('3', 'ManyQuestion'),
    ]
    title = models.CharField(max_length=255, choices=ANSWER_CHOICES, null=True)


class Question(models.Model):
    type_question = models.CharField(max_length=100, null=True, default='Question')
    text_q = models.TextField(max_length=1000, verbose_name='Вопрос')
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, default='1')

    class Meta:
        abstract = True
        ordering = ['order_id', '-updated_at']


class TextQuestion(Question):
    text = models.TextField(default='', verbose_name='Текстовый ответ')

    def __init__(self, *args, **kwargs):
        super(TextQuestion, self).__init__(*args, **kwargs)
        self.type_question = __class__.__name__

    class Meta:
        indexes = [models.Index(fields=['poll'])]

class OneQuestion(Question):
    var_answer = models.ManyToManyField('Answer', limit_choices_to=None)

    def __init__(self, *args, **kwargs):
        super(OneQuestion, self).__init__(*args, **kwargs)
        self.type_question = __class__.__name__

    class Meta:
        indexes = [models.Index(fields=['poll'])]

class ManyQuestion(Question):
    many_answer = models.ManyToManyField('Answer')

    def __init__(self, *args, **kwargs):
        super(ManyQuestion, self).__init__(*args, **kwargs)
        self.type_question = __class__.__name__

    class Meta:
        indexes = [models.Index(fields=['poll'])]



# Create your models here.
class Poll(models.Model):
    poll_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default='', unique=True, verbose_name='Заголовок')
    date_start = models.DateTimeField(auto_now_add=True, verbose_name='Старт опроса')
    date_end = models.DateTimeField(auto_now=True, verbose_name='Конец опроса')
    description = models.TextField(verbose_name='Описание опроса', max_length=1000)


    class Meta:
        ordering = ['-poll_id']

    def __str__(self):
        return f'{self.title}'

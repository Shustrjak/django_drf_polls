from django.db import models


class TypeAnswer(models.Model):
    ANSWER_CHOICES = [
        ('TYPE_1', 'type_1'),
        ('TYPE_2', 'type_2'),
        ('TYPE_3', 'type_3'),
    ]
    title = models.CharField(max_length=255)


class Question(models.Model):

    text_q = models.TextField(max_length=1000, verbose_name='Вопрос')
    type_q = models.ForeignKey(TypeAnswer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text_q}'


# Create your models here.
class Poll(models.Model):
    poll_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default='', unique=True, verbose_name='Заголовок')
    date_start = models.DateTimeField(auto_now_add=True, verbose_name='Старт опроса')
    date_end = models.DateTimeField(auto_now=True, verbose_name='Конец опроса')
    description = models.TextField(verbose_name='Описание опроса', max_length=1000)
    select_question = models.ManyToManyField(Question)

    class Meta:
        ordering = ['-poll_id']

    def __str__(self):
        return f'{self.title}'

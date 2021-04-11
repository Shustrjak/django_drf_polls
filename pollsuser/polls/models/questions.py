from django.db import models


class Question(models.Model):
    ANSWER_CHOICES = [
        ('1', 'TextQuestion'),
        ('2', 'OneQuestion'),
        ('3', 'ManyQuestion'),
    ]
    type_question = models.CharField(max_length=100, null=True, default='Question', choices=ANSWER_CHOICES)
    text_q = models.TextField(max_length=1000, verbose_name='Вопрос')
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.text_q}'

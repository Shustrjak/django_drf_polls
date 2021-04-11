from django.db import models


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

from django.db import models

from polls.models.polls import Poll
from polls.models.questions import Question


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, blank=False, null=False, on_delete=models.CASCADE)
    text = models.CharField(max_length=500, default='', blank=True, null=True)
    checked = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        if str(self.text) is None:
            return None
        if len(str(self.text)) > 10:
            return f'{self.text[:10]}...'
        return self.text

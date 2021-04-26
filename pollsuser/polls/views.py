from rest_framework.viewsets import ModelViewSet

from .models.polls import Poll
from .models.answers import Answer
from .models.questions import Question
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class PollViewSet(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('title',)


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('question_id',)


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    field_labels = 'type_question',
    filterset_fields = ('type_question', 'poll')


from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models.polls import Poll
from .models.answers import Answer
from .models.questions import Question
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer


class PollViewSet(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

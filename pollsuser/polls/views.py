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

from rest_framework import serializers
from polls.models.answers import Answer
from polls.models.polls import Poll
from polls.models.questions import Question


class PollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poll
        fields = 'title', 'date_start', 'date_end', 'description'


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = 'type_question', 'text_q', 'poll'


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = 'poll_id', 'question_id', 'text', 'checked', 'poll_id_id'

    poll_id = PollSerializer()
    question_id = QuestionSerializer()

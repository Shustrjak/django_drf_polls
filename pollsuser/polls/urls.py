from django.urls import path, include
from .views import PollViewSet, AnswerViewSet, QuestionViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet)
router.register('answers', AnswerViewSet)
router.register('questions', QuestionViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))

]

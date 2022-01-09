from django.urls import path
from .views import VisualizerView, VisualizerQuestion


urlpatterns = [
    path('<int:voting_id>/', VisualizerView.as_view()),
    path('',VisualizerQuestion.as_view()),
]

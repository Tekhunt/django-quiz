from django.urls import path
from .views import Home, QuizIdsView


urlpatterns = [
    path('api/home/', Home.as_view(), name='home'),
    path('quiz-ids/<str:store>/', QuizIdsView.as_view(), name='quiz_ids'),
]

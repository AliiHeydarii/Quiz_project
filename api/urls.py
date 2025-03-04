from django.urls import path
from . import views

urlpatterns = [
    path('quiz/' , views.QuizListApiView.as_view()),
    path('quiz/<int:pk>/', views.QuizDetailApiView.as_view())
]
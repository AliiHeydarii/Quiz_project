from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index_view , name='index'),
    path('quiz/<int:pk>/',views.quize_detail,name='quiz-detail'),
]
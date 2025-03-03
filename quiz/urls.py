from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index_view , name='index'),
    path('quize/<int:pk>/',views.quize_detail,name='quiz-detail'),
]
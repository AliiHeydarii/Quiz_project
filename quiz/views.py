from django.shortcuts import render
from .models import Quiz,Question

def index_view(request):
    quiz_list = Quiz.objects.all()
    return render(request , 'quiz/index.html' , {'quiz_list' : quiz_list})


def quize_detail(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = Question.objects.filter(quiz=quiz)
    if request.method == 'POST':
        score = 0
        for question in questions:
            answer = request.POST.get(f'question_{question.id}')
            if answer == question.correct_answer :
                score += 1
        print(score)
    return render(request,'quiz/quiz_detail.html' , {'questions' : questions})



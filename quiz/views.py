from django.shortcuts import render
from .models import Quiz,Question,UserAnswer
from django.contrib.auth.decorators import login_required

@login_required()
def index_view(request):
    quiz_list = Quiz.objects.all()
    for quiz in quiz_list:
        user_answer = UserAnswer.objects.filter(user=request.user , quiz=quiz).first()
    return render(request , 'quiz/index.html' , {'quiz_list' : quiz_list,'user_answer' : user_answer})

@login_required()
def quize_detail(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = Question.objects.filter(quiz=quiz)

    if UserAnswer.objects.filter(user = request.user , quiz = quiz).exists():
        return render(request,'quiz/already_taken.html')

    if request.method == 'POST':
        score = 0
        for question in questions:
            answer = request.POST.get(f'question_{question.id}')
            if answer == question.correct_answer :
                score += 1

        user_answer = UserAnswer.objects.filter(user=request.user).first()
        if user_answer:
            print('user')
        else:
            UserAnswer.objects.create(
                user = request.user,
                quiz = quiz , 
                score = score
            )
        return render(request , 'quiz/result.html' , {'score' : score})
    return render(request,'quiz/quiz_detail.html' , {'questions' : questions})



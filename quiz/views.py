from django.shortcuts import render
from .models import Quiz,Question,UserAnswer
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required()
def index_view(request):
    quiz_list = Quiz.objects.all()
    user_answers = UserAnswer.objects.filter(user=request.user)
    total_score = user_answers.aggregate(total_score=Sum('score'))['total_score']
    for quiz in quiz_list:
        quiz.user_answer = user_answers.filter(quiz=quiz).first()

    return render(request , 'quiz/index.html' , {'quiz_list' : quiz_list , 'total_score' : total_score })


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

        UserAnswer.objects.get_or_create(
            user=request.user,
            quiz=quiz,
            score=score
        )
        return render(request , 'quiz/result.html' , {'score' : score , 'quiz' : quiz})
    return render(request,'quiz/quiz_detail.html' , {'questions' : questions , 'quiz' : quiz})



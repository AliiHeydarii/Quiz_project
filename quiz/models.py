from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Quiz(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Question(models.Model):

    ANSWER_CHOICES = [
        ('answer1' , 'itme 1'),
        ('answer2' , 'itme 2'),
        ('answer3' , 'itme 3'),
        ('answer4' , 'itme 4'),
    ]

    text = models.TextField()
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questions')
    answer1 = models.CharField(max_length=250)
    answer2 = models.CharField(max_length=250)
    answer3 = models.CharField(max_length=250)
    answer4 = models.CharField(max_length=250)

    correct_answer = models.CharField(max_length=10 , choices=ANSWER_CHOICES)
    

    def __str__(self):
        return self.text

    
# class Choice(models.Model):
#     question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='choices')
#     text = models.CharField(max_length=300)
#     is_correct = models.BooleanField(default=False)

#     def __str__(self):
#         return self.text
    

class UserAnswer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answers')
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}-{self.quiz.title}-{self.score}'
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Quiz(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quiz-detail' , kwargs={'pk' : self.pk})
    
    
class Question(models.Model):

    ANSWER_CHOICES = [
        ('option1' , 'option1'),
        ('option2' , 'option2'),
        ('option3' , 'option3'),
        ('option4' , 'option4'),
    ]

    text = models.TextField()
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questions')
    option1 = models.CharField(max_length=250)
    option2 = models.CharField(max_length=250)
    option3 = models.CharField(max_length=250)
    option4 = models.CharField(max_length=250)

    correct_answer = models.CharField(max_length=10 , choices=ANSWER_CHOICES)
    

    def __str__(self):
        return self.text

    

class UserAnswer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answers')
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}-{self.quiz.title}-{self.score}'
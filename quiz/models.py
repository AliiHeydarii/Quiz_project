from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Quiz(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questions')

    def __str__(self):
        return self.text

    
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='choices')
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
    
class UserAnswer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answers')
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='user_answers')
    selected_choice = models.ForeignKey(Choice,on_delete=models.CASCADE,related_name='user_selections')
    created_at = models.DateTimeField(auto_now_add=True)

    def is_correct(self):
        return self.selected_choice.is_correct

    def __str__(self):
        return f'{self.user.email}-{self.question.text}-{self.selected_choice.text}'
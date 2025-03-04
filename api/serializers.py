from rest_framework import serializers
from quiz.models import Quiz,Question , UserAnswer
from django.contrib.auth import get_user_model

User = get_user_model

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email']



class QuizSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()
    user_score = serializers.SerializerMethodField()
    class Meta:
        model = Quiz
        fields = ['title' , 'absolute_url','user_score']

    def get_absolute_url(self,obj):
        return f'http://0.0.0.0:8000/api{obj.get_absolute_url()}'
    
    def get_user_score(self,obj):
        request = self.context.get('request')
        user_answer = UserAnswer.objects.filter(user=request.user,quiz=obj).first()
        return user_answer.score


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text' , 'answer1' , 'answer2', 'answer3' , 'answer4']
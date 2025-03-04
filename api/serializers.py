from rest_framework import serializers
from quiz.models import Quiz,Question


class QuizSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = '__all__'

    def get_absolute_url(self,obj):
        return obj.get_absolute_url()
    
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text' , 'answer1' , 'answer2', 'answer3' , 'answer4']
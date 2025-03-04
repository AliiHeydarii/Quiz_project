from rest_framework import serializers
from quiz.models import Quiz,Question , UserAnswer


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
        if user_answer:
            return user_answer.score
        return None

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id' , 'text' , 'option1' , 'option2', 'option3' , 'option4']


class QuiestionAnswerSerializer(serializers.Serializer):
        answers = serializers.DictField(
        child=serializers.ChoiceField(choices=['option1', 'option2', 'option3', 'option4'])
    )
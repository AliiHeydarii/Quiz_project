from rest_framework.generics import ListAPIView , RetrieveAPIView
from .serializers import QuizSerializer,QuestionSerializer , QuiestionAnswerSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from quiz.models import Quiz , Question , UserAnswer
from rest_framework.views import APIView

class QuizListApiView(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    


class QuizDetailApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        quiz = Quiz.objects.get(pk=kwargs['pk'])
        questions = Question.objects.filter(quiz=quiz)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        quiz = Quiz.objects.get(pk=kwargs['pk'])
        user = request.user

        serializer = QuiestionAnswerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)

        answers = serializer.validated_data['answers']
        user_answer, created = UserAnswer.objects.get_or_create(user=user, quiz=quiz)

        if not created:
            return Response({"error": "You have already taken this quiz."})

        correct_answers = 0

        for question in quiz.questions.all():
            user_choice = answers.get(str(question.id))
            if user_choice and user_choice == getattr(question, "correct_answer"):
                correct_answers += 1


        user_answer.score = correct_answers
        user_answer.save()

        return Response({"message": "Quiz submitted successfully.", "score": user_answer.score})
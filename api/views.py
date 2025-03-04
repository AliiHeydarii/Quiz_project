from rest_framework.generics import ListAPIView , RetrieveAPIView
from .serializers import QuizSerializer,QuestionSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from quiz.models import Quiz , Question , User

class QuizListApiView(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    
class QuizDetailApiView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        quiz = self.get_object()
        question = Question.objects.filter(quiz=quiz)
        serializer = self.get_serializer(question,many=True)
        return Response(serializer.data)
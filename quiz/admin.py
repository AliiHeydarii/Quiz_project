from django.contrib import admin
from .models import Question,Quiz,UserAnswer


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Question)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(UserAnswer)
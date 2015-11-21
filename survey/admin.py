from django.contrib import admin

# Register your models here.
from .models import Response, Person, Survey, Question

class QuestionAdmin(admin.ModelAdmin):
	fields =['question_text', 'response']

admin.site.register(Question, QuestionAdmin)
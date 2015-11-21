from django.contrib import admin

# Register your models here.
from .models import Response, Person, Survey, Question

class SurveyAdmin(admin.ModelAdmin):
	fields =['person', 'question_text', 'response']

admin.site.register(Survey, SurveyAdmin)
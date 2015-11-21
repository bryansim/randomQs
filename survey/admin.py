from django.contrib import admin

# Register your models here.
from .models import Response, User

class ResponseAdmin(admin.ModelAdmin):
	fields =['user', 'question_text', 'user_response']

admin.site.register(Response, ResponseAdmin)
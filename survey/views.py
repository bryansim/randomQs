from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def home(request): #This function is what is returned when survey.views.home is called
	home_text = "Hello, this is the filler text for home.html"
	return render_to_response("survey/home.html", {'home_text': home_text})
	
def questions(request): #This function is what is returned when survey.views.questions is called
	question_list = [1,2,3,4,5]
	return render_to_response("survey/questions.html", {'question_list': question_list})
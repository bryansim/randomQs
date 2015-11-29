from django.http import HttpResponse
from django.shortcuts import render_to_response
from survey.models import Question

# Create your views here.
def home(request): #This function is what is returned when survey.views.home is called
    home_text = "What is your age?" #This eventually becomes Person.person_age
    return render_to_response("survey/home.html", {'home_text': home_text})
	
def questions(request): #This function is what is returned when survey.views.questions is called
    question_list = Question.objects.all()
    responses = range(1,8)
    return render_to_response("survey/questions.html", {'question_list': question_list, 'responses' : responses})
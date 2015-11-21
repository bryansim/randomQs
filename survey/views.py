from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def home(request): #This function is what is returned when survey.views.home is called
	return render_to_response("survey/home.html", {'hello': "Hello World!"})
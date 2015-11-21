from django.db import models

#rewritten based on http://dba.stackexchange.com/questions/120246/best-data-modeling-approch-to-handle-redundant-foreign-keys-in-relational-model

# Create your models here.
class Person(models.Model): #Creates a new class 'Person' that is a sub-class of the Model class in django.db.models.
	person_id = models.AutoField(primary_key=True) #This is the primary key of the person table (i.e., the unique ID of each person)
	person_age = models.IntegerField(default = 0) #Person also has the attribute 'age', because we want to store that.
	#user_location #We eventually want to get their location
	def __str__(self):
		return str(self.person_id)
		
class Survey(models.Model):
	survey_id = models.AutoField(primary_key=True) #This is the unique id of the survey (list of questions) that is answered by one person
	def __str__(self):
		return str(self.survey_id)
		
class PersonSurvey(models.Model):
	personsurvey_id = models.AutoField(primary_key=True) 
	person = models.ForeignKey(Person) #Multiple people register in personsurvey
	survey = models.ForeignKey(Survey) #Multiple surveys register in personsurvey
	
class Question(models.Model):
	question_id = models.AutoField(primary_key=True)
	question_text = models.CharField(max_length=200)
	def __str__(self):
		return self.question_text
		
class SurveyQuestion(models.Model): #This might be how we populate each survey with our questions
	surveyquestion_id = models.AutoField(primary_key=True)
	survey = models.ForeignKey(Survey)
	question = models.ForeignKey(Question)
	
class Response(models.Model): #Everyone's response is linked to who they are, what survey they did, as well as what the question in the survey was
	response_id = models.AutoField(primary_key=True)
	response = models.IntegerField(default = 0)
	personsurvey = models.ForeignKey(PersonSurvey)
	surveyquestion = models.ForeignKey(SurveyQuestion)
	
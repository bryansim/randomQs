from django.db import models

# Create your models here.
class User(models.Model): #Creates a new class 'Question' that is a sub-class of the Model class in django.db.models.
	user_id = models.AutoField(primary_key=True) #This is the primary key of the user table (i.e., the unique ID of each user`)
	user_age = models.IntegerField(default = 0) #User also has the attribute 'age', because we want to store that.
	#user_location #We eventually want to get their location
	
class Question(models.Model): #Creates a new class 'Question' that is sub-class of the Model class in django.db.models.
	user = models.ForeignKey(User) #This means that each user can have multiple questions related to them (i.e., each user answers multiple questions`)
	question_id = models.AutoField(primary_key=True) #This is the unique ID of the question)
	#This is the text of the question
	question_text = models.CharField(max_length=200) #Class 'Question' has an attribute question_text that is a sub-class of the class 'CharField' in django.db.models.

class Choice(models.Model): #Currently, each choice is uniquely linked to one question. Is this the best way to go?
	question = models.ForeignKey(Question) #Each question will have a bunch of choices linked to them.
	choice_text = models.CharField(max_length=200) #This is the text of the choice.
	votes = models.IntegerField(default = 0) #These are how many votes a choice has.
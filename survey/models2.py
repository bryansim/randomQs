from django.db import models

# Create your models here.
class User(models.Model): #Creates a new class 'Question' that is a sub-class of the Model class in django.db.models.
	user_id = models.AutoField(primary_key=True) #This is the primary key of the user table (i.e., the unique ID of each user`)
	user_age = models.IntegerField(default = 0) #User also has the attribute 'age', because we want to store that.
	#user_location #We eventually want to get their location
	def __str__(self):
		return str(self.user_id)

class Question(models.Model):
	question_id = models.AutoField(primary_key=True) #Unique id of question
	#This is the question text
	question_text = models.CharField(max_length=200) #Class 'Question' has an attribute question_text that is a sub-class of the class 'CharField' in django.db.models.
		
class Response(models.Model): #Creates a new class 'Question' that is sub-class of the Model class in django.db.models.
	question = models.ForeignKey(Question) #This means that each question can have multiple responses related to it (each question has multiple answers)
	response_id = models.AutoField(primary_key=True) #This is the unique ID of the response
	answer = models.IntegerField(default=0)
	def __str__(self):
		return self.answer
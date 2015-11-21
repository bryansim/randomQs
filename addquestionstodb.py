from survey.models import Question

def addquestions():
	Q1 = Question(question_text = "What is your favorite color?")
	Q2 = Question(question_text = "What is your favorite food?")
	Q3 = Question(question_text = "What is your favorite genre of music?")
	Q1.save()
	Q2.save()
	Q3.save()
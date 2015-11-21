# randomQs

This is a django project that will:

1. Display a list of questions prefaced by asking the user for some demographic information.
2. It will loop through the existing responses, and find the most similar user. It will do this by using some sort of deviation score.
3. It will return that user's demographic information (age, location)

###11.21.2015###
I made some changes to model.py, following this post:
http://dba.stackexchange.com/questions/120246/best-data-modeling-approch-to-handle-redundant-foreign-keys-in-relational-model

To the best of my understanding, Questions can be written ahead of time, whereas a Person class is created each time someone registers to take a survey. A survey class is then created and populated by questions (linked via SurveyQuestion), and are linked to persons via the class PersonSurvey.

I'm not sure I need a Person class if all I'm collecting is demographic data. I might be able to get away with just having Questions linked to Surveys, and each Survey represents a unique person.

###11.20.2015###
The urls.py file points index to survey.views.home at the moment.

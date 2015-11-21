Right now, there are two models: User and Response

The User class stores unique user_ids as well as, for now, user_age.
The Response class stores question_text, user_answer, and is linked via Foreign Key to User.

In other words, each User can have multiple Responses linked to him or her, with each response storing a question and the user's response.

This is probably not the best way to do it. There could be another table called Questions, let's say, that stores all the questions we want to ask, and is linked to each Response.

There is a templates folder that currently contains a base.html and home.html file. The base.html file will be an overall layout, and the home.html file will be nested within it.

The views.py file in this folder contains the function "home" that looks for survey/home.html, finds the key "hello", and returns "Hello world!". This is a placeholder and will be changed to our survey stuff.

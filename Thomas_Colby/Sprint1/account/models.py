# ACCOUNT MODELS
from django.db import models
from django.contrib.auth.models import AbstractUser

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    category = models.TextField(null=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class FomoUser(AbstractUser):
#     #username
#     #first_name
#     #last_name
#     #password
#     #last_login
    birthdate = models.DateField(null=True)
    gender = models.CharField(max_length=10)

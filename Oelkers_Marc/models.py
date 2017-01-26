#account models
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
    #username
    #first_name
    #last_name
    #email
    #is_staff(bool)
    #is_active (bool)
    #date_joined
    #password
    #last_login
    birthday = models.DateTimeField(null=True)
    gender = models.CharField(max_length=10)
# Define models here

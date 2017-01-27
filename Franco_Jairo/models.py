from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    category = models.TextField(null=True)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
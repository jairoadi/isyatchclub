import os
from datetime import datetime

#initialize the django environement
os.environ['DJANGO_SETTINGS_MODULE'] = 'fomo.settings'
import django
django.setup()

from account.models import Question, Choice

q1 = Question()#this allows me to create an object
q1.question_text = question_text ='Is it snowing today?'
q1.pub_date = datetime(2017,4,1,5,15)
q1.category = 'Day Stuff'
q1.save()

c1 = Choice()
c1.question = q1
c1.choice_text = 'Yes'
c1.save()

c2 = Choice()
c2.question = q1
c2.choice_text = 'No'
c2.save()

#q2 = Question.objects.get(id=5) #expects a single object
#questions = Question.object.filter(question_text = 'Is it snowing today?') #expects a list
#questions = Question.object.exclude(question_text = 'Is it snowing today?') # excludes whatever the user gives

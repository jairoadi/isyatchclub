import os
from datetime import datetime

#initialize django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'fomo.settings'
import django
django.setup()

from account.models import Question, Choice, FomoUser

#C#
# Question q1 = new Question()
#
# q1 = Question()
# q1.question_text = 'Is it snowing today?'
# q1.pub_date = datetime(2017, 4, 1, 5, 15)
# q1.category = 'Day Stuff'
# q1.save()
#
# c1 = Choice()
# c1.question = q1
# c1.choice_text = 'Yes'
# c1.save()
#
# c2 = Choice()
# c2.question = q1
# c2.choice_text = 'No'
# c2.save()

# q2 = Question.objects.get(id=2)
# print(q2.id, q2.question_text)
# for c in q2.choice_set.all():
#     print(c.choice_text)
#     print(c.question.question_text)

# questions = Question.objects.filter(id__gt=0)
# for q in questions:
#     print(q.id)

u1 = FomoUser()
u1.username = 'mkoelkers'
u1.first_name = 'Marc'
u1.last_name = 'Oelkers'
u1.password = 'Password1'
u1.last_login = datetime.now()
u1.birthday = datetime(1994, 12, 13)
u1.gender = 'Male'

u2 = FomoUser()
u2.username = 'shiblonsucks'
u2.first_name = 'Shiblo'
u2.last_name = 'Pahulu'
u2.password = 'Shiblonsucks'
u2.last_login = datetime.now()
u2.birthday = datetime(1987, 07, 02)
u2.gender = 'Male'

u3 = FomoUser()
u3.username = 'colbysucks'
u3.first_name = 'Colby'
u3.last_name = 'Thomas'
u3.password = 'Colbysucks'
u3.last_login = datetime.now()
u3.birthday = datetime(1994, 06, 16)
u3.gender = 'Male'

u4 = FomoUser()
u4.username = 'jairosucks'
u4.first_name = 'Jairo'
u4.last_name = 'Franco'
u4.password = 'Jairosucks'
u4.last_login = datetime.now()
u4.birthday = datetime(1992, 02, 05)
u4.gender = 'Male'

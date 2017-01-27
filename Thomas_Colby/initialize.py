from django.core import management
from django.db import connection
from datetime import datetime, date
import os, os.path, sys

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green

# ensure the user really wants to do this
areyousure = input(R + '''
  You are about to drop and recreate the entire database.
  All data are about to be deleted.  Use of this script
  may cause itching, vertigo, dizziness, tingling in
  extremities, loss of balance or coordination, slurred
  speech, temporary zoobie syndrome, longer lines at the
  testing center, changed passwords in Learning Suite, or
  uncertainty about whether to call your professor
  'Brother' or 'Doctor'.

  Please type 'yes' to confirm the data destruction: ''' + W)
if areyousure.lower() != 'yes':
    print()
    print('  Wise choice.')
    sys.exit(1)

# initialize the django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'fomo.settings'
import django
django.setup()


# drop and recreate the database tables
print()
print('Living on the edge!  Dropping the current database tables.')
with connection.cursor() as cursor:
    cursor.execute("DROP SCHEMA public CASCADE")
    cursor.execute("CREATE SCHEMA public")
    cursor.execute("GRANT ALL ON SCHEMA public TO postgres")
    cursor.execute("GRANT ALL ON SCHEMA public TO public")

# make the migrations and migrate
management.call_command('makemigrations')
management.call_command('migrate')


from account.models import FomoUser

    ## USERS ##

u1 = FomoUser()
u1.username = 'coloradocolby'
u1.first_name = 'Colby'
u1.last_name = 'Thomas'
u1.gender = 'Male'
u1.birthdate = date(1994, 6, 16)
u1.email = 'coloradocolby@gmail.com'
u1.password = 'iluvmichelle'
u1.is_staff = True
u1.is_active = True
u1.date_joined = datetime.now()
u1.last_login = datetime.now()
u1.save()

u2 = FomoUser()
u2.username = 'marcoelkers'
u2.first_name = 'Marc'
u2.last_name = 'Oelkers'
u2.gender = 'Male'
u2.birthdate = date(1994, 2, 13)
u2.email = 'marcoelkers@gmail.com'
u2.password = 'minvikings'
u2.is_staff = True
u2.is_active = True
u2.date_joined = datetime.now()
u2.last_login = datetime.now()
u2.save()

u3 = FomoUser()
u3.username = 'jairofranco'
u3.first_name = 'Jairo'
u3.last_name = 'Franco'
u3.gender = 'Male'
u3.birthdate = date(1991, 4, 12)
u3.email = 'jairoadi@gmail.com'
u3.password = 'portugal'
u3.is_staff = True
u3.is_active = True
u3.date_joined = datetime.now()
u3.last_login = datetime.now()
u3.save()

u4 = FomoUser()
u4.username = 'shiblonp'
u4.first_name = 'Shiblon'
u4.last_name = 'Pahulu'
u4.gender = 'Male'
u4.birthdate = date(1987, 11, 9)
u4.email = 'shiblonp@gmail.com'
u4.password = 'shibby'
u4.is_staff = True
u4.is_active = True
u4.date_joined = datetime.now()
u4.last_login = datetime.now()
u4.save()

u5 = FomoUser()
u5.username = 'michellethomas'
u5.first_name = 'Michelle'
u5.last_name = 'Thomas'
u5.gender = 'Female'
u5.birthdate = date(1993, 7, 2)
u5.email = 'michellethomas0814@gmail.com'
u5.password = 'iluvcolby'
u5.is_staff = True
u5.is_active = True
u5.date_joined = datetime.now()
u5.last_login = datetime.now()
u5.save()


    ## QUERIES

## query DB to get information about entered users
print(G + '\nQuery 1: Prints all users usernames\n' + W)
all_users = FomoUser.objects.all()
for u in all_users:
    print(u)

print(G + '\nQuery 2: Prints user with id = 1\n' + W)
user1 = FomoUser.objects.get(id=1)
print(user1.first_name)

print(G + '\nQuery 3: Prints all female users\n' + W)
female_users = FomoUser.objects.filter(gender="Female")
for cur_user in female_users:
    print(cur_user.first_name)

print(G + '\nQuery 4: Prints all users except those with first name Marc\n' + W)
not_marc = FomoUser.objects.exclude(first_name="Marc")
for cur_user in not_marc:
    print(cur_user.first_name)

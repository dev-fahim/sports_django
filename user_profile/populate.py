import os
import random
from datetime import datetime

from django import setup
from django.utils import timezone

from faker import Faker
from faker.providers import person, address, phone_number, company, barcode

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_django.settings')
setup()

try:
    from django.conf import settings

    from django.contrib.auth.models import User
    from user_profile.models import Profile, UserTypeChoice, GenderChoice
    from sports.models import Teacher, Student, Department, Event, EventTypeChoice
except ModuleNotFoundError:
    exit(1)

TOTAL_STUDENTS = 100
TOTAL_TEACHERS = 50
TOTAL_PLAYERS = 50
TOTAL_ADMINS = 5
TOTAL_DEPARTMENTS = 20
TOTAL_EVENTS = 100

fake = Faker()
fake.add_provider(person)
fake.add_provider(address)
fake.add_provider(phone_number)
fake.add_provider(company)
fake.add_provider(barcode)


def get_random_date(start_date: datetime, end_date: datetime):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    return start_date + timezone.timedelta(days=random_number_of_days)


def get_departments():
    departments = []

    departments_queryset = Department.objects.all()
    for i in departments_queryset:
        departments.append(i)

    return departments


def create_departments():
    for _ in range(TOTAL_DEPARTMENTS):
        department = Department.objects.create(name=fake.company())
        print('DEPARTMENT', department.name)


def create_student_users():
    for _ in range(TOTAL_STUDENTS):
        first_name = fake.first_name()
        last_name = fake.last_name()

        email = fake.email()

        password = '1234'

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        profile = Profile.objects.create(
            user_id=user.id,
            user_type=UserTypeChoice.STUDENT,
            address=fake.address(),
            gender=random.choice(list(GenderChoice)),
            phone_number=fake.phone_number()
        )
        Student.objects.create(
            profile_id=profile.id,
            student_id='ST' + fake.ean8(),
            student_reg='RG' + fake.ean13(),
            department_id=random.choice(get_departments()).id
        )
        print('STUDENTS', user, user.first_name, user.last_name)


def create_teacher_users():
    for _ in range(TOTAL_TEACHERS):
        first_name = fake.first_name()
        last_name = fake.last_name()

        email = fake.email()

        password = '1234'

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        profile = Profile.objects.create(
            user_id=user.id,
            user_type=UserTypeChoice.TEACHER,
            address=fake.address(),
            gender=random.choice(list(GenderChoice)),
            phone_number=fake.phone_number()
        )
        Teacher.objects.create(
            profile_id=profile.id,
            teacher_id='TC' + fake.ean8(),
            department_id=random.choice(get_departments()).id
        )
        print('TEACHER', user, user.first_name, user.last_name)


def create_admins():
    for _ in range(TOTAL_ADMINS):
        first_name = fake.first_name()
        last_name = fake.last_name()

        email = fake.email()

        password = '1234'

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=True,
            is_superuser=True
        )
        Profile.objects.create(
            user_id=user.id,
            user_type=UserTypeChoice.ADMIN,
            address=fake.address(),
            gender=random.choice(list(GenderChoice)),
            phone_number=fake.phone_number()
        )
        print('ADMIN', user, user.first_name, user.last_name)


def create_events():
    admins = []

    admins_query = Profile.objects.filter(user_type=UserTypeChoice.ADMIN)
    for i in admins_query:
        admins.append(i)

    for _ in range(TOTAL_EVENTS):
        event = Event.objects.create(
            by_profile=random.choice(admins),
            name=fake.company(),
            starts=get_random_date(timezone.now() + timezone.timedelta(days=1),
                                   timezone.now() + timezone.timedelta(days=10)),
            ends=get_random_date(timezone.now() + timezone.timedelta(days=15),
                                 timezone.now() + timezone.timedelta(days=20)),
            event_type=random.choice(list(EventTypeChoice))
        )
        print('EVENT', event.name, event.starts, event.ends, event.event_type)


if __name__ == '__main__':
    create_admins()
    create_departments()
    create_student_users()
    create_teacher_users()
    create_events()

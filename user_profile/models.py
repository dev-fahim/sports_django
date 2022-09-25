from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from utils.helpers import file_upload_directory


class UserTypeChoice(models.TextChoices):
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'
    ADMIN = 'ADMIN'
    PLAYER = 'PLAYER'


class GenderChoice(models.TextChoices):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHERS = 'OTHERS'


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=file_upload_directory, null=True, blank=True)

    gender = models.CharField(max_length=10, choices=GenderChoice.choices, default=GenderChoice.MALE)
    user_type = models.CharField(max_length=100, choices=UserTypeChoice.choices, default=UserTypeChoice.STUDENT)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def department(self):
        if self.user_type == UserTypeChoice.STUDENT:
            return self.student.department.name
        elif self.user_type == UserTypeChoice.TEACHER:
            return self.teacher.department.name

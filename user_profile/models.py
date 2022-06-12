from django.db import models

# Create your models here.


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

    gender = models.CharField(max_length=10, choices=GenderChoice.choices, default=GenderChoice.MALE)
    user_type = models.CharField(max_length=100, choices=UserTypeChoice.choices, default=UserTypeChoice.STUDENT)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

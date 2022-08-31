from django.db import models

# Create your models here.
from utils.helpers import file_upload_directory


class EventTypeChoice(models.TextChoices):
    OUTDOOR = 'OUTDOOR'
    INDOOR = 'INDOOR'


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    profile = models.OneToOneField('user_profile.Profile', on_delete=models.CASCADE)

    student_id = models.CharField(max_length=20)
    student_reg = models.CharField(max_length=20, null=True, blank=True)

    department = models.ForeignKey('sports.Department', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.profile)


class Teacher(models.Model):
    profile = models.OneToOneField('user_profile.Profile', on_delete=models.CASCADE)

    teacher_id = models.CharField(max_length=20)

    department = models.ForeignKey('sports.Department', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.profile)


class Player(models.Model):
    profile = models.OneToOneField('user_profile.Profile', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.profile)


class Event(models.Model):
    by_profile = models.ForeignKey('user_profile.Profile', on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=100)

    starts = models.DateTimeField()
    ends = models.DateTimeField()

    event_type = models.CharField(max_length=10, choices=EventTypeChoice.choices, default=EventTypeChoice.OUTDOOR)
    image = models.ImageField(upload_to=file_upload_directory, null=True, blank=True)

    def __str__(self):
        return self.name


class Manager(models.Model):
    profile = models.ForeignKey('user_profile.Profile', on_delete=models.CASCADE)
    event = models.ForeignKey('sports.Event', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.profile) + ' Event: ' + self.event.name


class Group(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey('sports.Event', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    group = models.ForeignKey('sports.Group', on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.group) + ' | ' + self.name


class TeamPlayer(models.Model):
    team = models.ForeignKey('sports.Team', on_delete=models.CASCADE, related_name='players')
    player = models.ForeignKey('sports.Player', on_delete=models.CASCADE)


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=file_upload_directory, null=True, blank=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    name = models.CharField(max_length=100)

    teams = models.ManyToManyField('sports.Team', blank=True)
    event = models.ForeignKey('sports.Event', on_delete=models.CASCADE)
    venue = models.ForeignKey('sports.Venue', on_delete=models.SET_NULL, null=True, blank=True)

    time = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Standing(models.Model):
    match = models.ForeignKey('sports.Match', on_delete=models.CASCADE)
    team = models.ForeignKey('sports.Team', on_delete=models.CASCADE)

    gained_points = models.FloatField(default=0)
    has_won = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True, null=True)

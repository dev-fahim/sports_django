from django.db import models

# Create your models here.


class EventTypeChoice(models.TextChoices):
    OUTDOOR = 'OUTDOOR'
    INDOOR = 'INDOOR'


class Department(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    profile = models.OneToOneField('user_profile.Profile', on_delete=models.CASCADE)

    student_id = models.CharField(max_length=20)
    student_reg = models.CharField(max_length=20, null=True, blank=True)

    department = models.ForeignKey('sports.Department', on_delete=models.SET_NULL, null=True, blank=True)


class Teacher(models.Model):
    profile = models.OneToOneField('user_profile.Profile', on_delete=models.CASCADE)

    teacher_id = models.CharField(max_length=20)

    department = models.ForeignKey('sports.Department', on_delete=models.SET_NULL, null=True, blank=True)


class Player(models.Model):
    profile = models.OneToOneField('user_profile.Profile', on_delete=models.CASCADE)


class Event(models.Model):
    by_profile = models.ForeignKey('user_profile.Profile', on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=100)

    starts = models.DateTimeField()
    ends = models.DateTimeField()

    event_type = models.CharField(max_length=10, choices=EventTypeChoice.choices, default=EventTypeChoice.OUTDOOR)


class Manager(models.Model):
    profile = models.ForeignKey('user_profile.Profile', on_delete=models.CASCADE)
    event = models.ForeignKey('sports.Event', on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=100)


class Team(models.Model):
    players = models.ManyToManyField('sports.Player', blank=True)
    group = models.ForeignKey('sports.Group', on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=100)


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)


class Match(models.Model):
    name = models.CharField(max_length=100)

    teams = models.ManyToManyField('sports.Team', blank=True)
    event = models.ForeignKey('sports.Event', on_delete=models.CASCADE)
    venue = models.ForeignKey('sports.Venue', on_delete=models.SET_NULL, null=True, blank=True)


class Standing(models.Model):
    match = models.ForeignKey('sports.Match', on_delete=models.CASCADE)
    team = models.ForeignKey('sports.Team', on_delete=models.CASCADE)

    gained_points = models.FloatField(default=0)
    has_won = models.BooleanField(default=False)

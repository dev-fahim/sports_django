# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Department, Student, Teacher, Player, Event, Manager, Group, Team, Venue, Match, Standing


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'profile',
        'student_id',
        'student_reg',
        'department',
    )
    list_filter = ('profile', 'department')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'teacher_id', 'department')
    list_filter = ('profile', 'department')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile')
    list_filter = ('profile',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'by_profile',
        'name',
        'starts',
        'ends',
        'event_type',
    )
    list_filter = ('by_profile', 'starts', 'ends')
    search_fields = ('name',)


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'event')
    list_filter = ('profile', 'event')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'name')
    list_filter = ('group',)
    raw_id_fields = ('players',)
    search_fields = ('name',)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name',)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'event', 'venue')
    list_filter = ('event', 'venue')
    raw_id_fields = ('teams',)
    search_fields = ('name',)


@admin.register(Standing)
class StandingAdmin(admin.ModelAdmin):
    list_display = ('id', 'match', 'team', 'gained_points', 'has_won')
    list_filter = ('match', 'team', 'has_won')

# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db.models import QuerySet

from .models import Department, Student, Teacher, Player, Event, Manager, Group, Team, Venue, Match, Standing, \
    TeamPlayer


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
    raw_id_fields = ['profile']


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
    exclude = ['by_profile']

    def save_model(self, request, obj: Event, form, change):
        if request.user.is_superuser:
            obj.by_profile_id = request.user.profile.id
        return super(EventAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset: QuerySet[Manager] = super(EventAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        profile = request.user.profile
        event_ids = list(profile.manager_set.values_list('event_id')[0])

        return queryset.filter(id__in=event_ids)


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'event')
    list_filter = ('profile', 'event')
    raw_id_fields = ('profile', 'event')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class PlayerInline(admin.TabularInline):
    extra = 0
    model = TeamPlayer
    raw_id_fields = ['player']
    max_num = 16


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'name')
    list_filter = ('group',)
    search_fields = ('name',)
    inlines = [PlayerInline]


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name',)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'event', 'venue')
    list_filter = ('event', 'venue')
    filter_horizontal = ('teams',)
    search_fields = ('name',)


@admin.register(Standing)
class StandingAdmin(admin.ModelAdmin):
    list_display = ('id', 'match', 'team', 'gained_points', 'has_won')
    list_filter = ('match', 'team', 'has_won')

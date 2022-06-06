# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'gender',
        'user_type',
        'phone_number',
        'address',
    )
    list_filter = ('user',)

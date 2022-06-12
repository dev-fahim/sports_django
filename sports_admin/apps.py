from django.contrib.admin.apps import AdminConfig


class SportsAdminConfig(AdminConfig):
    default_site = 'sports_admin.admin.SportsAdminSite'

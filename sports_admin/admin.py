from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _


class SportsAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = _('Sports Event Management System')

    # Text to put in each page's <h1> (and above login form).
    site_header = _('Sports Event Management System Admin')

    # Text to put at the top of the admin index page.
    index_title = _('Sports Event Management System Admin')


admin_site = SportsAdminSite(name="sports_admin")

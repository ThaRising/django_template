from django.contrib import admin
from drizm_django_commons.admin import SortableAdminMenuMixin


class SiteAdmin(SortableAdminMenuMixin, admin.AdminSite):
    site_header = "{{cookiecutter.project_name}} Administration"
    index_title = "{{cookiecutter.project_name}} Administration"
    site_title = "Administration"

    admin_app_ordering = {
        "auth": ("users", "auth"),
    }

from django.contrib.admin.apps import AdminConfig


class CustomAdmin(AdminConfig):
    default_site = "{{cookiecutter.project_name}}.admin.SiteAdmin"

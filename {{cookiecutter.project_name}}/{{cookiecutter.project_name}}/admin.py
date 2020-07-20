from django.contrib import admin


class SiteAdmin(admin.AdminSite):
    site_header = "{{cookiecutter.project_name}} Administration"
    index_title = "{{cookiecutter.project_name}} Administration"
    site_title = "Administration"

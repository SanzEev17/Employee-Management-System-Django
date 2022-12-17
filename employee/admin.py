from django.contrib import admin
from .models import Project, EmpLeave


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'project_name')
    list_display_links = ('id', 'employee', 'project_name')
    list_per_page = 20

admin.site.register(Project, ProjectAdmin)


class EmpLeaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'reason')
    list_display_links = ('id', 'employee', 'reason')
    list_per_page = 20

admin.site.register(EmpLeave, EmpLeaveAdmin)
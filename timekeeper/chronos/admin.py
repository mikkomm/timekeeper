from django.contrib import admin
from chronos.models import Project
from chronos.models import Task
from chronos.models import Reference

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Reference)

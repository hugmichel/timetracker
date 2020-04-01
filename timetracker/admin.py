from django.contrib import admin

# Register your models here.
from timetracker.models import TimeEntry, Project

admin.site.register(TimeEntry)
admin.site.register(Project)

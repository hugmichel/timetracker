from django.contrib import admin

# Register your models here.
from timetracker.models import TimeEntry, Project


class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'date', 'duration', 'comment')
    list_filter = ('user', 'project')


admin.site.register(TimeEntry, TimeEntryAdmin)
admin.site.register(Project)

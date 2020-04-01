from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=200, default="noname")

    def __str__(self):
        return self.name


class TimeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('work on date', default=timezone.now)
    duration = models.IntegerField('work duration in seconds', default=0)
    comment = models.TextField('optionnal comment', default="")

    def __str__(self):
        return "time entry [user=" + str(
            self.user.id) + "] [date=" + self.date.__str__() + "] [duration=" + str(self.duration) + "]"

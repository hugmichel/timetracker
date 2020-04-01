from django import forms
from django.contrib.auth.models import User

from timetracker.models import Project, TimeEntry


class TimeEntryForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    duration = forms.DurationField()
    date = forms.DateField(widget=forms.DateInput)
    comment = forms.CharField(widget=forms.Textarea, required=False)

    def save_timeentry(self):
        timeentry = TimeEntry()
        timeentry.project = self.cleaned_data['project']
        timeentry.user = self.cleaned_data['user']
        timeentry.duration = self.cleaned_data['duration'].seconds
        timeentry.date = self.cleaned_data['date']
        timeentry.comment = self.cleaned_data['comment']
        timeentry.save()
        pass

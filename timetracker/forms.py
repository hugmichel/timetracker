from django import forms
from django.contrib.auth.models import User

from timetracker.models import Project, TimeEntry


class TimeEntryForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    duration = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)

    def save_timeentry(self):
        timeentry = TimeEntry()
        timeentry.project = self.cleaned_data['project']
        timeentry.user = self.cleaned_data['user']
        hours, minutes = self.cleaned_data['duration'].split(':')
        timeentry.duration = int(hours) * 3600 + int(minutes) * 60
        timeentry.date = self.cleaned_data['date']
        timeentry.comment = self.cleaned_data['comment']
        timeentry.save()
        pass

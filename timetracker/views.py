import math

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import CreateView, FormView

from timetracker.forms import TimeEntryForm
from timetracker.models import TimeEntry, Project


class IndexView(generic.ListView):
    template_name = 'timetracker/index.html'
    context_object_name = 'timeentrys'

    def get_queryset(self):
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user

        time_entrys = TimeEntry.objects.filter(user=user)

        project_id = self.request.GET.get('project_id')
        if project_id and len(project_id) > 0:
            project_id = int(project_id)
            time_entrys = time_entrys.filter(project_id=project_id)

        date_min = self.request.GET.get('date_min')
        if date_min and len(date_min) > 0:
            # date_min = (date_min)
            time_entrys = time_entrys.filter(date__gte=date_min)

        date_max = self.request.GET.get('date_max')
        if date_max and len(date_max) > 0:
            # date_max = (date_max)
            time_entrys = time_entrys.filter(date__lte=date_max)

        total = 0
        for time_entry in time_entrys:
            total += time_entry.duration

        self.extra_context = {"total": total,
                              "project_id": project_id,
                              "date_min": date_min,
                              "date_max": date_max,
                              "projects": Project.objects.all()}
        return time_entrys.order_by('-id')


class TimeEntryCreateView(FormView):
    template_name = 'timetracker/timeentry_form.html'
    form_class = TimeEntryForm
    success_url = '/'

    def get_initial(self):
        initial = super(TimeEntryCreateView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'user': self.request.user})
            user_entries = TimeEntry.objects.filter(user=self.request.user).order_by('-id')
            if len(user_entries) > 0:
                initial.update({'project': user_entries[0].project})
        initial.update({"date": timezone.now})
        return initial

    def form_valid(self, form):
        form.save_timeentry()
        return super().form_valid(form)


class TimeEntryUpdateView(FormView):
    template_name = 'timetracker/timeentry_form.html'
    form_class = TimeEntryForm
    success_url = '/'

    @property
    def time_entry_id(self):
        return self.kwargs['time_entry_id']

    def get_initial(self):
        time_entry = get_object_or_404(TimeEntry, pk=self.time_entry_id)
        initial = super(TimeEntryUpdateView, self).get_initial()
        hour = math.floor(time_entry.duration / 3600)
        minutes = math.floor((time_entry.duration - (hour * 3600)) / 60)
        initial.update({
            "project": time_entry.project,
            "user": time_entry.user,
            "date": time_entry.date,
            "duration": str(hour) + ':' + str(minutes),
            "comment": time_entry.comment,
        })
        return initial

    def form_valid(self, form):
        form.save_timeentry(self.time_entry_id)
        return super().form_valid(form)


def remove_time_entry(request, time_entry_id):
    # TODO : check user permissions
    time_entry = get_object_or_404(TimeEntry, pk=time_entry_id)
    time_entry.delete()
    return HttpResponseRedirect(reverse('index'))

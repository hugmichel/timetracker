from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import CreateView, FormView

from timetracker.forms import TimeEntryForm
from timetracker.models import TimeEntry


class IndexView(generic.ListView):
    template_name = 'timetracker/index.html'
    context_object_name = 'timeentrys'

    def get_queryset(self):
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user
        return TimeEntry.objects.filter(user=user).order_by('-id')


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


def remove_time_entry(request, time_entry_id):
    time_entry = get_object_or_404(TimeEntry, pk=time_entry_id)  # , user=request.user
    time_entry.delete()
    return HttpResponseRedirect(reverse('index'))

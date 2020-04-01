from django.views import generic
from django.views.generic import CreateView, FormView

from timetracker.forms import TimeEntryForm
from timetracker.models import TimeEntry


class IndexView(generic.ListView):
    template_name = 'timetracker/index.html'
    context_object_name = 'timeentrys'

    def get_queryset(self):
        return TimeEntry.objects.filter(user=2)


class TimeEntryCreateView(FormView):
    template_name = 'timetracker/timeentry_form.html'
    form_class = TimeEntryForm
    success_url = '/'

    def form_valid(self, form):
        form.save_timeentry()
        return super().form_valid(form)

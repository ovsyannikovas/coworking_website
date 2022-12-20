from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import EventRequestForm
from account.models import *
from event.models import *
from event.utils import is_enrolled


@login_required
def personal_account(request):
    events = EventList.objects.filter(user=request.user)
    events_number = events.count()
    events_per_row = 2
    rows_number = events_number // events_per_row + (events_number % events_per_row)
    context = {
        'events': events,
    }
    return render(request, 'account/MemberPersAcc_t.html', context=context)


@login_required
def organizer_account(request):
    events = EventOrgRequest.objects.filter(user=request.user)
    context = {'events': events, }
    return render(request, 'account/OrgPersAcc_t.html', context=context)


class CreateEventRequest(LoginRequiredMixin, CreateView):
    model = EventOrgRequest
    form_class = EventRequestForm
    template_name = 'account/regevent_t.html'
    success_url = reverse_lazy('organizer_account')

    def get_initial(self):
        initial = super(CreateEventRequest, self).get_initial()
        initial.update({'user': self.request.user})

        return initial

    def form_valid(self, form):
        """Force the user to request.user"""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super(CreateEventRequest, self).form_valid(form)


@login_required
def create_event_request(request):
    context = {}
    if request.method == 'POST':
        form = EventOrgRequest(request.POST)
        # send_message(request.user.email, form.cleaned_data['message'])
    form = EventOrgRequest()
    context['form'] = form
    return render(request, 'account/regevent_t.html', context=context)


@login_required
def sign_down(request):
    event_id = request.GET.get('event')
    event = get_object_or_404(Event, id=event_id)
    event_record = get_object_or_404(EventList, event=event, user=request.user)
    event_record.delete()
    return redirect('personal_account')

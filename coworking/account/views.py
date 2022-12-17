from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

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
        'rows_range': range(1, rows_number),
    }
    return render(request, 'account/MemberPersAcc_t.html', context=context)


@login_required
def organizer_account(request):
    return HttpResponse('Страница личного кабинета организатора')


@login_required
def sign_down(request):
    event_id = request.GET.get('event')
    event = get_object_or_404(Event, id=event_id)
    event_record = get_object_or_404(EventList, event=event, user=request.user)
    event_record.delete()
    return redirect('personal_account')

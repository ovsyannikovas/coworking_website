from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from event.models import *


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

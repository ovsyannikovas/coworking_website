from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from event.models import *
from account.models import *
from .forms import CoworkingForm

@login_required
def personal_account(request):
    events = EventList.objects.filter(user=request.user)
    events_number = events.count()
    events_per_row = 2
    cow_inacc = Coworking.objects.exclude(user=request.user)
    cow_booked = Coworking.objects.filter(user=request.user)
    cow_signs_number = cow_booked.count()
    cow_signs_per_row = 2
    if (events_number / events_per_row) % 1 != 0:
        rows_number = events_number // events_per_row + 1
    else:
        rows_number = events_number // events_per_row

    if (cow_signs_number / cow_signs_per_row) % 1 != 0:
        cow_rows_number = cow_signs_number // cow_signs_per_row + 1
    else:
        cow_rows_number = cow_signs_number // cow_signs_per_row

    context = {
        'events': events,
        'events_per_row': events_per_row,
        'rows_range': range(1, rows_number),
        'on_row_range': range(1, events_per_row + 1),

    }
    return render(request, 'account/MemberPersAcc_t.html', context=context)


# @login_required
def organizer_account(request):
    return HttpResponse('Страница личного кабинета организатора')

def coworking(request):
    cows = Coworking.objects.all()
    #form = CoworkingForm(user=request.user)
    form = CoworkingForm()
    if form.is_valid():
        form.save(request)
    context = {
        'cows': cows,
        'form': form,
    }
    return render(request, 'account/regcowork_t.html', context=context)

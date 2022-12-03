from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from event.models import EventList


@login_required
def personal_account(request):
    events = EventList.objects.filter(user=request.user)
    events_number = events.count()
    events_per_slide = 4
    if (events_number / events_per_slide) % 1 != 0:
        slides_number = events_number // events_per_slide + 1
    else:
        slides_number = events_number // events_per_slide
    context = {
        'events': events,
        'events_per_slide': events_per_slide,
        'inactive_slides_range': range(1, slides_number),
        'on_slide_range': range(1, events_per_slide + 1)
    }
    return render(request, 'account/MemberPersAcc_t.html', context=context)


# @login_required
def orginizer_account(request):
    return HttpResponse('Страница личного кабинета организатора')

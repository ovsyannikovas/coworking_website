from django.urls import path

from account.views import *

urlpatterns = [
    path('personal/', personal_account, name='personal_account'),
    path('organizer/', organizer_account, name='organizer_account'),
    path('coworking/', CreateCoworkingRequest.as_view(), name='coworking'),
    path('coworking/signdown/', sign_down_coworking, name='signdown_coworking'),
    path('event/signdown/', sign_down, name='signdown'),
    path('organizer/event_request', CreateEventRequest.as_view(), name='event_request')
]

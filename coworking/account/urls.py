from django.urls import path

from account.views import *

urlpatterns = [
    path('personal/', personal_account, name='personal_account'),
    path('organizer/', organizer_account, name='organizer_account'),
    path('coworking/', coworking, name='coworking')
]

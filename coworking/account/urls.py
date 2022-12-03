from django.urls import path

from account.views import *

urlpatterns = [
    path('personal/', personal_account, name='personal_account'),
    path('orginizer/', orginizer_account, name='orginizer_account'),
]
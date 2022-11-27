from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# @login_required
def personal_account(request):
    return HttpResponse('Страница личного кабинета')


# @login_required
def orginizer_account(request):
    return HttpResponse('Страница личного кабинета организатора')

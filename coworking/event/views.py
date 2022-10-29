from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu = [
    {'title': 'Организаторам', 'url_name': '...'},
    {'title': 'Контакты', 'url_name': 'contacts'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Войти', 'url_name': 'login'},
]


def home_page(request):
    events = Event.objects.all()
    context = {
        'events': events,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'event/MainPage_t.html', context=context)


def about_page(request):
    return render(request, 'event/AboutUs_t.html')


def contacts_page(request):
    return render(request, 'event/Contacts_t.html')


def help_page(request):
    return HttpResponse('Обратная связь')


def events(request, cat_slug):
    return HttpResponse(f'Категория: {cat_slug}')


def events_page(request):
    events = Event.objects.all()
    context = {
        'events': events,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'event/Events_t.html', context=context)


def login_page(request):
    return render(request, 'event/auth_t.html')


def page_not_found(request, exception):
    return HttpResponseNotFound

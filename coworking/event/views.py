from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import LoginUserForm
from .models import *
from .utils import DataMixin

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


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'event/auth_t.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('successful_auth')
        # return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def page_not_found(request, exception):
    return HttpResponseNotFound


def successful_auth(request):
    return render(request, 'event/successful_auth_t.html')

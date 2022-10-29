from django.urls import path

from event.views import home_page, about_page, contacts_page, help_page, events_page, login_page

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contacts/', contacts_page, name='contacts'),  # страница контакты
    path('help/', help_page, name='help'),  # страница обращения в поддержку

    path('events/', events_page, name='events'), # все мероприятия
    # path('events/<slug:cat_slug>', events, name='category'),  # категория мероприятия пока функция-заглушка
    # path('event/<slug:event_slug>/', , name='event') # конкретное событие

    # path('register/', RegisterUser.as_view(), name='register'),
    # path('login/', LoginUser.as_view(), name='login'),
    path('login/', login_page, name='login'),
    # path('logout/', logout_user, name='logout'),
]

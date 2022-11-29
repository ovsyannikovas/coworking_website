from django.urls import path

from event.views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contacts/', contacts_page, name='contacts'),  # страница контакты
    path('help/', help_page, name='help'),  # страница обращения в поддержку

    path('events/', events_page, name='events'), # все мероприятия
    # path('events/<slug:cat_slug>', events, name='category'),  # категория мероприятия пока функция-заглушка
    # path('event/<slug:event_slug>/', , name='event') # конкретное событие
    path('event/<int:event_id>/signup/', sign_up, name='signup'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('login/successful_auth/', successful_auth, name='successful_auth')
]

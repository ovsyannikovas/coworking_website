from .models import *
from django.db.models import Count

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 20

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('event'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


def is_enrolled(request, event_id):
    if request.user.is_authenticated:
        records = EventList.objects.filter(user=request.user, event=event_id)
        return len(records) == 1
    return False


def send_message(email, message):
    print(f'* на почту сайта с {email} отправлено сообщение: {message} *')

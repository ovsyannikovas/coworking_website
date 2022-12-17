from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

from event.models import *


class Coworking(models.Model):
    date_time = models.DateTimeField(verbose_name="Время начала забронированного интервала")
    username = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                 verbose_name="Забронировавший интервал пользователь")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время записи")

    # time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения параметров записи")

    def __str__(self):
        return self.date_time


class EventOrgRequest(models.Model):
    CHOICES = (
        (0, 'Лекция'),
        (1, 'Мастер-класс'),
        (2, 'Хакатон'),
    )

    title = models.CharField(max_length=255, verbose_name="Название мероприятия")
    content = models.TextField(blank=True, verbose_name="Описание мероприятия")
    # отредактировать путь для фото?
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    date_time = models.DateTimeField(verbose_name="Время проведения мероприятия")
    organizer = models.CharField(max_length=255, verbose_name="Организатор")
    # organizer = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name="Организатор")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.CharField(choices=CHOICES, verbose_name="Категории", max_length=10)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Организатор")

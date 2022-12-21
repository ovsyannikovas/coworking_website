import uuid

from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

from event.models import *


class Coworking(models.Model):
    date_time = models.DateTimeField(unique=True, verbose_name="Время начала забронированного интервала", )
    #date = models.DateField(verbose_name="Дата, на которую бронируется коворкинг",)
    #time = models.TimeField(verbose_name="Время, на которое бронируется коворкинг",)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Бронирующий")
    #time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время записи")
    #time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения параметров записи")
    unique_num = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Интервал'
        verbose_name_plural = 'Интервалы'
        ordering = ['id']
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
    date_time = models.DateTimeField(verbose_name="Время проведения мероприятия", blank=True, null=True)
    organizer = models.CharField(max_length=255, verbose_name="Организатор")
    # organizer = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name="Организатор")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=False, verbose_name="Рассмотрено")
    category = models.IntegerField(choices=CHOICES, verbose_name="Категории", default=0)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Организатор", null=True)


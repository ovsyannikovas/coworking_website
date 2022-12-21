import uuid

from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Coworking(models.Model):
    date_time = models.DateTimeField(unique=True, verbose_name="Время начала забронированного интервала", )
    #date = models.DateField(verbose_name="Дата, на которую бронируется коворкинг",)
    #time = models.TimeField(verbose_name="Время, на которое бронируется коворкинг",)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Бронирующий")
    #time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время записи")
    # time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения параметров записи")
    unique_num = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Интервал'
        verbose_name_plural = 'Интервалы'
        ordering = ['id']

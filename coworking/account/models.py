from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Coworking(models.Model):
    date_time = models.DateTimeField(verbose_name="Время начала забронированного интервала")
    username = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                 verbose_name="Забронировавший интервал пользователь")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время записи")
    # time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения параметров записи")

    def __str__(self):
        return self.date_time

import uuid

from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название мероприятия")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Описание мероприятия")
    # отредактировать путь для фото?
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    date_time = models.DateTimeField(verbose_name="Время проведения мероприятия")
    organizer = models.CharField(max_length=255, verbose_name="Организатор")
    # organizer = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name="Организатор")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', kwargs={'event_slug': self.slug})

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


def get_unique_num():
    return 0


class EventList(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Участник")
    event = models.ForeignKey(Event, on_delete=models.PROTECT, verbose_name="Мероприятие")
    unique_num = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=False)

    class Meta:
        verbose_name = 'Запись на мероприятие'
        verbose_name_plural = 'Записи на мероприятия'
        ordering = ['id']


class EventRequestList(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Участник")
    event = models.ForeignKey(Event, on_delete=models.PROTECT, verbose_name="Мероприятие")
    unique_num = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=False)
    status = models.BooleanField(default=False, verbose_name="Статус")

    class Meta:
        verbose_name = 'Запись на мероприятие'
        verbose_name_plural = 'Записи на мероприятия'
        ordering = ['id']

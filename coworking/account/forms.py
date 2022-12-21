from django import forms
from .models import Coworking
from django.core.exceptions import ValidationError
from datetime import datetime, date, time
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from account.models import EventOrgRequest


class CoworkingForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d.%m.%Y'], widget=forms.DateTimeInput(format='%d.%m.%Y',
                                                                                  attrs={'type': "datetext",
                                                                                         'class': "forms-control",
                                                                                         'id': "inputdate"}))
    TIME_CHOICES = [
        ('11:00', '11:00 - 14:00'),
        ('14:00', '14:00 - 17:00'),
        ('17:00', '17:00 - 19:00'),
    ]
    time = forms.TimeField(widget=forms.RadioSelect(choices=TIME_CHOICES,
                                                    attrs={'class': "radio-input2", 'type': "radio",
                                                           'name': "coworktime"}))

    # def __init__(self, *args, **kwargs):
    #   self.user = kwargs.pop('user', None)
    #  super(CoworkingForm, self).__init__(*args, **kwargs)

    # def save(self, user):
    #     date_time = datetime.datetime(self.cleaned_data['date'].year, self.cleaned_data['date'].month,
    #                                   self.cleaned_data['date'].day, self.cleaned_data['time'].hour,
    #                                   self.cleaned_data['time'].minute, 0)
    #     new_book = Coworking.objects.create(date_time=date_time, user=user)
    #     return new_book

    class Meta:
        model = Coworking
        fields = ('date', 'time')


class EventRequestForm(forms.ModelForm):
    CHOICES = (
        (0, 'Лекция'),
        (1, 'Мастер-класс'),
        (2, 'Хакатон'),
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"type": "text", "class": "forms-control", "id": "inputtext"}
        )
    )
    organizer = forms.CharField(
        widget=forms.TextInput(
            attrs={"type": "text", "class": "forms-control", "id": "inputtext"}
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'name': "text", 'cols': '40', 'rows': '100'}
        )
    )
    category = forms.IntegerField(
        widget=forms.RadioSelect(
            choices=CHOICES, attrs={"name": "eventtype", "class": "radio-input2", "type": "radio"}
        )
    )
    date_time = forms.DateTimeField(input_formats=['%d.%m.%Y'],
                                    widget=forms.DateTimeInput(
                                        format='%d.%m.%Y'
                                    )
                                    )

    class Meta:
        model = EventOrgRequest
        fields = ('title', 'content', 'category', 'organizer', 'date_time')

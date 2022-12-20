from django import forms
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from account.models import EventOrgRequest


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

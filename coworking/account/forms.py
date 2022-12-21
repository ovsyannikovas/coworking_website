from django import forms
from .models import Coworking
from django.core.exceptions import ValidationError
from datetime import datetime, date, time



class CoworkingForm(forms.ModelForm):
    date = forms.DateField()
    TIME_CHOICES = ['11:00', '14:00', '17:00']
    time = forms.TimeField(widget=forms.RadioSelect(choices=TIME_CHOICES))

    #def __init__(self, *args, **kwargs):
     #   self.user = kwargs.pop('user', None)
      #  super(CoworkingForm, self).__init__(*args, **kwargs)

    def save(self, user):
        date_time = datetime.datetime(self.cleaned_data['date'].year, self.cleaned_data['date'].month,
                                      self.cleaned_data['date'].day, self.cleaned_data['time'].hour,
                                      self.cleaned_data['time'].minute, 0)
        new_book = Coworking.objects.create(date_time=date_time, user=user)
        return new_book

    class Meta:
        model = Coworking
        fields = ('date_time', 'user')


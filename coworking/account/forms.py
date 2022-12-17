from django import forms

from account.models import EventOrgRequest


class EventRequestForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'name': "text", 'cols': '40', 'rows': '100'}
        )
    )

    class Meta:
        model = EventOrgRequest
        fields = ('title', 'content', 'user', 'cat', 'date_time')

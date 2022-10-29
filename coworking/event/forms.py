from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'type': "login", 'class': "forms-control", 'id': "inputlogin"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'type': "password", 'class': "forms-control", 'id': "inputpassword"}))

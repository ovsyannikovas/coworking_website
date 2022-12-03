from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'type': "login", 'class': "forms-control", 'id': "inputlogin"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'type': "password", 'class': "forms-control", 'id': "inputpassword"}))


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'type': "name", 'class': "forms-control", 'id': "inputname"}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'type': "surname", 'class': "forms-control", 'id': "inputsurname"}))
    username = forms.CharField(label='Никнейм', widget=forms.TextInput(
        attrs={'type': "name", 'class': "forms-control", 'id': "username"}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={'type': 'email', 'class': 'forms-control', 'id': "inputemail"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'type': 'password', 'class': 'forms-control', 'id': "inputpassword"}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'type': 'password', 'class': 'forms-control', 'id': "inputpassword"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class ContactForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'name': "text", 'cols': '40', 'rows': '100'}
        )
    )

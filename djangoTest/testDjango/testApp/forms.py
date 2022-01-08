from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.db import models

from .models import Task, Example, UserProfile, Message, Room
from django.forms import ModelForm, TextInput, Textarea, ModelChoiceField, ChoiceField, PasswordInput
from django.core.exceptions import ValidationError
from django.utils import timezone as tz


def validate_date_not_in_future(value):
    if value > tz.now():
        raise ValidationError('date is in the future')


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "name"]
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите оценку'}),
                   }


class ExampleForm(ModelForm):
    class Meta:
        model = Example
        fields = ["Name"]
        widgets = {
            "Name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["birth_date", "genre", "address", "age", "email", "image", "vk", "tg", "data", "first_name", "last_name"]
        widgets = {
            "address": TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'Введите адресс'}),
            "first_name": TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'Имя'}),
            "last_name": TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'Фамилия'}),
            "age": TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'Введите возраст'}),
            "email": TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'Введите email'}),
            "vk": TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'https://vk.com/user'}),
            "tg": TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'https://t.me/usertest'}),
        }


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter old password'}))
    new_password1 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter new password'}))
    new_password2 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirm new password'}))

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]


class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields = ["name"]


class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ["value", "user", "room"]
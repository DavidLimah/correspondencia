from django import forms
from django.contrib.auth.models import User

from django.forms import ModelChoiceField
from django.db import models

from accounts.models import Profile

from django.urls import path
from .views import home, bandeja, enviado, observado



class ProfileForm(forms.ModelForm):
    funcioario = forms.ModelChoiceField(queryset=User.objects.filter(group__name='Funcionarios'), label='Funcionario')

    class Meta:
        model = Profile
        fields = ['user','oficina','cargo']


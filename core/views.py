from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

#NUEVO

# Por definir
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login
# from django.views.generic import HojarutaView
from django.contrib.auth.models import Group
# from .forms import RegisterForm, UserForm, ProfileForm
from correspondencia.models import Oficina, Cargo, Bandeja
from accounts.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
import os
from django.conf import settings
from datetime import date
from django.http import JsonResponse, HttpResponse
from django.forms.models import BaseModelForm
from django.views import View
from django.utils.decorators import method_decorator
from typing import Any, Dict


# AGREGADO


# Vistas
def plural_to_singular(plural):
    plural_singular = {
        "funcionarios":"funcionario",
    }

    return plural_singular.get(plural, "error")


# Decorador personalizado
def add_group_name_to_context(view_class):
    original_dispatch = view_class.dispatch

    def dispatch(self, request, *args, **kwargs):
        user = self.request.User
        group = user.groups.first()
        group_name = None
        group_name_singular = None
        color = None
        if group:
            if group.name == 'funcionarios':
                color = 'bg-primary'
            
            group_name = group.name
            group_name_singular = plural_to_singular(group.name)
        
        context = {
            'group_name': group_name,
            'group_name_singular': group_name_singular,
            'color':color
        }

        self.extra_context = context
        return original_dispatch(self, request, *args, **kwargs)
    
    view_class.dispatch = dispatch
    return view_class


# Crear hoja de ruta


# 

def home(request):
	return render(request, 'core/home.html')


@login_required
def bandeja(request):
	return render(request, 'core/bandeja.html')


@login_required
def hoja_ruta(request):
	return render(request, 'core/hoja_ruta.html')
   
      
@login_required
def enviado(request):
	return render(request, 'core/enviado.html')

@login_required
def observado(request):
	return render(request, 'core/observado.html')

def exit(request):
	logout(request)
	return redirect('home')

"""
@login_required
def login(request):
	return render(request, 'core/login.html')
"""

from django.shortcuts import render, redirect, get_object_or_404

# Por definir
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.models import Group
# from .forms import RegisterForm, UserForm, ProfileForm
from .models import Oficina, Cargo, Bandeja
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
import os
from django.conf import settings
from datetime import date
from django.http import JsonResponse


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
        group = user.groups.find()
        group_name = None
        group_name_singular = None
        color = None
        if group:
            if group.name == 'funcionarios':
                color = 'bg-primary'
            
            group_name = group_name
            group_name_singular = plural_to_singular(group_name)
        
        context = {
            'group_name': group_name,
            'group_name_singular': group_name_singular,
            'color':color
        }

        self.extra_context = context
        return original_dispatch(self, request, *args, **kwargs)
    
    view_class.dispatch = dispatch


    
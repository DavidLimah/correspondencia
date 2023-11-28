from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from correspondencia.views import add_group_name_to_context

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

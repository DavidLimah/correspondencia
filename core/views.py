from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.contrib.auth.models import User
from correspondencia.models import Oficina, Cargo, Correspondencia, Enviado
from accounts.models import Profile
from correspondencia.forms import CorrespondenciaForm, ArchivarForm

from django.contrib import messages
from django.http import HttpResponseRedirect

from django.views.generic import ListView

from django.views.generic.edit import FormView

from django import db

#from django.contrib.messages.views import SuccessMessageMixin

# PÁGINAS

def home(request):
	return render(request, 'core/home.html')


@login_required
def recibido(request):
    obj_recibido = Correspondencia.objects.all()
    context_recibido = {
        'obj_recibido':obj_recibido,
    }
    return render(request, 'core/recibido.html', context_recibido)


@login_required
def archivar(request, id):
	instance = get_list_or_404(Correspondencia, id=id)
	archivar_form = ArchivarForm(request.POST, instance=instance)
	correspondencia = archivar_form.save(commit=False)
	if request.method == 'POST':
		if 'button_archivar' in request.POST:
			if archivar_form.is_valid():
				
				correspondencia.save()
	return render(request, 'core/archivar.html', context={'archivar_form':archivar_form,})


@login_required
def archivado(request):
    obj_archivado = Correspondencia.objects.all()
    context_archivado = {
        'obj_archivado':obj_archivado,
    }
    return render(request, 'core/archivado.html', context_archivado)


@login_required
def hoja_ruta(request):    
	if request.method == "POST":
		form = CorrespondenciaForm(request.POST)
		if form.is_valid():
			form.save()
            # messages.add_message(request, CRITITAL, "Mensaje")
		return HttpResponseRedirect("/enviado/")
	else:
		form = CorrespondenciaForm()
	context_hoja_ruta = {'form':form}
	return render(request, 'core/hoja_ruta.html', context_hoja_ruta)


@login_required
def enviado(request):
    obj_enviado = Correspondencia.objects.all()
    context_enviado = {
        'obj_enviado':obj_enviado,
    }
    return render(request, 'core/enviado.html', context_enviado)

@login_required
def devuelto(request):
    obj_devuelto = Correspondencia.objects.all()
    context_devuelto = {
        'obj_devuelto':obj_devuelto,
    }
    return render(request, 'core/devuelto.html',context_devuelto)

@login_required
def cancelado(request):
	obj_cancelado = Correspondencia.objects.all()
	context_cancelado = {
		'obj_cancelado':obj_cancelado,
    }
	return render(request, 'core/cancelado.html', context_cancelado)

def exit(request):
	logout(request)
	return redirect('home')

"""
@login_required
def login(request):
	return render(request, 'core/login.html')
"""

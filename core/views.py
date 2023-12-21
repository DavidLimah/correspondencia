from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.contrib.auth.models import User
from correspondencia.models import Oficina, Cargo, Correspondencia, Enviado
from accounts.models import Profile
from correspondencia.forms import CorrespondenciaForm, ArchivarForm, DevolverForm, CancelarForm

from django.contrib import messages
from django.http import HttpResponseRedirect

from django.views.generic import ListView

from django.views.generic.edit import FormView

from django import db

#from django.contrib.messages.views import SuccessMessageMixin


# HOME
def home(request):
	return render(request, 'core/home.html')


# HOJA DE RUTA
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


# RECIBIDO
@login_required
def recibido(request):
    obj_recibido = Correspondencia.objects.all()
    context_recibido = {
        'obj_recibido':obj_recibido,
    }
    return render(request, 'core/recibido.html', context_recibido)


# ENVIADO
@login_required
def enviado(request):
    obj_enviado = Correspondencia.objects.all()
    context_enviado = {
        'obj_enviado':obj_enviado,
    }
    return render(request, 'core/enviado.html', context_enviado)


# ARCHIVADO
@login_required
def archivado(request):
    obj_archivado = Correspondencia.objects.all()
    context_archivado = {
        'obj_archivado':obj_archivado,
    }
    return render(request, 'core/archivado.html', context_archivado)


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


# ACCIONES

# ARCHIVAR
@login_required
def archivar(request, id):
	asunto_archivar = Correspondencia.objects.get(id=id)
	asunto_archivar.archivado = True
	if request.method == 'POST':
		form_archivar = ArchivarForm(request.POST, instance=asunto_archivar)
		if form_archivar.is_valid():
			form_archivar.save()
			return HttpResponseRedirect('/archivado/')
	else:
		form_archivar = ArchivarForm(instance=asunto_archivar)
	context_archivar = {'form_archivar':form_archivar,}
	return render(request, 'core/archivar.html', context_archivar)


# DEVOLVER
@login_required
def devolver(request, id):
	asunto_devolver = Correspondencia.objects.get(id=id)
	asunto_devolver.devuelto = True
	if request.method == 'POST':
		form_devolver = DevolverForm(request.POST, instance=asunto_devolver)
		if form_devolver.is_valid():
			form_devolver.save()
			return HttpResponseRedirect('/devuelto/')
	else:
		form_devolver = DevolverForm(instance=asunto_devolver)
	context_devolver = {'form_devolver':form_devolver,}
	return render(request, 'core/devolver.html', context_devolver)


# CANCELAR
@login_required
def cancelar(request, id):
	asunto_cancelar = Correspondencia.objects.get(id=id)
	asunto_cancelar.cancelado = True
	if request.method == 'POST':
		form_cancelar = CancelarForm(request.POST, instance=asunto_cancelar)
		if form_cancelar.is_valid():
			form_cancelar.save()
			return HttpResponseRedirect('/cancelado/')
	else:
		form_cancelar = CancelarForm(instance=asunto_cancelar)
	context_cancelar = {'form_cancelar':form_cancelar,}
	return render(request, 'core/cancelar.html', context_cancelar)
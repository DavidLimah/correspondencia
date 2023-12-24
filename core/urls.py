"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include

from django.urls import path
from .views import home, derivar, recibido, enviado, devuelto,  archivado, cancelado, archivar, devolver, cancelar, exit

urlpatterns = [
    path('', home, name='home'),
    path('recibido/', recibido, name='recibido'),
    path('enviado/', enviado, name='enviado'),
    path('archivado/', archivado, name='archivado'),
    path('devuelto/', devuelto, name='devuelto'),
    path('cancelado/', cancelado, name='cancelado'),
    path('derivar/', derivar, name='derivar'),
    path('archivar/<int:id>/change', archivar, name='archivar'),
    path('devolver/<int:id>/change', devolver, name='devolver'),
    path('cancelar/<int:id>/change', cancelar, name='cancelar'),
    path('logout/', exit, name='exit'),
]

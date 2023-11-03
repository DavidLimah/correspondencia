from django.shortcuts import render

# Renderizar vistas
from django.views.generic import TemplateView


# Página de inicio
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class HojaRutaPageView(TemplateView):
    template_name = 'hoja_ruta.html'
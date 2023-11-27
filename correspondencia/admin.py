from django.contrib import admin
from correspondencia.models import Oficina, Cargo, Bandeja

import autocomplete_all as admin

from django.contrib.postgres.search import TrigramSimilarity

# Register your models here.
@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
	search_fields = ('nombre_oficina',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
	search_fields = ('nombre_cargo',)

@admin.register(Bandeja)
class Bandeja(admin.ModelAdmin):
	search_fields = ('usuario_remitente',)
	


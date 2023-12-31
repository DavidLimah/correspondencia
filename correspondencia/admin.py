from django.contrib import admin
from correspondencia.models import Correspondencia, Unidad, Cargo


import autocomplete_all as admin

from django.contrib.postgres.search import TrigramSimilarity


@admin.register(Correspondencia)
class Correspondencia(admin.ModelAdmin):
	search_fields = ('codigo',)


@admin.register(Unidad)
class Unidad(admin.ModelAdmin):
	search_fields = ('nombre_unidad','sigla_unidad',)

@admin.register(Cargo)
class Cargo(admin.ModelAdmin):
	search_fields = ('nombre_cargo',)













"""
@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
	search_fields = ('nombre_oficina',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
	search_fields = ('nombre_cargo',)
"""


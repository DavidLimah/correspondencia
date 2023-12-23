from django.contrib import admin
from correspondencia.models import Correspondencia, Unidad, ConsejoMunicipal, DespachoAlcalde, SecretariaGeneral, SecAdmFinanciera, SecretariaTecnica, SecretariaPlanificacion, SecFortalecimientoInSocial, DirAsesoriaLegal, DireccionFinanzas, DirAuditoriaInterna, DirDesarrolloHumano, DireccionIngresos, DirDesProdMedAmbiente, DirUrbanismoCatastro, DirObrasPublicas, DireccionPlanificacion, DirSaneamientoBasico, DirAdministracionSalud, DirEduGestionSocial, AsesoresU


import autocomplete_all as admin

from django.contrib.postgres.search import TrigramSimilarity


@admin.register(Correspondencia)
class Correspondencia(admin.ModelAdmin):
	search_fields = ('codigo',)


@admin.register(Unidad)
class Unidad(admin.ModelAdmin):
	search_fields = ('nombre_unidad',)













"""
@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
	search_fields = ('nombre_oficina',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
	search_fields = ('nombre_cargo',)
"""


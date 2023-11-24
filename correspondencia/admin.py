from django.contrib import admin
from correspondencia.models import Oficina, Cargo, Bandeja

import autocomplete_all as admin

# Register your models here.
@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
	search_fields = ('nombre_oficina',)
	

# admin.site.register(Oficina)
admin.site.register(Cargo)
admin.site.register(Bandeja)
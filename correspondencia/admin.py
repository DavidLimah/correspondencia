from django.contrib import admin
from .models import Oficina, Cargo, TipoDocumento

# Register your models here.

admin.site.register(Oficina)
admin.site.register(Cargo)
admin.site.register(TipoDocumento)
from django.contrib import admin
from .models import Profile


# Oficina, Cargo, 
# Register your models here.
# admin.site.register(Oficina)
# admin.site.register(Cargo)

# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	search_fields = ('user',)
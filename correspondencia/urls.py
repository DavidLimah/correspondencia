from django.urls import path
from . import views

urlpatterns = [
	path('',views.correspondencia, name='correspondencias')
]
from django.urls import path
from .views import HomePageView, AboutPageView, HojaRutaPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('hoja_ruta/', HojaRutaPageView.as_view(), name='hoja_ruta'),
    path('', HomePageView.as_view(), name='home'),
]
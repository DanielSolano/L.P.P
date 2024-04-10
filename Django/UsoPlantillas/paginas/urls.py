from django.urls import path
from .views import VistaPaginaDeInicio, VistaPaginaDeAcercaDe

urlpatterns = [
    path('', VistaPaginaDeInicio.as_view(), name='pagina_inicio'),
    path('acerca_de/', VistaPaginaDeAcercaDe.as_view(), name='acerca_de'),
]
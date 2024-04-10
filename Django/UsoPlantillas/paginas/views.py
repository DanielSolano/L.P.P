from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class VistaPaginaDeInicio(TemplateView):
    template_name = 'pagina_inicio.html'
    
class VistaPaginaDeAcercaDe(TemplateView):
    template_name = 'acerca_de.html'
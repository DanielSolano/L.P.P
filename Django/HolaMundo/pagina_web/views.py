from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vistaPaginaDeInicio(solicitud):
    return HttpResponse('<h1>Hola Mundo</h1>')
from django.http import HttpResponse
from django.shortcuts import render

#importamos el modelo Persona de la app personas
from personas.models import Persona


# Create your views here.

def bienvenido(request):
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all() #retorna los objetos de tipo modelo
    personas = Persona.objects.order_by('id')#para que sea descendente al inicio de id va - -> '-id'
    return render(request, 'bienvenido.html', {'no_personas':no_personas, 'personas':personas})


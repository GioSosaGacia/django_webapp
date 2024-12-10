from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')

def despedida(request):
    return HttpResponse('Despedida desde Django!!')


def contacto(request):
    return HttpResponse('Mi nombre es Giovanni, mis datos son: Telefono: 3326036684, Correo:giovanni-sosa-12@outlook.com')
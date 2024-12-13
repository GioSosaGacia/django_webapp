from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404
from personas.models import Persona


# Create your views here.
def detallePersona(request,id):
    #persona = Persona.objects.get(pk=id) #marca error y te envia a una pagina donde muestra el error de manera poco agradable
    persona = get_object_or_404(Persona, pk=id) #de esta manera nos arroja 404 si no existe el registro
    return render(request, 'personas/detalle.html', {'persona':persona})


#clase generada a partir del objeto modelform_factory, tambien debemos indicar si vamos a excluir algunos de los campos del modelo
PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})
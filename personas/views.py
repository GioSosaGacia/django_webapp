from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from personas.forms import PersonaForm
from personas.models import Persona


# Create your views here.
def detallePersona(request,id):
    #persona = Persona.objects.get(pk=id) #marca error y te envia a una pagina donde muestra el error de manera poco agradable
    persona = get_object_or_404(Persona, pk=id) #de esta manera nos arroja 404 si no existe el registro
    return render(request, 'personas/detalle.html', {'persona':persona})


#1.Forma de crear un formulario
#clase generada a partir del objeto modelform_factory, tambien debemos indicar si vamos a excluir algunos de los campos del modelo
#PersonaForm = modelform_factory(Persona, exclude=[])


#2.Segunda forma creando un archivo forms.py para crear el formulario e importamos el formulario creado de forms.py a views
def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})


def editarPersona(request,id):
    persona = get_object_or_404(Persona, pk=id)  # de esta manera nos arroja 404 si no existe el registro
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)

    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})
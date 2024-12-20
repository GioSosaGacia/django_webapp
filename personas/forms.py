from django.forms import ModelForm, EmailInput, TextInput

from personas.models import Persona, Domicilio


#Este formulario nos sirve para personalizar mas el formulario, como el el typy EmailInput
class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'no_calle': TextInput(attrs={'type':'number'})
        }
from django.forms import ModelForm, EmailInput

from personas.models import Persona


#Este formulario nos sirve para personalizar mas el formulario, como el el typy EmailInput
class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }
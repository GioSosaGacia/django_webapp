from django.db import models

# Create your models here.
class Persona(models.Model):
    # nombre de la variable, extiende de model.tipo de dato y la longitud de caracteres que almacenara
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

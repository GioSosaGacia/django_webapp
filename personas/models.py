from django.db import models

# Create your models here.
#Primero van declarasdas las clases que no tienen relacion con otra clase o clases:

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)
    
    def __str__(self):
        return f' Domiciolio {self.id}: {self.calle} {self.no_calle} {self.pais}'

class Persona(models.Model):
    # nombre de la variable, extiende de model.tipo de dato y la longitud de caracteres que almacenara
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    #1.de esta manera relacionamos un campo de una tabla con otra, mediante el uso de FK
    #2.Tambien debemos de especificar que se hará cuando se elimine un registro de la tabla ya que estan relacionadas, usando on_delete
    #3.Debemos de especifical que el campo admitira null para que no borre los datos de ambas tablas relacionadas
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)
    #Nota on_delete=CASCADE elimina el registro de ambas tablas relacionadas por el Id o coluna en comun 
    
    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'

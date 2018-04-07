import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Estudiates(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
            return self.nombre

    

class Certificados(models.Model):
    descripcion =  models.CharField(max_length=200)
    valor = models.IntegerField(default=0)

    def __str__(self):
        return self.descripcion


class Solicitudes(models.Model):
    estudiante = models.ForeignKey(Estudiates, on_delete=models.CASCADE)
    certificados = models.ForeignKey(Certificados, on_delete=models.CASCADE)
    fecha = models.DateTimeField('date published')

    def __str__(self):
        return self.estudiante.nombre +" " +self.certificados.descripcion
    


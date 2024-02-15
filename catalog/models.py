from django.db import models

class Servicio(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100)
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"Servicio #{self.numero}: {self.area}"

class DatosCMPCChile(models.Model):
    numero = models.IntegerField()
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"Datos CMPC Chile #{self.numero}: {self.dependencia}"

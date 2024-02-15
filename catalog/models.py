# models.py
from django.db import models
from django.contrib.auth.models import User

class Contrato(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona el contrato con un usuario
    fecha_inicio = models.DateField()
    fecha_vencimiento = models.DateField()
    # Otros campos necesarios

    def __str__(self):
        return f"Contrato ({self.fecha_inicio} - {self.fecha_vencimiento})"

class Asistencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)  # Relación con el contrato
    fecha = models.DateField()
    presente = models.BooleanField()
    # Otros campos necesarios

    def __str__(self):
        return f"Asistencia ({self.fecha}, Presente: {self.presente})"
    
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
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
    campo3 = models.DateField()

    def __str__(self):
        return self.campo1

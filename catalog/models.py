from django.db import models

class Contrato(models.Model):
    fecha_inicio = models.DateField()
    fecha_vencimiento = models.DateField()
    # Otros campos necesarios

    def __str__(self):
        return f"Contrato ({self.fecha_inicio} - {self.fecha_vencimiento})"

class Asistencia(models.Model):
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

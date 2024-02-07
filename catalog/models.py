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

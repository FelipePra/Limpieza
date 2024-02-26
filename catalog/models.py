from django.db import models


class DatosCMPCChile(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return self.numero
    class Meta:
        db_table = 'datoschile'
    
class RegistroExcel(models.Model):
    numero= models.IntegerField()
    area= models.CharField(max_length=100)
    depdencia= models.CharField(max_length=100)
    detalle= models.TextField()
    frecuencia= models.CharField(max_length=100)
    procedimiento= models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"Registro Excel #{self.numero}: {self.area}"



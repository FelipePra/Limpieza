from django.db import models
#Models CMPC
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
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'datoschile'

class DatosCMPCArgentina(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'datosargentina'

class DatosCMPCMexico(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'datosmexico'

class DatosCMPCBrasil(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'datosbrasil'


#Models Box Board
class Maule(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table ='maule'

class Valdivia(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'valdivia'

#Models Corrugados
class Chimolsa(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'chimolsa'

class Cordillera(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=1000, default='')
    dependencia = models.CharField(max_length=1000)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=1000)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=1000)
    horario = models.CharField(max_length=1000)
    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'cordillera'

class Buin(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'buin'

class Osorno(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'osorno'

class TilTil(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'tiltil'

class Pudahuel(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'pudahuel'

class PuenteAlto(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'puentealto'

class RedOficinas(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table = 'redoficinas'

class SanJoaquin(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f"Número: {self.numero}, Área: {self.area}, Dependencia: {self.dependencia}"
    class Meta:
        db_table ='sanjoaquin'

#Models Edipac
class OfiConcepcion(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'oficoncepcion'

class OfiTemuco(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'ofitemuco'

class Quilicura(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'quilicura'
       
#Models Sack Kraft
class CamposNovos(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'camposnovos'
class Chillan(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=1000, default='')
    dependencia = models.CharField(max_length=1000)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=1000)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=1000)
    horario = models.CharField(max_length=1000)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'chillan'
class Fabi(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'fabi'
class Guadalajara(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'guadalajara' 
class Irapuato(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'irapuato'
class Peru(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'peru'
class PiraidoSul(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'piraidosul'
class SanJose(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table ='sanjose'
        
#Models Bosques
        
class Balnearios(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'balnearios'

class VillaForest(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'villaforest'

class BosquesPlata(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'bosquesplata'

class EdiCorpo(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'edicorpo'

class Transito(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'transito'

class Coyhaique(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'coyhaique'

class Vivero(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'vivero'

#Models Maderas
        
class Bucalemu(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f''
    class Meta:
        db_table = 'bucalemu'

class Mulchen(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table ='mulchen'

class Nacimiento(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'nacimiento'

class Niuform(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'niuform'

class Plywood(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'plywood'

class Coronel(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'coronel'
    
class RemLA(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table ='remla'


#Models Pulp

class BalnearioLaja(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'balneariolaja'

class CasaHuespedes(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'casahuespedes'

class Guaiba(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f""
    class Meta:
        db_table = 'guaiba'

class Laja(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'laja'

class Pacifico(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table = 'pacifico'

class SantaFe(models.Model):
    numero = models.IntegerField()
    area = models.CharField(max_length=100, default='')
    dependencia = models.CharField(max_length=100)
    detalle = models.TextField()
    frecuencia = models.CharField(max_length=100)
    procedimientos = models.TextField()
    parametro_control = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    def __str__(self):
        return f""
    class Meta:
        db_table ='santafe'


    
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

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Puedes agregar campos adicionales según tus necesidades
    age = models.PositiveIntegerField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    
    # Especifica related_name único para las relaciones Many-to-Many
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Por ejemplo, aquí cambiamos el related_name
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # También cambiamos el related_name aquí
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.username

class Nota(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contenido
    class Meta:
        db_table ='Notas'
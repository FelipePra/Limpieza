from django import forms
from .models import *
#Forms CMPC
class DatosCMPCChileForm(forms.ModelForm):
    class Meta:
        model = DatosCMPCChile
        fields = '__all__'

class DatosCMPCArgentinaForm(forms.ModelForm):
    class Meta:
        model = DatosCMPCArgentina
        fields = '__all__'

class DatosCMPCBrasilForm(forms.ModelForm):
    class Meta:
        model = DatosCMPCBrasil
        fields = '__all__'

class DatosCMPCMexicoForm(forms.ModelForm):
    class Meta:
        model = DatosCMPCMexico
        fields = '__all__'

#Forms Box Board
class MauleForm(forms.ModelForm):
    class Meta:
        model = Maule
        fields = '__all__'

class ValdiviaForm(forms.ModelForm):
    class Meta:
        model = Valdivia
        fields = '__all__'

#Forms Corrugados
class ChimolsaForm(forms.ModelForm):
    class Meta:
        model = Chimolsa
        fields = '__all__'

class CordilleraForm(forms.ModelForm):
    class Meta:
        model = Cordillera
        fields = '__all__'

class BuinForm(forms.ModelForm):
    class Meta:
        model = Buin
        fields = '__all__'

class OsornoForm(forms.ModelForm):
    class Meta:
        model = Osorno
        fields = '__all__'

class TilTilForm(forms.ModelForm):
    class Meta:
        model = TilTil
        fields = '__all__'

class PudahuelForm(forms.ModelForm):
    class Meta:
        model = Pudahuel
        fields = '__all__'

class PuenteAltoForm(forms.ModelForm):
    class Meta:
        model = PuenteAlto
        fields = '__all__'

class RedOficinasForm(forms.ModelForm):
    class Meta:
        model = RedOficinas
        fields = '__all__'

class SanJoaquinForm(forms.ModelForm):
    class Meta:
        model = SanJoaquin
        fields = '__all__'

#Forms Edipac
class OfiConcepcionForm(forms.ModelForm):
    class Meta:
        model = OfiConcepcion
        fields = '__all__'

class OfiTemucoForm(forms.ModelForm):
    class Meta:
        model = OfiTemuco
        fields = '__all__'

class QuilicuraForm(forms.ModelForm):
    class Meta:
        model = Quilicura
        fields = '__all__'

#Forms Sack Kraft
class CamposNovosForm(forms.ModelForm):
    class Meta:
        model = CamposNovos
        fields = '__all__'

class ChillanForm(forms.ModelForm):
    class Meta:
        model = Chillan
        fields = '__all__'

class FabiForm(forms.ModelForm):
    class Meta:
        model = Fabi
        fields = '__all__'

class GuadalajaraForm(forms.ModelForm):
    class Meta:
        model = Guadalajara
        fields = '__all__'

class IrapuatoForm(forms.ModelForm):
    class Meta:
        model = Irapuato
        fields = '__all__'

class PeruForm(forms.ModelForm):
    class Meta:
        model = Peru
        fields = '__all__'

class PiraidoSulForm(forms.ModelForm):
    class Meta:
        model = PiraidoSul
        fields = '__all__'

class SanJoseForm(forms.ModelForm):
    class Meta:
        model = SanJose
        fields = '__all__'

#Forms Bosqes
class BalneariosForm(forms.ModelForm):
    class Meta:
        model = Balnearios
        fields = '__all__'

class VillaForestForm(forms.ModelForm):
    class Meta:
        model = VillaForest
        fields = '__all__'

class BosquesPlataForm(forms.ModelForm):
    class Meta:
        model = BosquesPlata
        fields = '__all__'

class EdiCorpoForm(forms.ModelForm):
    class Meta:
        model = EdiCorpo
        fields = '__all__'

class TransitoForm(forms.ModelForm):
    class Meta:
        model = Transito
        fields = '__all__'

class CoyhaiqueForm(forms.ModelForm):
    class Meta:
        model = Coyhaique
        fields = '__all__'

class ViveroForm(forms.ModelForm):
    class Meta:
        model = Vivero
        fields = '__all__'

#Forms Maderas
class BucalemuForm(forms.ModelForm):
    class Meta:
        model = Bucalemu
        fields = '__all__'

class MulchenForm(forms.ModelForm):
    class Meta:
        model = Mulchen
        fields = '__all__'

class NacimientoForm(forms.ModelForm):
    class Meta:
        model = Nacimiento
        fields = '__all__'

class NiuformForm(forms.ModelForm):
    class Meta:
        model = Niuform
        fields = '__all__'

class PlywoodForm(forms.ModelForm):
    class Meta:
        model = Plywood
        fields = '__all__'

class CoronelForm(forms.ModelForm):
    class Meta:
        model = Coronel
        fields = '__all__'

class RemLAForm(forms.ModelForm):
    class Meta:
        model = RemLA
        fields = '__all__'

#Forms Pulp
class BalnearioLajaForm(forms.ModelForm):
    class Meta:
        model = BalnearioLaja
        fields = '__all__'

class CasaHuespedesForm(forms.ModelForm):
    class Meta:
        model = CasaHuespedes
        fields = '__all__'

class GuaibaForm(forms.ModelForm):
    class Meta:
        model = Guaiba
        fields = '__all__'

class LajaForm(forms.ModelForm):
    class Meta:
        model = Laja
        fields = '__all__'

class PacificoForm(forms.ModelForm):
    class Meta:
        model = Pacifico
        fields = '__all__'

class SantaFeForm(forms.ModelForm):
    class Meta:
        model = SantaFe
        fields = '__all__'

class RegristoExcelForm(forms.ModelForm):
    class Meta:
        model = RegistroExcel
        fields = '__all__'

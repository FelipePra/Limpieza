# forms.py
from django import forms
from .models import Contrato, DatosCMPCChile, Asistencia

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['usuario', 'fecha_inicio', 'fecha_vencimiento']

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['usuario', 'contrato', 'fecha', 'presente']


class DatosCMPCChileForm(forms.ModelForm):
    class Meta:
        model = DatosCMPCChile
        fields = '__all__' 

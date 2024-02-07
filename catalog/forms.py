from django import forms
from .models import Contrato, RegistroAsistencia

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['usuario', 'fecha_inicio', 'fecha_vencimiento']

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = RegistroAsistencia
        fields = ['usuario', 'contrato', 'fecha', 'presente']

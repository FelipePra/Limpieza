from django import forms
from .models import DatosCMPCChile, RegistroExcel

class DatosCMPCChileForm(forms.ModelForm):
    class Meta:
        model = DatosCMPCChile
        fields = '__all__'

class RegristoExcelForm(forms.ModelForm):
    class Meta:
        model = RegistroExcel
        fields = '__all__'

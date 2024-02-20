from django import forms
from .models import DatosCMPCChile

class DatosCMPCChileForm(forms.ModelForm):
    class Meta:
        
        model = DatosCMPCChile
        fields = '__all__'

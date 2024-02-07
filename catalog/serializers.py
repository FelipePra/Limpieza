from rest_framework import serializers
from .models import Contrato, Asistencia

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'  # Puedes cambiar '__all__' por una lista de los campos que deseas serializar

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'  # Puedes cambiar '__all__' por una lista de los campos que deseas serializar

from django.shortcuts import render
from rest_framework import generics
from .models import Contrato, Asistencia
from .serializers import ContratoSerializer, AsistenciaSerializer

class ContratoListCreate(generics.ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class ContratoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class AsistenciaListCreate(generics.ListCreateAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

class AsistenciaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

def index(request):
    return render(request, 'index.html')

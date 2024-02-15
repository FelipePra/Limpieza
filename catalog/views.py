from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from catalog.forms import DatosCMPCChileForm
from .models import  Servicio, DatosCMPCChile
from .serializers import ServicioSerializer

# Vistas para renderizar las plantillas HTML

def index_view(request):
    return render(request, 'index.html')

def servicios_list_view(request):
    servicios = Servicio.objects.all()
    return render(request, 'Servicios/servicios_list.html', {'asistencias': servicios})


# Vistas de Instalaciones
def instalaciones(request):
    return render(request, 'Instalaciones/instalaciones.html')

def bosques(request):
    return render(request, 'Bosques/Bosques.html', {})



# Vistas CMPC
def CMPC_Chile(request):
    datos_cmpc_chile = DatosCMPCChile.objects.all()
    return render(request, 'Instalaciones/CMPC/CMPC_Chile.html', {'datos_cmpc_chile': datos_cmpc_chile})




def ejemplo_api(request):
    return render(request, 'ejemplo.html')

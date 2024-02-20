from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response

from catalog.forms import DatosCMPCChileForm
from .models import  Servicio, DatosCMPCChile
from .serializers import ServicioSerializer

# Vistas para renderizar las plantillas HTML

def index(request):
    return render(request, 'index.html')

def servicios_list_view(request):
    servicios = Servicio.objects.all()
    return render(request, 'Servicios/servicios_list.html', {'asistencias': servicios})


# Vistas de Instalaciones
def instalaciones(request):
    return render(request, 'Instalaciones/instalaciones.html')

def bosques(request):
    return render(request, 'Instalaciones/Bosques.html', {})

def pulp(request):
    return render(request, 'Instalaciones/Pulp.html', {})

def biopackaging(request):
    return render(request, 'Instalaciones/Biopackaging.html', {})

def maderas(request):
    return render(request, 'Instalaciones/Maderas.html', {})



#Vistas Biopackaging
def boxboard(request):
    return render(request, 'Instalaciones/Biopackaging/Boxboard.html', {})

def corrugados(request):
    return render(request, 'Instalaciones/Biopackaging/Corrugados.html', {})

def edipac(request):
    return render(request, 'Instalaciones/Biopackaging/Edipac.html', {})

def sackkraft(request):
    return render(request, 'Instalaciones/Biopackaging/SackKraft.html', {})


# Vistas CMPC
def cmpc_chile(request):
    datos_cmpc_chile = DatosCMPCChile.objects.all()
    return render(request, 'Instalaciones/CMPC/CMPC_Chile.html', {'datos_cmpc_chile': datos_cmpc_chile})

def cmpc_argentina(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/CMPC/CMPC_Argentina.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/CMPC/CMPC_Argentina.html', {'excel_uploaded': False})
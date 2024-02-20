from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response

from catalog.forms import DatosCMPCChileForm
from .models import  DatosCMPCChile


# Vistas para renderizar las plantillas HTML

def index(request):
    return render(request, 'index.html')


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

def cmpc_brasil(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/CMPC/CMPC_Brasil.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/CMPC/CMPC_Brasil.html', {'excel_uploaded': False})

def cmpc_mexico(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/CMPC/CMPC_Mexico.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/CMPC/CMPC_Mexico.html', {'excel_uploaded': False})

#Biopackaging Box-Board

def maule(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/Biopackaging/Box-Board/Maule.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/Biopackaging/Box-Board/Maule.html', {'excel_uploaded': False})

def valdivia(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/Biopackaging/Box-Board/Valdivia.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/Biopackaging/Box-Board/Valdivia.html', {'excel_uploaded': False})

#Biopackaging Corrugados

def chimolsa(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/Biopackaging/Corrugados/Chimolsa.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/Biopackaging/Corrugados/Chimolsa.html', {'excel_uploaded': False})

def cordillera(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/Biopackaging/Corrugados/Cordillera.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/Biopackaging/Corrugados/Cordillera.html', {'excel_uploaded': False})

def buin(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIIBuin.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIIBuin.html', {'excel_uploaded': False})

def osorno(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIIOsorno.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIIOsorno.html', {'excel_uploaded': False})

def tiltil(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIITilTil.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIITilTil.html', {'excel_uploaded': False})

def sorepapudahuel(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaPudahuel.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaPudahuel.html', {'excel_uploaded': False})

def sorepapuentealto(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaPuenteAlto.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaPuenteAlto.html', {'excel_uploaded': False})

def sorepaofi(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaRedOficinas.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaRedOficinas.html', {'excel_uploaded': False})

def sorepasanjoaquin(request):
    if request.method == 'POST':
        excel_uploaded = False
        # Verificar si se ha enviado un archivo
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            # Aquí podrías realizar el procesamiento del archivo Excel si es necesario
            # Por ejemplo, guardar el archivo en el servidor, analizar su contenido, etc.
            excel_uploaded = True
        return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaSanJoaquin.html', {'excel_uploaded': excel_uploaded})
    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaSanJoaquin.html', {'excel_uploaded': False})
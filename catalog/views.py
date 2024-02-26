from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib import messages

from catalog.forms import *
from .models import  DatosCMPCChile
from django.contrib import messages as django_messages

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
    if request.method == 'POST':
        form = DatosCMPCChileForm(request.POST, request.FILES)
        if form.is_valid():
            datoschile = form.save(commit=False)
            datoschile.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('cmpc_chile')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = DatosCMPCChileForm()

    return render(request, 'Instalaciones/CMPC/CMPC_Chile.html', {'form': form})


def cmpc_argentina(request):
    if request.method == 'POST':
        form = DatosCMPCArgentinaForm(request.POST, request.FILES)
        if form.is_valid():
            datosargentina = form.save(commit=False)
            datosargentina.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('cmpc_argentina')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = DatosCMPCArgentinaForm()

    return render(request, 'Instalaciones/CMPC/CMPC_Argentina.html', {'form':form})

def cmpc_brasil(request):
    if request.method == 'POST':
            form = DatosCMPCBrasilForm(request.POST, request.FILES)
            if form.is_valid():
                datosbrasil = form.save(commit=False)
                datosbrasil.save()
                messages.success(request, 'Datos ingresados correctamente')
                return redirect('cmpc_argentina')
            else:
                messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
            form = DatosCMPCBrasilForm()
    return render(request, 'Instalaciones/CMPC/CMPC_Brasil.html', {'form': form})

def cmpc_mexico(request):
    if request.method == 'POST':
            form = DatosCMPCMexicoForm(request.POST, request.FILES)
            if form.is_valid():
                datosbrasil = form.save(commit=False)
                datosbrasil.save()
                messages.success(request, 'Datos ingresados correctamente')
                return redirect('cmpc_argentina')
            else:
                messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
            form = DatosCMPCMexicoForm()
    return render(request, 'Instalaciones/CMPC/CMPC_Mexico.html', {'form': form})

def maule(request):
    if request.method == 'POST':
        form = MauleForm(request.POST, request.FILES)
        if form.is_valid():
            datos_maule = form.save(commit=False)
            datos_maule.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('maule')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = MauleForm()

    return render(request, 'Instalaciones/Biopackaging/Box-Board/Maule.html', {'form': form})

def valdivia(request):
    if request.method == 'POST':
        form = ValdiviaForm(request.POST, request.FILES)
        if form.is_valid():
            datos_valdivia = form.save(commit=False)
            datos_valdivia.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('valdivia')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = ValdiviaForm()

    return render(request, 'Instalaciones/Biopackaging/Box-Board/Valdivia.html', {'form': form})

# Biopackaging Corrugados

def chimolsa(request):
    if request.method == 'POST':
        form = ChimolsaForm(request.POST, request.FILES)
        if form.is_valid():
            datos_chimolsa = form.save(commit=False)
            datos_chimolsa.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('chimolsa')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = ChimolsaForm()

    return render(request, 'Instalaciones/Biopackaging/Corrugados/Chimolsa.html', {'form': form})

def cordillera(request):
    if request.method == 'POST':
        form = CordilleraForm(request.POST, request.FILES)
        if form.is_valid():
            datos_cordillera = form.save(commit=False)
            datos_cordillera.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('cordillera')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = CordilleraForm()

    return render(request, 'Instalaciones/Biopackaging/Corrugados/Cordillera.html', {'form': form})

def buin(request):
    if request.method == 'POST':
        form = BuinForm(request.POST, request.FILES)
        if form.is_valid():
            datos_buin = form.save(commit=False)
            datos_buin.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('buin')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = BuinForm()

    return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIIBuin.html', {'form': form})

def osorno(request):
    if request.method == 'POST':
        form = OsornoForm(request.POST, request.FILES)
        if form.is_valid():
            datos_osorno = form.save(commit=False)
            datos_osorno.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('osorno')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = OsornoForm()

    return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIIOsorno.html', {'form': form})

def tiltil(request):
    if request.method == 'POST':
        form = TilTilForm(request.POST, request.FILES)
        if form.is_valid():
            datos_tiltil = form.save(commit=False)
            datos_tiltil.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('tiltil')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = TilTilForm()

    return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIITilTil.html', {'form': form})

def sorepapudahuel(request):
    if request.method == 'POST':
        form = PudahuelForm(request.POST, request.FILES)
        if form.is_valid():
            datos_sorepa_pudahuel = form.save(commit=False)
            datos_sorepa_pudahuel.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('sorepapudahuel')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PudahuelForm()

    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaPudahuel.html', {'form': form})

def sorepapuentealto(request):
    if request.method == 'POST':
        form = PuenteAltoForm(request.POST, request.FILES)
        if form.is_valid():
            datos_sorepa_puentealto = form.save(commit=False)
            datos_sorepa_puentealto.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('sorepapuentealto')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PuenteAltoForm()

    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaPuenteAlto.html', {'form': form})

def sorepaofi(request):
    if request.method == 'POST':
        form = RedOficinasForm(request.POST, request.FILES)
        if form.is_valid():
            datos_sorepa_oficinas = form.save(commit=False)
            datos_sorepa_oficinas.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('sorepaofi')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = RedOficinasForm()

    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaRedOficinas.html', {'form': form})

def sorepasanjoaquin(request):
    if request.method == 'POST':
        form = SanJoaquinForm(request.POST, request.FILES)
        if form.is_valid():
            datos_sorepa_sanjoaquin = form.save(commit=False)
            datos_sorepa_sanjoaquin.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('sorepasanjoaquin')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = SanJoaquinForm()

    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaSanJoaquin.html', {'form': form})


#Edipac

def oficinas_concepcion(request):
    if request.method == 'POST':
        form = DatosCMPCMexicoForm(request.POST, request.FILES)
        if form.is_valid():
            datosmexico = form.save(commit=False)
            datosmexico.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('cmpc_argentina')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = DatosCMPCMexicoForm()

    return render(request, 'Instalaciones/CMPC/CMPC_Mexico.html', {'form': form})

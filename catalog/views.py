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


#Biopackaging Box Board
def maule(request):
    if request.method == 'POST':
        form = MauleForm(request.POST, request.FILES)
        if form.is_valid():
            datosmaule = form.save(commit=False)
            datosmaule.save()
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
            datosvaldivia = form.save(commit=False)
            datosvaldivia.save()
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
            datoschimolsa = form.save(commit=False)
            datoschimolsa.save()
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
            datoscordillera = form.save(commit=False)
            datoscordillera.save()
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
            datosbuin = form.save(commit=False)
            datosbuin.save()
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
            datososorno = form.save(commit=False)
            datososorno.save()
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
            datostiltil = form.save(commit=False)
            datostiltil.save()
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
            datossorepa_pudahuel = form.save(commit=False)
            datossorepa_pudahuel.save()
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
            datossorepa_puentealto = form.save(commit=False)
            datossorepa_puentealto.save()
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
            datossorepa_oficinas = form.save(commit=False)
            datossorepa_oficinas.save()
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
            datossorepa_sanjoaquin = form.save(commit=False)
            datossorepa_sanjoaquin.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('sorepasanjoaquin')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = SanJoaquinForm()

    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaSanJoaquin.html', {'form': form})


#Views Edipac

def oficinas_concepcion(request):
    if request.method == 'POST':
        form = OfiConcepcionForm(request.POST, request.FILES)
        if form.is_valid():
            datosofi_concepcion = form.save(commit=False)
            datosofi_concepcion.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('oficoncenpcion')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = DatosCMPCMexicoForm()

    return render(request, 'Instalaciones/Biopackaging/Edipac/OficinasConcepcion.html', {'form': form})

def oficinas_temuco(request):
    if request.method == 'POST':
        form = OfiTemucoForm(request.POST, request.FILES)
        if form.is_valid():
            datosofi_temuco = form.save(commit=False)
            datosofi_temuco.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('ofitemuco')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = OfiTemucoForm()

    return render(request, 'Instalaciones/Biopackaging/Edipac/OficinasTemuco.html', {'form': form})

def quilicura(request):
    if request.method == 'POST':
        form = QuilicuraForm(request.POST, request.FILES)
        if form.is_valid():
            datosquilicura = form.save(commit=False)
            datosquilicura.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('quilicura')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form =QuilicuraForm()

    return render(request, 'Instalaciones/Biopackaging/Edipac/PlantaQuilicura.html', {'form': form})

#Views SackKraft

def camposnovos(request):
    if request.method == 'POST':
        form = CamposNovosForm(request.POST, request.FILES)
        if form.is_valid():
            datoscampos_novos = form.save(commit=False)
            datoscampos_novos.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('camposnovos')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = CamposNovosForm()

    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/CamposNovos.html', {'form': form})

def chillan(request):
    if request.method == 'POST':
        form = ChillanForm(request.POST, request.FILES)
        if form.is_valid():
            datoschillan = form.save(commit=False)
            datoschillan.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('chillan')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = ChillanForm()

    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/Chillan.html', {'form': form})

def fabi(request):
    if request.method == 'POST':
        form = FabiForm(request.POST, request.FILES)
        if form.is_valid():
            datosfabi = form.save(commit=False)
            datosfabi.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('fabi')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = FabiForm()

    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/Fabi.html', {'form': form})

def guadalajara(request):
    if request.method == 'POST':
        form = GuadalajaraForm(request.POST, request.FILES)
        if form.is_valid():
            datosguadalajara = form.save(commit=False)
            datosguadalajara.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('guadalajara')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = GuadalajaraForm()

    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/Guadalajara.html', {'form': form})

def irapuato(request):
    if request.method == 'POST':
        form = IrapuatoForm(request.POST, request.FILES)
        if form.is_valid():
            datosirapuato = form.save(commit=False)
            datosirapuato.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('irapuato')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = IrapuatoForm()

    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/Irapuato.html', {'form': form})

def peru(request):
    if request.method == 'POST':
        form = PeruForm(request.POST, request.FILES)
        if form.is_valid():
            datosperu = form.save(commit=False)
            datosperu.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('peru')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PeruForm()

    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/Peru.html', {'form': form})

def piraidosul(request):
    if request.method == 'POST':
        form = PiraidoSulForm(request.POST, request.FILES)
        if form.is_valid():
            datospiraido_sul = form.save(commit=False)
            datospiraido_sul.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('piradosul')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PiraidoSulForm()

    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/PiraidoSul.html', {'form': form})

def sanjose(request):
    if request.method == 'POST':
        form = SanJoseForm(request.POST, request.FILES)
        if form.is_valid():
            datossanjose = form.save(commit=False)
            datossanjose.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('sanjose')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = SanJoseForm()

    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/SanJose.html', {'form': form})

#Bosques
def balnearios(request):
    if request.method == 'POST':
        form = BalneariosForm(request.POST, request.FILES)
        if form.is_valid():
            datosbalnearios = form.save(commit=False)
            datosbalnearios.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('balnearios')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = BalneariosForm()
    return render(request, 'Instalaciones/Bosques/Balnearios-y-casas-H.html', {'form': form})

def villaforest(request):
    if request.method == 'POST':
        form = VillaForestForm(request.POST, request.FILES)
        if form.is_valid():
            datosvilla_forest = form.save(commit=False)
            datosvilla_forest.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('villaforest')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = VillaForestForm()
    return render(request, 'Instalaciones/Bosques/Bases-y-Villas-Forest.html', {'form': form})

def bosquesplata(request):
    if request.method == 'POST':
        form = BosquesPlataForm(request.POST, request.FILES)
        if form.is_valid():
            datobosques_plata = form.save(commit=False)
            datobosques_plata.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('bosquesplata')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = BosquesPlataForm()
    return render(request, 'Instalaciones/Bosques/Bosques-del-Plata.html', {'form': form})

def edicorpo(request):
    if request.method == 'POST':
        form = EdiCorpoForm(request.POST, request.FILES)
        if form.is_valid():
            datoedicorpo = form.save(commit=False)
            datoedicorpo.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('edicorpo')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = EdiCorpoForm()
    return render(request, 'Instalaciones/Bosques/Edificio-Corporativo.html', {'form': form})

def transito(request):
    if request.method == 'POST':
        form = TransitoForm(request.POST, request.FILES)
        if form.is_valid():
            datotransito = form.save(commit=False)
            datotransito.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('transito')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = TransitoForm()
    return render(request, 'Instalaciones/Bosques/Oficina-Transito.html', {'form': form})

def coyhaique(request):
    if request.method == 'POST':
        form = CoyhaiqueForm(request.POST, request.FILES)
        if form.is_valid():
            datocoyhaique = form.save(commit=False)
            datocoyhaique.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('coyhaique')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = CoyhaiqueForm()
    return render(request, 'Instalaciones/Bosques/Vivero-Coyhaique.html', {'form': form})

def viverocd(request):
    if request.method == 'POST':
        form = ViveroForm(request.POST, request.FILES)
        if form.is_valid():
            datovivero = form.save(commit=False)
            datovivero.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('viverocd')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = ViveroForm()
    return render(request, 'Instalaciones/Bosques/ViveroCD.html', {'form': form})

#Maderas

def bucalemu(request):
    if request.method == 'POST':
        form = BucalemuForm(request.POST, request.FILES)
        if form.is_valid():
            datobucalemu = form.save(commit=False)
            datobucalemu.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('bucalemu')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = BucalemuForm()
    return render(request, 'Instalaciones/Maderas/AS_Bucalemu.html', {'form': form})

def mulchen(request):
    if request.method == 'POST':
        form = MulchenForm(request.POST, request.FILES)
        if form.is_valid():
            datomulchen = form.save(commit=False)
            datomulchen.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('mulchen')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = MulchenForm()
    return render(request, 'Instalaciones/Maderas/AS_Mulchen.html', {'form': form})

def nacimiento(request):
    if request.method == 'POST':
        form = NacimientoForm(request.POST, request.FILES)
        if form.is_valid():
            datonacimiento = form.save(commit=False)
            datonacimiento.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('nacimiento')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = NacimientoForm()
    return render(request, 'Instalaciones/Maderas/AS_Nacimiento.html', {'form': form})

def niuform(request):
    if request.method == 'POST':
        form = NiuformForm(request.POST, request.FILES)
        if form.is_valid():
            datoniuform = form.save(commit=False)
            datoniuform.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('niform')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = NiuformForm()
    return render(request, 'Instalaciones/Maderas/Niform_Los_Angeles.html', {'form': form})

def plywood(request):
    if request.method == 'POST':
        form = PlywoodForm(request.POST, request.FILES)
        if form.is_valid():
            datoplywood = form.save(commit=False)
            datoplywood.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('plywood')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PlywoodForm()
    return render(request, 'Instalaciones/Maderas/Plywood.html', {'form': form})

def coronel(request):
    if request.method == 'POST':
        form = CoronelForm(request.POST, request.FILES)
        if form.is_valid():
            datocoronel = form.save(commit=False)
            datocoronel.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('coronel')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = CoronelForm()
    return render(request, 'Instalaciones/Maderas/Rem_Coronel.html', {'form': form})

def remLA(request):
    if request.method == 'POST':
        form = RemLAForm(request.POST, request.FILES)
        if form.is_valid():
            datoremLA = form.save(commit=False)
            datoremLA.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('remLA')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = RemLAForm()
    return render(request, 'Instalaciones/Maderas/Rem_Los_Angeles.html', {'form': form})

#Pulp

def balneariolaja(request):
    if request.method == 'POST':
        form = BalnearioLajaForm(request.POST, request.FILES)
        if form.is_valid():
            datobalneariolaja = form.save(commit=False)
            datobalneariolaja.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('balneariolaja')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = BalnearioLajaForm()
    return render(request, 'Instalaciones/Pulp/Balneariolaja.html', {'form': form})

def casahuespedes(request):
    if request.method == 'POST':
        form = CasaHuespedesForm(request.POST, request.FILES)
        if form.is_valid():
            datocasahuespedes = form.save(commit=False)
            datocasahuespedes.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('casauhuespedes')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = CasaHuespedesForm()
    return render(request, 'Instalaciones/Pulp/Casasdehuespedes.html', {'form': form})

def guaiba(request):
    if request.method == 'POST':
        form = GuaibaForm(request.POST, request.FILES)
        if form.is_valid():
            datoguaiba = form.save(commit=False)
            datoguaiba.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('guaiba')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = GuaibaForm()
    return render(request, 'Instalaciones/Pulp/PlantaGuaíba.html', {'form': form})

def laja(request):
    if request.method == 'POST':
        form = LajaForm(request.POST, request.FILES)
        if form.is_valid():
            datolaja = form.save(commit=False)
            datolaja.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('laja')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = LajaForm()
    return render(request, 'Instalaciones/Pulp/PlantaLaja.html', {'form': form})

def pacifico(request):
    if request.method == 'POST':
        form = PacificoForm(request.POST, request.FILES)
        if form.is_valid():
            datopacifico = form.save(commit=False)
            datopacifico.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('pacifico')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PacificoForm()
    return render(request, 'Instalaciones/Pulp/PlantaPacifico.html', {'form': form})

def santafe(request):
    if request.method == 'POST':
        form = SantaFeForm(request.POST, request.FILES)
        if form.is_valid():
            datosantafe = form.save(commit=False)
            datosantafe.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('santafe')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = SantaFeForm()
    return render(request, 'Instalaciones/Pulp/PlantaSantaFe.html', {'form': form})
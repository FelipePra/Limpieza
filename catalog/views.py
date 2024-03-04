from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib import messages
from django.http import HttpResponse
import xlwt

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
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('cmpc_chile')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = DatosCMPCChileForm()

    datoschile = DatosCMPCChile.objects.all()
    return render(request, 'Instalaciones/CMPC/CMPC_Chile.html', {'form': form, 'datoschile': datoschile})
def eliminar_dato(request, dato_id):
    if request.method == 'POST':
        dato = DatosCMPCChile.objects.get(pk=dato_id)
        dato.delete()
    return redirect('cmpc_chile')

def modificar_dato(request, dato_id):
    dato = DatosCMPCChile.objects.get(pk=dato_id)
    if request.method == 'POST':
        form = DatosCMPCChileForm(request.POST, instance=dato)
        if form.is_valid():
            form.save()
            return redirect('cmpc_chile')
    else:
        form = DatosCMPCChileForm(instance=dato)
    return render(request, 'tu_template_para_modificar.html', {'form': form})

def descargar_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="datos_cmpc_chile.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Datos CMPC Chile')

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Número', 'Área', 'Dependencia', 'Detalle', 'Frecuencia', 'Procedimiento', 'Parámetros de Control', 'Horario']

    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title, font_style)

    font_style = xlwt.XFStyle()

    datos = DatosCMPCChile.objects.all().values_list('numero', 'area', 'dependencia', 'detalle', 'frecuencia', 'procedimientos', 'parametro_control', 'horario')

    for row in datos:
        row_num += 1
        for col_num, value in enumerate(row):
            ws.write(row_num, col_num, value, font_style)

    wb.save(response)
    return response
def cmpc_argentina(request):
    if request.method == 'POST':
        form = DatosCMPCArgentinaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('cmpc_argentina')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = DatosCMPCArgentinaForm()

    datosargentina = DatosCMPCArgentina.objects.all()
    return render(request, 'Instalaciones/CMPC/CMPC_Argentina.html', {'form':form, 'datosargentina':datosargentina})

def eliminar_datoarg(request, dato_id):
    if request.method == 'POST':
        dato = DatosCMPCArgentina.objects.get(pk=dato_id)
        dato.delete()
    return redirect('cmpc_argentina')

def modificar_datoarg(request, dato_id):
    dato = DatosCMPCArgentina.objects.get(pk=dato_id)
    if request.method == 'POST':
        form = DatosCMPCArgentinaForm(request.POST, instance=dato)
        if form.is_valid():
            form.save()
            return redirect('cmpc_argentina')
    else:
        form = DatosCMPCArgentinaForm(instance=dato)
    return render(request, 'tu_template_para_modificar.html', {'form': form})

def descargar_excelarg(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="datos_cmpc_argentina.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Datos CMPC Argentina')

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Número', 'Área', 'Dependencia', 'Detalle', 'Frecuencia', 'Procedimiento', 'Parámetros de Control', 'Horario']

    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title, font_style)

    font_style = xlwt.XFStyle()

    datos = DatosCMPCChile.objects.all().values_list('numero', 'area', 'dependencia', 'detalle', 'frecuencia', 'procedimientos', 'parametro_control', 'horario')

    for row in datos:
        row_num += 1
        for col_num, value in enumerate(row):
            ws.write(row_num, col_num, value, font_style)

    wb.save(response)
    return response

def cmpc_brasil(request):
    if request.method == 'POST':
        form = DatosCMPCBrasilForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('cmpc_argentina')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = DatosCMPCBrasilForm()

    datosbrasil = DatosCMPCBrasil.objects.all()
    return render(request, 'Instalaciones/CMPC/CMPC_Brasil.html', {'form': form, 'datosbrasil': datosbrasil})


def eliminar_datonbra(request, dato_id):
    if request.method == 'POST':
        dato = DatosCMPCArgentina.objects.get(pk=dato_id)
        dato.delete()
    return redirect('cmpc_argentina')

def modificar_datobra(request, dato_id):
    dato = DatosCMPCArgentina.objects.get(pk=dato_id)
    if request.method == 'POST':
        form = DatosCMPCArgentinaForm(request.POST, instance=dato)
        if form.is_valid():
            form.save()
            return redirect('cmpc_argentina')
    else:
        form = DatosCMPCArgentinaForm(instance=dato)
    return render(request, 'tu_template_para_modificar.html', {'form': form})

def descargar_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="datos_cmpc_argentina.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Datos CMPC Argentina')

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Número', 'Área', 'Dependencia', 'Detalle', 'Frecuencia', 'Procedimiento', 'Parámetros de Control', 'Horario']

    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title, font_style)

    font_style = xlwt.XFStyle()

    datos = DatosCMPCChile.objects.all().values_list('numero', 'area', 'dependencia', 'detalle', 'frecuencia', 'procedimientos', 'parametro_control', 'horario')

    for row in datos:
        row_num += 1
        for col_num, value in enumerate(row):
            ws.write(row_num, col_num, value, font_style)

    wb.save(response)
    return response

def cmpc_mexico(request):
    if request.method == 'POST':
        form = DatosCMPCMexicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('cmpc_mexico')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = DatosCMPCMexicoForm()

    datosmexico = DatosCMPCMexico.objects.all()
    return render(request, 'Instalaciones/CMPC/CMPC_Mexico.html', {'form': form, 'datosmexico': datosmexico})


#Biopackaging Box Board
def maule(request):
    if request.method == 'POST':
        form = MauleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('maule')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = MauleForm()
    maule = Maule.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Box-Board/Maule.html', {'form': form, 'maule': maule})

def valdivia(request):
    if request.method == 'POST':
        form = ValdiviaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('valdivia')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = ValdiviaForm()

    valdivia = Valdivia.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Box-Board/Valdivia.html', {'form': form, 'valdivia': valdivia})

# Biopackaging Corrugados

def chimolsa(request):
    if request.method == 'POST':
        form = ChimolsaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('chimolsa')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = ChimolsaForm()

    chimolsa = Chimolsa.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Corrugados/Chimolsa.html', {'form': form, 'chimolsa': chimolsa})

def cordillera(request):
    if request.method == 'POST':
        form = CordilleraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('cordillera')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = CordilleraForm()

    cordillera = Cordillera.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Corrugados/Cordillera.html', {'form': form, 'cordillera': cordillera})

def buin(request):
    if request.method == 'POST':
        form = BuinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('buin')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = BuinForm()

    buin = Buin.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIIBuin.html', {'form': form, 'buin': buin})

def osorno(request):
    if request.method == 'POST':
        form = OsornoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('osorno')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = OsornoForm()

    osorno = Osorno.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIIOsorno.html', {'form': form, 'osorno': osorno})

def tiltil(request):
    if request.method == 'POST':
        form = TilTilForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('tiltil')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = TilTilForm()

    tiltil = TilTil.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Corrugados/EEIITilTil.html', {'form': form, 'tiltil': tiltil})

def sorepapudahuel(request):
    if request.method == 'POST':
        form = PudahuelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('sorepapudahuel')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PudahuelForm()

    pudahuel = Pudahuel.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaPudahuel.html', {'form': form, 'pudahuel': pudahuel})

def sorepapuentealto(request):
    if request.method == 'POST':
        form = PuenteAltoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('sorepapuentealto')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PuenteAltoForm()

    puentealto = PuenteAlto.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaPuenteAlto.html', {'form': form, 'puentealto': puentealto})

def sorepaofi(request):
    if request.method == 'POST':
        form = RedOficinasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('sorepaofi')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = RedOficinasForm()

    redoficinas = RedOficinas.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaRedOficinas.html', {'form': form, 'redoficinas': redoficinas})

def sorepasanjoaquin(request):
    if request.method == 'POST':
        form = SanJoaquinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('sorepasanjoaquin')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = SanJoaquinForm()

    sanjoaquin = SanJoaquin.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Corrugados/SorepaSanJoaquin.html', {'form': form, 'sanjoaquin': sanjoaquin})


#Views Edipac

def oficoncepcion(request):
    if request.method == 'POST':
        form = OfiConcepcionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('oficoncepcion')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = OfiConcepcionForm()

    oficoncepcion = OfiConcepcion.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Edipac/OficinasConcepcion.html', {'form': form, 'oficoncepcion': oficoncepcion})

def oficinas_temuco(request):
    if request.method == 'POST':
        form = OfiTemucoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('ofitemuco')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = OfiTemucoForm()

    ofitemuco = OfiTemuco.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Edipac/OficinasTemuco.html', {'form': form, 'ofitemuco': ofitemuco})

def quilicura(request):
    if request.method == 'POST':
        form = QuilicuraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('quilicura')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = QuilicuraForm()

    quilicura = Quilicura.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Edipac/PlantaQuilicura.html', {'form': form, 'quilicura': quilicura})

#Views SackKraft

def camposnovos(request):
    if request.method == 'POST':
        form = CamposNovosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('camposnovos')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = CamposNovosForm()

    camposnovos = CamposNovos.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/CamposNovos.html', {'form': form, 'camposnovos':camposnovos})

def chillan(request):
    if request.method == 'POST':
        form = ChillanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('chillan')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = ChillanForm()

    chillan = Chillan.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/Chillan.html', {'form': form, 'chillan': chillan})

def fabi(request):
    if request.method == 'POST':
        form = FabiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('fabi')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = FabiForm()

    fabi = Fabi.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/Fabi.html', {'form': form, 'fabi': fabi})

def guadalajara(request):
    if request.method == 'POST':
        form = GuadalajaraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('guadalajara')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = GuadalajaraForm()

    guadalajara = Guadalajara.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/Guadalajara.html', {'form': form, 'guadalajara': guadalajara})

def irapuato(request):
    if request.method == 'POST':
        form = IrapuatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('irapuato')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = IrapuatoForm()

    irapuato = Irapuato.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/Irapuato.html', {'form': form, 'irapuato': irapuato})

def peru(request):
    if request.method == 'POST':
        form = PeruForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('peru')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PeruForm()

    peru = Peru.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/Peru.html', {'form': form, 'peru': peru})

def piraidosul(request):
    if request.method == 'POST':
        form = PiraidoSulForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('piraidosul')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PiraidoSulForm()

    piraidosul = PiraidoSul.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/PiraidoSul.html', {'form': form, 'piraidosul':piraidosul})

def sanjose(request):
    if request.method == 'POST':
        form = SanJoseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('sanjose')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = SanJoseForm()

    sanjose = SanJose.objects.all()
    return render(request, 'Instalaciones/Biopackaging/Sack-Kraft/SanJose.html', {'form': form, 'sanjose': sanjose})

#Bosques
def balnearios(request):
    if request.method == 'POST':
        form = BalneariosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('balnearios')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = BalneariosForm()

    balnearios = Balnearios.objects.all()
    return render(request, 'Instalaciones/Bosques/Balnearios-y-casas-H.html', {'form': form, 'balnearios': balnearios})

def villaforest(request):
    if request.method == 'POST':
        form = VillaForestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('villaforest')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = VillaForestForm()

    villaforest = VillaForest.objects.all()
    return render(request, 'Instalaciones/Bosques/Bases-y-Villas-Forest.html', {'form': form, 'villaforest': villaforest})

def bosquesplata(request):
    if request.method == 'POST':
        form = BosquesPlataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('bosquesplata')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = BosquesPlataForm()

    bosquesplata = BosquesPlata.objects.all()
    return render(request, 'Instalaciones/Bosques/Bosques-del-Plata.html', {'form': form, 'bosquesplata':bosquesplata})

def edicorpo(request):
    if request.method == 'POST':
        form = EdiCorpoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('edicorpo')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = EdiCorpoForm()

    edicorpo = EdiCorpo.objects.all()
    return render(request, 'Instalaciones/Bosques/Edificio-Corporativo.html', {'form': form, 'edicorpo': edicorpo})

def transito(request):
    if request.method == 'POST':
        form = TransitoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('transito')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = TransitoForm()

    transito = Transito.objects.all()
    return render(request, 'Instalaciones/Bosques/Oficina-Transito.html', {'form': form, 'transito': transito})

def coyhaique(request):
    if request.method == 'POST':
        form = CoyhaiqueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('coyhaique')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = CoyhaiqueForm()
    
    coyhaique = Coyhaique.objects.all()
    return render(request, 'Instalaciones/Bosques/Vivero-Coyhaique.html', {'form': form, 'coyhaique': coyhaique})

def viverocd(request):
    if request.method == 'POST':
        form = ViveroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('viverocd')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = ViveroForm()

    viverocd = Vivero.objects.all()
    return render(request, 'Instalaciones/Bosques/ViveroCD.html', {'form': form, 'viverocd': viverocd})

#Maderas

def bucalemu(request):
    if request.method == 'POST':
        form = BucalemuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('bucalemu')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = BucalemuForm()

    bucalemu = Bucalemu.objects.all()
    return render(request, 'Instalaciones/Maderas/AS_Bucalemu.html', {'form': form, 'bucalemu': bucalemu})

def mulchen(request):
    if request.method == 'POST':
        form = MulchenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('mulchen')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = MulchenForm()

    mulchen = Mulchen.objects.all()
    return render(request, 'Instalaciones/Maderas/AS_Mulchen.html', {'form': form, 'mulchen': mulchen})

def nacimiento(request):
    if request.method == 'POST':
        form = NacimientoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('nacimiento')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = NacimientoForm()

    nacimiento = Nacimiento.objects.all()
    return render(request, 'Instalaciones/Maderas/AS_Nacimiento.html', {'form': form, 'nacimiento': nacimiento})

def niuform(request):
    if request.method == 'POST':
        form = NiuformForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('niuform')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = NiuformForm()
    
    niuform = Niuform.objects.all()
    return render(request, 'Instalaciones/Maderas/Niuform_Los_Angeles.html', {'form': form, 'niuform': niuform})

def plywood(request):
    if request.method == 'POST':
        form = PlywoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('plywood')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PlywoodForm()

    plywood = Plywood.objects.all()
    return render(request, 'Instalaciones/Maderas/Plywood.html', {'form': form, 'plywood': plywood})

def coronel(request):
    if request.method == 'POST':
        form = CoronelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('coronel')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = CoronelForm()

    coronel = Coronel.objects.all()
    return render(request, 'Instalaciones/Maderas/Rem_Coronel.html', {'form': form, 'coronel': coronel})

def remLA(request):
    if request.method == 'POST':
        form = RemLAForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('remLA')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = RemLAForm()

    remLA = RemLA.objects.all()
    return render(request, 'Instalaciones/Maderas/Rem_Los_Angeles.html', {'form': form, 'remLA': remLA})

#Pulp

def balneariolaja(request):
    if request.method == 'POST':
        form = BalnearioLajaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('balneariolaja')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = BalnearioLajaForm()

    balneariolaja = BalnearioLaja.objects.all()
    return render(request, 'Instalaciones/Pulp/Balneariolaja.html', {'form': form, 'balneariolaja': balneariolaja})

def casahuespedes(request):
    if request.method == 'POST':
        form = CasaHuespedesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('casauhuespedes')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = CasaHuespedesForm()

    casahuespedes = CasaHuespedes.objects.all()
    return render(request, 'Instalaciones/Pulp/Casasdehuespedes.html', {'form': form,'casahuespedes': casahuespedes})

def guaiba(request):
    if request.method == 'POST':
        form = GuaibaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('guaiba')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = GuaibaForm()

    guaiba = Guaiba.objects.all()
    return render(request, 'Instalaciones/Pulp/PlantaGuaíba.html', {'form': form, 'guaiba': guaiba})

def laja(request):
    if request.method == 'POST':
        form = LajaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('laja')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = LajaForm()

    laja = Laja.objects.all()
    return render(request, 'Instalaciones/Pulp/PlantaLaja.html', {'form': form, 'laja': laja})

def pacifico(request):
    if request.method == 'POST':
        form = PacificoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('pacifico')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = PacificoForm()

    pacifico = Pacifico.objects.all()
    return render(request, 'Instalaciones/Pulp/PlantaPacifico.html', {'form': form, 'pacifico': pacifico})

def santafe(request):
    if request.method == 'POST':
        form = SantaFeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos ingresados correctamente')
            return redirect('santafe')
        else:
            messages.error(request, 'Error al ingresar los datos. Por favor, revise los datos ingresados.')
    else:
        form = SantaFeForm()

    santafe = SantaFe.objects.all()
    return render(request, 'Instalaciones/Pulp/PlantaSantaFe.html', {'form': form, 'santafe': santafe})
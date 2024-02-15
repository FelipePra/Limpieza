from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contrato, Asistencia, Servicio
from .serializers import ContratoSerializer, AsistenciaSerializer, ServicioSerializer

# Vistas para renderizar las plantillas HTML

def index_view(request):
    return render(request, 'index.html')

def contratos_list_view(request):
    contratos = Contrato.objects.all()
    return render(request, 'Contratos/contratos_list.html', {'contratos': contratos})

def asistencias_list_view(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'Asistencia/asistencias_list.html', {'asistencias': asistencias})

def servicios_list_view(request):
    servicios = Servicio.objects.all()
    return render(request, 'Servicios/servicios_list.html', {'asistencias': servicios})


# Vistas de Instalaciones
def instalaciones(request):
    return render(request, 'Instalaciones/instalaciones.html')

def bosques(request):
    return render(request, 'Instalaciones/Index/Bosques.html')



def ejemplo_api(request):
    return render(request, 'ejemplo.html')

# Vistas para las APIs

@api_view(['GET', 'POST'])
def contrato_api(request):
    if request.method == 'GET':
        contratos = Contrato.objects.all()
        serializer = ContratoSerializer(contratos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContratoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def asistencia_api(request):
    if request.method == 'GET':
        asistencias = Asistencia.objects.all()
        serializer = AsistenciaSerializer(asistencias, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AsistenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def servicio_api(request):
    if request.method == 'GET':
        servicios = Servicio.objects.all()
        serializer = ServicioSerializer(servicios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



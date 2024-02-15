"""
URL configuration for Limpieza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from catalog import views

urlpatterns = [
    # Rutas para renderizar las plantillas HTML
    path('', views.index_view, name='index'),
    path('contratos/', views.contratos_list_view, name='contratos_list'),
    path('asistencias/', views.asistencias_list_view, name='asistencias_list'),
    path('servicios/', views.servicios_list_view, name='servicios_list'),

    #Rutas Instalaciones
    path('instalaciones/', views.instalaciones, name='instalaciones'),
    path('bosques/', views.bosques, name='bosques'),

    # Rutas para las APIs
    path('api/contratos/', views.contrato_api),
    path('api/asistencias/', views.asistencia_api),
    path('api/servicios/', views.servicio_api),
    path('ejemplo/ejemplo/', views.ejemplo_api),
]

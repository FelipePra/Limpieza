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
from catalog.views import ContratoListCreate, ContratoRetrieveUpdateDestroy, AsistenciaListCreate, AsistenciaRetrieveUpdateDestroy, index

urlpatterns = [
    path('', index, name='index'),
    path('api/contratos/', ContratoListCreate.as_view(), name='contrato-list-create'),
    path('api/contratos/<int:pk>/', ContratoRetrieveUpdateDestroy.as_view(), name='contrato-detail'),
    path('api/asistencias/', AsistenciaListCreate.as_view(), name='asistencia-list-create'),
    path('api/asistencias/<int:pk>/', AsistenciaRetrieveUpdateDestroy.as_view(), name='asistencia-detail'),
    # Otras rutas de URL para tus otras vistas
]

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
    path('index/', views.index, name='index'),
    path('servicios/', views.servicios_list_view, name='servicios_list'),


    #urls CMPC
    path('cmpc_chile/', views.cmpc_chile, name='cmpc_chile'),
    path('cmpc_argentina/', views.cmpc_argentina, name='cmpc_argentina'),
    #urls Instalaciones
    path('instalaciones/', views.instalaciones, name='instalaciones'),
    
    path('bosques/', views.bosques, name='bosques'),
    path('pulp/', views.pulp, name='pulp'),
    path('biopackaging/', views.biopackaging , name='biopackaging'),
    path('maderas/', views.maderas, name='maderas'),

    #urls Biopackaging
    path('boxboard/', views.boxboard, name='boxboard'),
    path('corrugados/', views.corrugados , name='corrugados'),
    path('edipac/', views.edipac, name='edipac'),
    path('sackkraft/', views.sackkraft, name='sackkraft'),
]

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
    path('', views.index, name='index'),

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

   #urls CMPC
    path('cmpc_chile/', views.cmpc_chile, name='cmpc_chile'),
    path('cmpc_argentina/', views.cmpc_argentina, name='cmpc_argentina'),
    path('cmpc_brasil/', views.cmpc_brasil, name='cmpc_brasil'),
    path('cmpc_mexico/', views.cmpc_mexico, name='cmpc_mexico'),

    #urls Modificar
    path('modificar_chile/<int:dato_id>/', views.modificar_dato_chile, name='modificar_dato_chile'),
    path('modificar_argentina/<int:dato_id>/', views.modificar_dato_argentina, name='modificar_dato_argentina'),
    path('modificar_brasil/<int:dato_id>/', views.modificar_dato_brasil, name='modificar_dato_brasil'),
    path('modificar_mexico/<int:dato_id>/', views.modificar_dato_mexico, name='modificar_dato_mexico'),
    #ursl Eliminar
    path('eliminar_dato_chile/<int:dato_id>/', views.eliminar_dato_chile, name='eliminar_dato_chile'),
    path('eliminar_dato_argentina/<int:dato_id>/', views.eliminar_dato_argentina, name='eliminar_dato_argentina'),
    path('eliminar_dato_brasil/<int:dato_id>/', views.eliminar_dato_brasil, name='eliminar_dato_brasil'),
    path('eliminar_dato_mexico/<int:dato_id>/', views.eliminar_dato_mexico, name='eliminar_dato_mexico'),

    #ursl Descargar excel
    path('descargar_excel_chile/', views.descargar_excel_chile, name='descargar_excel_chile'),
    path('descargar_excel_argentina/', views.descargar_excel_argentina, name='descargar_excel_argentina'),
    path('descargar_excel_brasil/', views.descargar_excel_brasil, name='descargar_excel_brasil'),
    path('descargar_excel_mexico/', views.descargar_excel_mexico, name='descargar_excel_mexico'),


    #urls BoxBoard
    path('maule/', views.maule, name='maule'),
    path('valdivia/', views.valdivia, name='valdivia'),

    #urls Modificar

    path('modificar_maule/<int:dato_id>/', views.modificar_maule, name='modificar_maule'),
    path('modificar_valdivia/<int:dato_id>/', views.modificar_valdivia, name='modificar_valdivia'),

    #urls Eliminar

    path('eliminar_maule/<int:dato_id>/', views.eliminar_maule, name='eliminar_maule'),
    path('eliminar_valdivia/<int:dato_id>/', views.eliminar_valdivia, name='eliminar_valdivia'),

    #urls Descargar excel

    path('descargar_excel_maule/', views.descargar_excel_maule, name='descargar_excel_maule'),
    path('descargar_excel_valdivia/', views.descargar_excel_valdivia, name='descargar_excel_valdivia'),


    #urls Edipac
    path('oficoncepcion/', views.oficoncepcion, name='oficoncepcion'),
    path('ofitemuco/', views.oficinas_temuco, name='ofitemuco'),
    path('quilicura/', views.quilicura, name='quilicura'),

    #urls SacKraft
    path('camposnovos/', views.camposnovos, name='camposnovos'),
    path('chillan/', views.chillan, name='chillan'),
    path('fabi/', views.fabi, name='fabi'),
    path('guadalajara/', views.guadalajara, name='guadalajara'),
    path('irapuato/', views.irapuato, name='irapuato'),
    path('peru/', views.peru, name='peru'),
    path('piraidosul/', views.piraidosul,name='piraidosul'),
    path('sanjose/', views.sanjose, name='sanjose'),

    #ursl Corrugados
    path('chimolsa/', views.chimolsa, name='chimolsa'),
    path('cordillera/', views.cordillera, name='cordillera'),
    path('buin/', views.buin, name='buin'),
    path('osorno/', views.osorno, name='osorno'),
    path('tiltil/', views.tiltil, name='tiltil'),
    path('sorepapudahuel/', views.sorepapudahuel, name='sorepapudahuel'),
    path('sorepapuentealto/', views.sorepapuentealto, name='sorepapuentealto'),
    path('sorepaofi/', views.sorepaofi, name='sorepaofi'),
    path('sorepasanjoaquin/', views.sorepasanjoaquin, name='sorepasanjoaquin'),

    #Urls Bosques
    path('balnearios/', views.balnearios, name='balnearios'),
    path('villaforest/', views.villaforest, name='villaforest'),
    path('bosquesplata/', views.bosquesplata, name='bosquesplata'),
    path('edicorpo/', views.edicorpo, name='edicorpo'),
    path('transito/', views.transito, name='transito'),
    path('coyhaique/',views.coyhaique, name='coyhaique'),
    path('viverocd/', views.viverocd, name='viverocd'),

    #Ursl Maderas
    path('bucalemu/',views.bucalemu, name='bucalemu'),
    path('mulchen/',views.mulchen, name='mulchen'),
    path('nacimiento/',views.nacimiento,name='nacimiento'),
    path('niuform/',views.niuform, name='niuform'),
    path('plywood/',views.plywood, name='plywood'),
    path('coronel/',views.coronel, name='coronel'),
    path('remLA/',views.remLA, name='remLA'),

    #Urls Pulp
    path('balneariolaja/', views.balneariolaja, name='balneariolaja'),
    path('casahuespedes/', views.casahuespedes, name='casahuespedes'),
    path('guaiba/', views.guaiba, name='guaiba'),
    path('laja/', views.laja, name='laja'),
    path('pacifico/', views.pacifico, name='pacifico'),
    path('santafe/', views.santafe, name='santafe'),
]

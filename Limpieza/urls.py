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
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('contratos/', views.calendar, name='calendar'),

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

    #ursl Modificar
    path('modificar_oficoncepcion/<int:dato_id>/', views.modificar_oficoncepcion, name='modificar_oficoncepcion'),
    path('modificar_ofitemuco/<int:dato_id>', views.modificar_ofitemuco, name='modificar_ofitemuco'),
    path('modificar_quilicura/<int:dato_id>/', views.modificar_quilicura, name='modificar_quilicura'),

    #ursl Eliminar
    path('eliminar_oficoncepcion/<int:dato_id>/', views.eliminar_oficoncepcion, name='eliminar_oficoncepcion'),
    path('eliminar_ofitemuco/<int:dato_id>/', views.eliminar_ofitemuco, name='eliminar_ofitemuco'),
    path('eliminar_quilicura/<int:dato_id>/', views.eliminar_quilicura, name='eliminar_quilicura'),

    #ursl Descargar excel
    path('descargar_excel_oficoncepcion/', views.descargar_excel_oficoncepcion, name='descargar_excel_oficoncepcion'),
    path('descargar_excel_ofitemuco/', views.descargar_excel_ofitemuco, name='descargar_excel_ofitemuco'),
    path('descargar_excel_quilicura/', views.descargar_excel_quilicura, name='descargar_excel_quilicura'),

    #urls SacKraft
    path('camposnovos/', views.camposnovos, name='camposnovos'),
    path('chillan/', views.chillan, name='chillan'),
    path('fabi/', views.fabi, name='fabi'),
    path('guadalajara/', views.guadalajara, name='guadalajara'),
    path('irapuato/', views.irapuato, name='irapuato'),
    path('peru/', views.peru, name='peru'),
    path('piraidosul/', views.piraidosul,name='piraidosul'),
    path('sanjose/', views.sanjose, name='sanjose'),

    #ursl Modificar
    path('modificar_camposnovos/<int:dato_id>/', views.modificar_camposnovos, name='modificar_camposnovos'),
    path('modificar_chillan/<int:dato_id>/', views.modificar_chillan, name='modificar_chillan'),
    path('modificar_fabi/<int:dato_id>/', views.modificar_fabi, name='modificar_fabi'),
    path('modificar_guadalajara/<int:dato_id>/', views.modificar_guadalajara, name='modificar_guadalajara'),
    path('modificar_irapuato/<int:dato_id>/', views.modificar_irapuato, name='modificar_irapuato'),
    path('modificar_peru/<int:dato_id>/', views.modificar_peru, name='modificar_peru'),
    path('modificar_piraidosul/<int:dato_id>/', views.modificar_piraidosul, name='modificar_piraidosul'),
    path('modificar_sanjose/<int:dato_id>/', views.modificar_sanjose, name='modificar_sanjose'),

    #ursl Eliminar
    path('eliminar_camposnovos/<int:dato_id>/', views.eliminar_camposnovos, name='eliminar_camposnovos'),
    path('eliminar_chillan/<int:dato_id>/', views.eliminar_chillan, name='eliminar_chillan'),
    path('eliminar_fabi/<int:dato_id>/', views.eliminar_fabi, name='eliminar_fabi'),
    path('eliminar_guadalajara/<int:dato_id>/', views.eliminar_guadalajara, name='eliminar_guadalajara'),
    path('eliminar_irapuato/<int:dato_id>/', views.eliminar_irapuato, name='eliminar_irapuato'),
    path('eliminar_peru/<int:dato_id>/', views.eliminar_peru, name='eliminar_peru'),
    path('eliminar_piraidosul/<int:dato_id>/', views.eliminar_piraidosul, name='eliminar_piraidosul'),
    path('eliminar_sanjose/<int:dato_id>', views.eliminar_sanjose, name='eliminar_sanjose'),

    #ursl Descargar excel

    path('descargar_excel_camposnovos/', views.descargar_excel_camposnovos, name='descargar_excel_camposnovos'),
    path('descargar_excel_chillan/', views.descargar_excel_chillan, name='descargar_excel_chillan'),
    path('descargar_excel_fabi/', views.descargar_excel_fabi, name='descargar_excel_fabi'),
    path('descargar_excel_guadalajara/', views.descargar_excel_guadalajara, name='descargar_excel_guadalajara'),
    path('descargar_excel_irapuato/', views.descargar_excel_irapuato, name='descargar_excel_irapuato'),
    path('descargar_excel_peru/', views.descargar_excel_peru, name='descargar_excel_peru'),
    path('descargar_excel_piraidosul/', views.descargar_excel_piraidosul, name='descargar_excel_piraidosul'),
    path('descargar_excel_sanjose/', views.descargar_excel_sanjose, name='descargar_excel_sanjose'),

    #ursl Corrugados
    path('chimolsa/', views.chimolsa, name='chimolsa'),
    path('cordillera/', views.cordillera, name='cordillera'),
    path('buin/', views.buin, name='buin'),
    path('osorno/', views.osorno, name='osorno'),
    path('tiltil/', views.tiltil, name='tiltil'),
    path('sorepapudahuel/', views.sorepapudahuel, name='sorepapudahuel'),
    path('sorepapuentealto/', views.sorepapuentealto, name='sorepapuentealto'),
    path('redoficinas/', views.redoficinas, name='redoficinas'),
    path('sorepasanjoaquin/', views.sorepasanjoaquin, name='sorepasanjoaquin'),

    #urls Modificar
    path('modificar_chimolsa/<int:dato_id>/', views.modificar_chimolsa, name='modificar_chimolsa'),
    path('modificar_cordillera/<int:dato_id>/', views.modificar_cordillera, name='modificar_cordillera'),
    path('modificar_buin/<int:dato_id>/', views.modificar_buin, name='modificar_buin'),
    path('modificar_osorno/<int:dato_id>/', views.modificar_osorno, name='modificar_osorno'),
    path('modificar_tiltil/<int:dato_id>/', views.modificar_tiltil, name='modificar_tiltil'),
    path('modificar_sorepapudahuel/<int:dato_id>/', views.modificar_sorepapudahuel, name='modificar_sorepapudahuel'),
    path('modificar_sorepapuentealto/<int:dato_id>/', views.modificar_sorepapuentealto, name='modificar_sorepapuentealto'),
    path('modificar_redoficinas/<int:dato_id>/', views.modificar_redoficinas, name='modificar_redoficinas'),
    path('modificar_sorepasanjoaquin/<int:dato_id>/', views.modificar_sorepasanjoaquin, name='modificar_sorepasanjoaquin'),

    #urls Eliminar
    path('eliminar_chimolsa/<int:dato_id>/', views.eliminar_chimolsa, name='eliminar_chimolsa'),
    path('eliminar_cordillera/<int:dato_id>/', views.eliminar_cordillera, name='eliminar_cordillera'),
    path('eliminar_buin/<int:dato_id>/', views.eliminar_buin, name='eliminar_buin'),
    path('eliminar_osorno/<int:dato_id>/', views.eliminar_osorno, name='eliminar_osorno'),
    path('eliminar_tiltil/<int:dato_id>/', views.eliminar_tiltil, name='eliminar_tiltil'),
    path('eliminar_sorepapudahuel/<int:dato_id>/', views.eliminar_sorepapudahuel, name='eliminar_sorepapudahuel'),
    path('eliminar_sorepapuentealto/<int:dato_id>/', views.eliminar_sorepapuentealto, name='eliminar_sorepapuentealto'),
    path('eliminar_redoficinas/<int:dato_id>', views.redoficinas, name='eliminar_redoficinas'),
    path('eliminar_sorepasanjoaquin/<int:dato_id>/', views.eliminar_sorepasanjoaquin, name='eliminar_sorepasanjoaquin'),

    #urls Descargar excel
    path('descargar_excel_chimolsa/', views.descargar_excel_chimolsa, name='descargar_excel_chimolsa'),
    path('descargar_excel_cordillera/', views.descargar_excel_cordillera, name='descargar_excel_cordillera'),
    path('descargar_excel_buin/', views.descargar_excel_buin, name='descargar_excel_buin'),
    path('descargar_excel_osorno/', views.descargar_excel_osorno, name='descargar_excel_osorno'),
    path('descargar_excel_tiltil/', views.descargar_excel_tiltil, name='descargar_excel_tiltil'),
    path('descargar_excel_sorepapudahuel/', views.descargar_excel_sorepapudahuel, name='descargar_excel_sorepapudahuel'),
    path('descargar_excel_sorepapuentealto/', views.descargar_excel_sorepapuentealto, name='descargar_excel_sorepapuentealto'),
    path('descargar_excel_redoficinas/', views.descargar_excel_redoficinas, name='descargar_excel_redoficinas'),
    path('descargar_excel_sorepasanjoaquin/', views.descargar_excel_sorepasanjoaquin, name='descargar_excel_sorepasanjoaquin'),

    #Urls Bosques
    path('balnearios/', views.balnearios, name='balnearios'),
    path('villaforest/', views.villaforest, name='villaforest'),
    path('bosquesplata/', views.bosquesplata, name='bosquesplata'),
    path('edicorpo/', views.edicorpo, name='edicorpo'),
    path('transito/', views.transito, name='transito'),
    path('coyhaique/',views.coyhaique, name='coyhaique'),
    path('viverocd/', views.viverocd, name='viverocd'),

    #ursl Modificar
    path('modificar_balnearios/<int:dato_id>/', views.modificar_balnearios, name='modificar_balnearios'),
    path('modificar_villaforest/<int:dato_id>/', views.modificar_villaforest, name='modificar_villaforest'),
    path('modificar_bosquesplata/<int:dato_id>/', views.modificar_bosquesplata, name='modificar_bosquesplata'),
    path('modificar_edicorpo/<int:dato_id>/', views.modificar_edicorpo, name='modificar_edicorpo'),
    path('modificar_transito/<int:dato_id>/', views.modificar_transito, name='modificar_transito'),
    path('modificar_coyhaique/<int:dato_id>/', views.modificar_coyhaique, name='modificar_coyhaique'),
    path('modificar_viverocd/<int:dato_id>/', views.modificar_viverocd, name='modificar_viverocd'),

    #ursl Eliminar
    path('eliminar_balnearios/<int:dato_id>/', views.eliminar_balnearios, name='eliminar_balnearios'),
    path('eliminar_villaforest/<int:dato_id>/', views.eliminar_villaforest, name='eliminar_villaforest'),
    path('eliminar_bosquesplata/<int:dato_id>/', views.eliminar_bosquesplata, name='eliminar_bosquesplata'),
    path('eliminar_edicorpo/<int:dato_id>/', views.eliminar_edicorpo, name='eliminar_edicorpo'),
    path('eliminar_transito/<int:dato_id>/', views.eliminar_transito, name='eliminar_transito'),
    path('eliminar_coyhaique/<int:dato_id>/', views.eliminar_coyhaique, name='eliminar_coyhaique'),
    path('eliminar_viverocd/<int:dato_id>/', views.eliminar_viverocd, name='eliminar_viverocd'),

    #urls Descargar excel
    path('descargar_excel_balnearios/', views.descargar_excel_balnearios, name='descargar_excel_balnearios'),
    path('descargar_excel_villaforest/', views.descargar_excel_villaforest, name='descargar_excel_villaforest'),
    path('descargar_excel_bosquesplata/', views.descargar_excel_bosquesplata, name='descargar_excel_bosquesplata'),
    path('descargar_excel_edicorpo/', views.descargar_excel_edicorpo, name='descargar_excel_edicorpo'),
    path('descargar_excel_transito/', views.descargar_excel_transito, name='descargar_excel_transito'),
    path('descargar_excel_coyhaique/', views.descargar_excel_coyhaique, name='descargar_excel_coyhaique'),
    path('descargar_excel_viverocd/', views.descargar_excel_viverocd, name='descargar_excel_viverocd'),


    #Ursl Maderas
    path('bucalemu/',views.bucalemu, name='bucalemu'),
    path('mulchen/',views.mulchen, name='mulchen'),
    path('nacimiento/',views.nacimiento,name='nacimiento'),
    path('niuform/',views.niuform, name='niuform'),
    path('plywood/',views.plywood, name='plywood'),
    path('coronel/',views.coronel, name='coronel'),
    path('remLA/',views.remLA, name='remLA'),

    #urls Modificar
    path('modificar_bucalemu/<int:dato_id>/',views.modificar_bucalemu, name='modificar_bucalemu'),
    path('modificar_mulchen/<int:dato_id>/',views.modificar_mulchen, name='modificar_mulchen'),
    path('modificar_nacimiento/<int:dato_id>/',views.modificar_nacimiento,name='modificar_nacimiento'),
    path('modificar_niuform/<int:dato_id>/',views.modificar_niuform, name='modificar_niuform'),
    path('modificar_plywood/<int:dato_id>/',views.modificar_plywood, name='modificar_plywood'),
    path('modificar_coronel/<int:dato_id>/',views.modificar_coronel, name='modificar_coronel'),
    path('modificar_remLA/<int:dato_id>/',views.modificar_remLA, name='modificar_remLA'),

    #urls Eliminar
    path('eliminar_bucalemu/<int:dato_id>/', views.eliminar_bucalemu, name='eliminar_bucalemu'),
    path('eliminar_mulchen/<int:dato_id>/', views.eliminar_mulchen, name='eliminar_mulchen'),
    path('eliminar_nacimiento/<int:dato_id>/', views.eliminar_nacimiento,name='eliminar_nacimiento'),
    path('eliminar_niuform/<int:dato_id>/', views.eliminar_niuform, name='eliminar_niuform'),
    path('eliminar_plywood/<int:dato_id>/', views.eliminar_plywood, name='eliminar_plywood'),
    path('eliminar_coronel/<int:dato_id>/', views.eliminar_coronel, name='eliminar_coronel'),
    path('eliminar_remLA/<int:dato_id>/', views.eliminar_remLA, name='eliminar_remLA'),

    #urls Descargar excel
    path('descargar_excel_bucalemu/', views.descargar_excel_bucalemu, name='descargar_excel_bucalemu'),
    path('descargar_excel_mulchen/', views.descargar_excel_mulchen, name='descargar_excel_mulchen'),
    path('descargar_excel_nacimiento/', views.descargar_excel_nacimiento,name='descargar_excel_nacimiento'),
    path('descargar_excel_niuform/', views.descargar_excel_niuform, name='descargar_excel_niuform'),
    path('descargar_excel_plywood/', views.descargar_excel_plywood, name='descargar_excel_plywood'),
    path('descargar_excel_coronel/', views.descargar_excel_coronel, name='descargar_excel_coronel'),
    path('descargar_excel_remLA/', views.descargar_excel_remLA, name='descargar_excel_remLA'),


    #Urls Pulp
    path('balneariolaja/', views.balneariolaja, name='balneariolaja'),
    path('casahuespedes/', views.casahuespedes, name='casahuespedes'),
    path('guaiba/', views.guaiba, name='guaiba'),
    path('laja/', views.laja, name='laja'),
    path('pacifico/', views.pacifico, name='pacifico'),
    path('santafe/', views.santafe, name='santafe'),

    #ursl Modificar
    path('modificar_balneariolaja/<int:dato_id>/', views.modificar_balneariolaja, name='modificar_balneariolaja'),
    path('modificar_casahuespedes/<int:dato_id>/', views.modificar_casahuespedes, name='modificar_casahuespedes'),
    path('modificar_guaiba/<int:dato_id>/', views.modificar_guaiba, name='modificar_guaiba'),
    path('modificar_laja/<int:dato_id>/', views.modificar_laja, name='modificar_laja'),
    path('modificar_pacifico/<int:dato_id>/', views.modificar_pacifico, name='modificar_pacifico'),
    path('modificar_santafe/<int:dato_id>/', views.modificar_santafe, name='modificar_santafe'),

    #ursl Eliminar
    path('eliminar_balneariolaja/<int:dato_id>/',views.eliminar_balneariolaja, name='eliminar_balneariolaja'),
    path('eliminar_casahuespedes/<int:dato_id>/', views.eliminar_casahuespedes, name='eliminar_casahuespedes'),
    path('eliminar_guaiba/<int:dato_id>', views.eliminar_guaiba, name='eliminar_guaiba'),
    path('eliminar_laja/<int:dato_id>/', views.eliminar_laja, name='eliminar_laja'),
    path('eliminar_pacifico/<int:dato_id>/', views.eliminar_pacifico, name='eliminar_pacifico'),
    path('eliminar_santafe/<int:dato_id>/', views.eliminar_santafe, name='eliminar_santafe'),

    #urls Descargar excel
    path('descargar_excel_balneariolaja/',views.descargar_excel_balneariolaja, name='descargar_excel_balneariolaja'),
    path('descargar_excel_casahuespedes/', views.descargar_excel_casahuespedes, name='descargar_excel_casahuespedes'),
    path('descargar_excel_guaiba/', views.descargar_excel_guaiba, name='descargar_excel_guaiba'),
    path('descargar_excel_laja/', views.descargar_excel_laja,name='descargar_excel_laja'),
    path('descargar_excel_pacifico/', views.descargar_excel_pacifico, name='descargar_excel_pacifico'),
    path('descargar_excel_santafe/', views.descargar_excel_santafe, name='descargar_excel_santafe'),

]

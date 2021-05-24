from django.urls import path

from core.activos.views.activos import views
from core.activos.views.activos.views import *
from core.activos.views.dashboard.views import DashboardView
from core.activos.views.datos.views import *
from core.activos.views.equiposRed.views import *
from core.activos.views.hardware.views import *
from core.activos.views.noDeterminado.views import *
from core.activos.views.nube.views import *
from core.activos.views.ordenadores.views import *
from core.activos.views.plugin.views import *
from core.activos.views.protocolo.views import *
from core.activos.views.puertos.views import *
from core.activos.views.redes.views import *
from core.activos.views.software.views import *
from core.activos.views.vulnerabilidad.views import *

app_name = 'activos'

urlpatterns = [
    path('activo/listado/', ActivoListView.as_view(), name="activos_list"),
    path('activo/añadir/', ActivoCreateView.as_view(), name="activos_add"),
    path('activo/editar/<pk>/', ActivoUpdateView.as_view(), name="activos_edit"),
    path('activo/eliminar/<pk>/', ActivoDeleteView.as_view(), name="activos_delete"),
    path('activo/formulario/', ActivoFormView.as_view(), name="activos_form"),
    path('activo/vulnerabilidades/<pk>/', ActivoVulnerabilidadesListView.as_view(), name="activos_vulnerabilidades"),
    path('activo/vulnerabilidades/crear/<pk>/', views.añade_vulnerabilidades, name="activos_crear_vulnerabilidades"),

    path('datos/listado/', DatoListView.as_view(), name="datos_list"),
    path('datos/añadir/', DatoCreateView.as_view(), name="datos_add"),
    path('datos/editar/<pk>/', DatoUpdateView.as_view(), name="datos_edit"),
    path('datos/eliminar/<pk>/', DatoDeleteView.as_view(), name="datos_delete"),

    path('equipoRed/listado/', EquipoRedListView.as_view(), name="equipoRed_list"),
    path('equipoRed/añadir/', EquipoRedCreateView.as_view(), name="equipoRed_add"),
    path('equipoRed/editar/<pk>/', EquipoRedUpdateView.as_view(), name="equipoRed_edit"),
    path('equipoRed/eliminar/<pk>/', EquipoRedDeleteView.as_view(), name="equipoRed_delete"),

    path('hardware/listado/', HardwareListView.as_view(), name="hardware_list"),
    path('hardware/añadir/', HardwareCreateView.as_view(), name="hardware_add"),
    path('hardware/editar/<pk>/', HardwareUpdateView.as_view(), name="hardware_edit"),
    path('hardware/eliminar/<pk>/', HardwareDeleteView.as_view(), name="hardware_delete"),

    path('noDeterminado/listado/', NoDeterminadoListView.as_view(), name="noDeterminado_list"),
    path('noDeterminado/añadir/', NoDeterminadoCreateView.as_view(), name="noDeterminado_add"),
    path('noDeterminado/editar/<pk>/', NoDeterminadoUpdateView.as_view(), name="noDeterminado_edit"),
    path('noDeterminado/eliminar/<pk>/', NoDeterminadoDeleteView.as_view(), name="noDeterminado_delete"),

    path('nube/listado/', NubeListView.as_view(), name="nube_list"),
    path('nube/añadir/', NubeCreateView.as_view(), name="nube_add"),
    path('nube/editar/<pk>/', NubeUpdateView.as_view(), name="nube_edit"),
    path('nube/eliminar/<pk>/', NubeDeleteView.as_view(), name="nube_delete"),

    path('ordenador/listado/', OrdenadorListView.as_view(), name="ordenador_list"),
    path('ordenador/añadir/', OrdenadorCreateView.as_view(), name="ordenador_add"),
    path('ordenador/editar/<pk>/', OrdenadorUpdateView.as_view(), name="ordenador_edit"),
    path('ordenador/eliminar/<pk>/', OrdenadorDeleteView.as_view(), name="ordenador_delete"),

    path('plugin/listado/', PluginListView.as_view(), name="plugin_list"),
    path('plugin/añadir/', PluginCreateView.as_view(), name="plugin_add"),
    path('plugin/editar/<pk>/', PluginUpdateView.as_view(), name="plugin_edit"),
    path('plugin/eliminar/<pk>/', PluginDeleteView.as_view(), name="plugin_delete"),

    path('protocolo/listado/', ProtocoloListView.as_view(), name="protocolo_list"),
    path('protocolo/añadir/', ProtocoloCreateView.as_view(), name="protocolo_add"),
    path('protocolo/editar/<pk>/', ProtocoloUpdateView.as_view(), name="protocolo_edit"),
    path('protocolo/eliminar/<pk>/', ProtocoloDeleteView.as_view(), name="protocolo_delete"),

    path('puerto/listado/', PuertoListView.as_view(), name="puertos_list"),
    path('puerto/añadir/', PuertoCreateView.as_view(), name="puertos_add"),
    path('puerto/editar/<pk>/', PuertoUpdateView.as_view(), name="puertos_edit"),
    path('puerto/eliminar/<pk>/', PuertoDeleteView.as_view(), name="puertos_delete"),

    path('red/listado/', RedListView.as_view(), name="red_list"),
    path('red/añadir/', RedCreateView.as_view(), name="red_add"),
    path('red/editar/<pk>/', RedUpdateView.as_view(), name="red_edit"),
    path('red/eliminar/<pk>/', RedDeleteView.as_view(), name="red_delete"),

    path('software/listado/', SoftwareListView.as_view(), name="software_list"),
    path('software/añadir/', SoftwareCreateView.as_view(), name="software_add"),
    path('software/editar/<pk>/', SoftwareUpdateView.as_view(), name="software_edit"),
    path('software/eliminar/<pk>/', SoftwareDeleteView.as_view(), name="software_delete"),

    #home
    path('dashboard/', DashboardView.as_view(), name="dashboard"),

    path('vulnerabilidad/listado/', VulnerabilidadListView.as_view(), name="vulnerabilidad_list"),
    path('vulnerabilidad/eliminar/<pk>/', VulnerabilidadDeleteView.as_view(), name="vulnerabilidad_delete"),

]
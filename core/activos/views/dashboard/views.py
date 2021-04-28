from django.views.generic import TemplateView

from core.activos.models import *


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_grafico_por_impacto(self):
        data = []
        try:
            total = 0
            bajo = 0
            medio = 0
            alto = 0
            for vulnerabilidad in Vulnerabilidad.objects.all():
                for activo in vulnerabilidad.activo.all():
                    if activo.impacto == 'Alto':
                        alto+=1
                    elif activo.impacto == 'Bajo':
                        bajo+=1
                    else:
                        medio+=1
                total+=1
            if total != 0:
                data.append(alto/total)
                data.append(medio/total)
                data.append(bajo/total)
            else:
                data.append(0)
                data.append(0)
                data.append(0)
        except:
            pass
        return data

    def get_grafico_por_tipo(self):
        data = []
        hardware = 0
        datos = 0
        equipoRed = 0
        noDeterminado = 0
        nube = 0
        ordenador = 0
        plugin = 0
        protocolo = 0
        puerto = 0
        red = 0
        software = 0
        try:
            for vulnerabilidad in Vulnerabilidad.objects.all():
                for activo in vulnerabilidad.activo.all():
                    if hasattr(activo, 'dato'):
                        datos+=1
                    if hasattr(activo, 'equipoRed'):
                        equipoRed+=1
                    if hasattr(activo, 'noDeterminado'):
                        noDeterminado+=1
                    if hasattr(activo, 'nube'):
                        nube+=1
                    if hasattr(activo, 'ordenador'):
                        ordenador+=1
                    if hasattr(activo, 'hardware'):
                        hardware+=1
                    if hasattr(activo, 'plugin'):
                        plugin += 1
                    if hasattr(activo, 'puerto'):
                        puerto += 1
                    if hasattr(activo, 'protocolo'):
                        protocolo += 1
                    if hasattr(activo, 'red'):
                        red += 1
                    if hasattr(activo, 'software'):
                        software += 1
            data.append(datos)
            data.append(equipoRed)
            data.append(hardware)
            data.append(noDeterminado)
            data.append(nube)
            data.append(ordenador)
            data.append(plugin)
            data.append(protocolo)
            data.append(puerto)
            data.append(red)
            data.append(software)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['grafico_por_impacto'] = self.get_grafico_por_impacto()
        context['grafico_por_tipo'] = self.get_grafico_por_tipo()
        return context
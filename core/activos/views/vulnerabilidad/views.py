from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DeleteView
from django.utils.decorators import method_decorator

from core.activos.models import Vulnerabilidad


class VulnerabilidadListView(ListView):
    model = Vulnerabilidad
    template_name = 'vulnerabilidad/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Vulnerabilidad.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Vulnerabilidades'
        context['list_url'] = reverse_lazy('activos:vulnerabilidad_list')
        context['entity'] = 'Vulnerabilidad'
        return context

class VulnerabilidadDeleteView(DeleteView):
    model = Vulnerabilidad
    template_name = 'vulnerabilidad/delete.html'
    success_url = reverse_lazy('activos:vulnerabilidad_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Vulnerabilidad'
        context['list_url'] = reverse_lazy('activos:vulnerabilidad_list')
        context['entity'] = 'Vulnerabilidad'
        return context


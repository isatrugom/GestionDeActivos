from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.activos.forms import ProtocoloForm
from core.activos.models import Protocolo


class ProtocoloListView(ListView):
    model = Protocolo
    template_name = 'protocolo/list.html'

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
                for i in Protocolo.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Protocolos'
        context['create_url'] = reverse_lazy('activos:protocolo_add')
        context['list_url'] = reverse_lazy('activos:protocolo_list')
        context['entity'] = 'Protocolo'
        return context


class ProtocoloCreateView(CreateView):
    model = Protocolo
    form_class = ProtocoloForm
    template_name = 'protocolo/create.html'
    success_url = reverse_lazy('activos:protocolo_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Protocolo'
        context['list_url'] = reverse_lazy('activos:protocolo_list')
        context['entity'] = 'Protocolo'
        context['action'] = "add"
        return context


class ProtocoloUpdateView(UpdateView):
    model = Protocolo
    form_class = ProtocoloForm
    template_name = 'protocolo/create.html'
    success_url = reverse_lazy('activos:protocolo_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Protocolo'
        context['list_url'] = reverse_lazy('activos:protocolo_list')
        context['entity'] = 'Protocolo'
        context['action'] = "edit"
        return context


class ProtocoloDeleteView(DeleteView):
    model = Protocolo
    template_name = 'protocolo/delete.html'
    success_url = reverse_lazy('activos:protocolo_list')

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
        context['title'] = 'Eliminación de un Protocolo'
        context['list_url'] = reverse_lazy('activos:protocolo_list')
        context['entity'] = 'Protocolo'
        return context


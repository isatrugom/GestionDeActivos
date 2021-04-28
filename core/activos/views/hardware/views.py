from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.activos.forms import HardwareForm
from core.activos.models import Hardware


class HardwareListView(ListView):
    model = Hardware
    template_name = 'hardware/list.html'

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
                for i in Hardware.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Hardware'
        context['create_url'] = reverse_lazy('activos:hardware_add')
        context['list_url'] = reverse_lazy('activos:hardware_list')
        context['entity'] = 'Hardware'
        return context


class HardwareCreateView(CreateView):
    model = Hardware
    form_class = HardwareForm
    template_name = 'hardware/create.html'
    success_url = reverse_lazy('activos:hardware_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Hardware'
        context['list_url'] = reverse_lazy('activos:hardware_list')
        context['entity'] = 'Hardware'
        context['action'] = "add"
        return context


class HardwareUpdateView(UpdateView):
    model = Hardware
    form_class = HardwareForm
    template_name = 'hardware/create.html'
    success_url = reverse_lazy('activos:hardware_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Hardware'
        context['list_url'] = reverse_lazy('activos:hardware_list')
        context['entity'] = 'Hardware'
        context['action'] = "edit"
        return context


class HardwareDeleteView(DeleteView):
    model = Hardware
    template_name = 'hardware/delete.html'
    success_url = reverse_lazy('activos:hardware_list')

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
        context['title'] = 'Eliminación de un Hardware'
        context['list_url'] = reverse_lazy('activos:hardware_list')
        context['entity'] = 'Hardware'
        return context


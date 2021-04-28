from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.activos.forms import EquipoRedForm
from core.activos.models import EquipoRed


class EquipoRedListView(ListView):
    model = EquipoRed
    template_name = 'equipoRed/list.html'

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
                for i in EquipoRed.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Equipos de Red'
        context['create_url'] = reverse_lazy('activos:equipoRed_add')
        context['list_url'] = reverse_lazy('activos:equipoRed_list')
        context['entity'] = 'Equipos de Red'
        return context


class EquipoRedCreateView(CreateView):
    model = EquipoRed
    form_class = EquipoRedForm
    template_name = 'equipoRed/create.html'
    success_url = reverse_lazy('activos:equipoRed_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Equipo de Red'
        context['list_url'] = reverse_lazy('activos:equipoRed_list')
        context['entity'] = 'Equipo de Red'
        context['action'] = "add"
        return context


class EquipoRedUpdateView(UpdateView):
    model = EquipoRed
    form_class = EquipoRedForm
    template_name = 'equipoRed/create.html'
    success_url = reverse_lazy('activos:equipoRed_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Equipo de Red'
        context['list_url'] = reverse_lazy('activos:equipoRed_list')
        context['entity'] = 'Equipo de Red'
        context['action'] = "edit"
        return context


class EquipoRedDeleteView(DeleteView):
    model = EquipoRed
    template_name = 'equipoRed/delete.html'
    success_url = reverse_lazy('activos:equipoRed_list')

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
        context['title'] = 'Eliminación de un Equipo de Red'
        context['list_url'] = reverse_lazy('activos:equipoRed_list')
        context['entity'] = 'Equipo de Red'
        return context


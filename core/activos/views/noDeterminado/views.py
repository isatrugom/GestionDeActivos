from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.activos.forms import NoDeterminadoForm
from core.activos.models import NoDeterminado


class NoDeterminadoListView(ListView):
    model = NoDeterminado
    template_name = 'noDeterminado/list.html'

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
                for i in NoDeterminado.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de No Determinado'
        context['create_url'] = reverse_lazy('activos:noDeterminado_add')
        context['list_url'] = reverse_lazy('activos:noDeterminado_list')
        context['entity'] = 'No Determinado'
        return context


class NoDeterminadoCreateView(CreateView):
    model = NoDeterminado
    form_class = NoDeterminadoForm
    template_name = 'noDeterminado/create.html'
    success_url = reverse_lazy('activos:noDeterminado_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un No Determinado'
        context['list_url'] = reverse_lazy('activos:noDeterminado_list')
        context['entity'] = 'No Determinado'
        context['action'] = "add"
        return context


class NoDeterminadoUpdateView(UpdateView):
    model = NoDeterminado
    form_class = NoDeterminadoForm
    template_name = 'noDeterminado/create.html'
    success_url = reverse_lazy('activos:noDeterminado_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un No Determinadoto'
        context['list_url'] = reverse_lazy('activos:noDeterminado_list')
        context['entity'] = 'No Determinado'
        context['action'] = "edit"
        return context


class NoDeterminadoDeleteView(DeleteView):
    model = NoDeterminado
    template_name = 'noDeterminado/delete.html'
    success_url = reverse_lazy('activos:noDeterminado_list')

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
        context['title'] = 'Eliminación de un No Determinado'
        context['list_url'] = reverse_lazy('activos:noDeterminado_list')
        context['entity'] = 'No Determinado'
        return context


from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, DetailView
from django.utils.decorators import method_decorator

from core.activos.forms import ActivoForm
from core.activos.models import Activo, Vulnerabilidad


class ActivoListView(ListView):
    model = Activo
    template_name = 'activo/list.html'

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
                for i in Activo.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Activos'
        context['create_url'] = reverse_lazy('activos:activos_add')
        context['list_url'] = reverse_lazy('activos:activos_list')
        context['entity'] = 'Activos'
        return context


class ActivoCreateView(CreateView):
    model = Activo
    form_class = ActivoForm
    template_name = 'activo/create.html'
    success_url = reverse_lazy('activos:activos_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error']: 'No se ha intoducido ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Activo'
        context['list_url'] = reverse_lazy('activos:activos_list')
        context['entity'] = 'Activos'
        context['action'] = "add"
        return context


class ActivoUpdateView(UpdateView):
    model = Activo
    form_class = ActivoForm
    template_name = 'activo/create.html'
    success_url = reverse_lazy('activos:activos_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error']: 'No se ha intoducido ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Activo'
        context['list_url'] = reverse_lazy('activos:activos_list')
        context['entity'] = 'Activos'
        context['action'] = "edit"
        return context


class ActivoDeleteView(DeleteView):
    model = Activo
    template_name = 'activo/delete.html'
    success_url = reverse_lazy('activos:activos_list')

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
        context['title'] = 'Eliminación de un Activo'
        context['list_url'] = reverse_lazy('activos:activos_list')
        context['entity'] = 'Activos'
        return context


class ActivoFormView(FormView):
    form_class = ActivoForm
    template_name = 'activo/create.html'
    success_url = reverse_lazy('activos:activos_list')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario de un Activo'
        context['list_url'] = reverse_lazy('activos:activos_list')
        context['entity'] = 'Activos'
        context['action'] = "add"
        return context

class ActivoVulnerabilidadesListView(DetailView):
    model = Activo
    template_name = 'activo/vulnerability.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchvulnerability':
                data = []
                for v in Vulnerabilidad.objects.all():
                    for activo in v.activo.all():
                        if activo == self.object:
                            data.append(v.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Vulnerabilidades de ' + self.get_object().nombre
        context['entity'] = 'Activos'
        return context

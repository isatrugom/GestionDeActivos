from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.activos.forms import PluginForm
from core.activos.models import Plugin


class PluginListView(ListView):
    model = Plugin
    template_name = 'plugin/list.html'

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
                for i in Plugin.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Plugins'
        context['create_url'] = reverse_lazy('activos:plugin_add')
        context['list_url'] = reverse_lazy('activos:plugin_list')
        context['entity'] = 'Plugin'
        return context


class PluginCreateView(CreateView):
    model = Plugin
    form_class = PluginForm
    template_name = 'plugin/create.html'
    success_url = reverse_lazy('activos:plugin_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Plugin'
        context['list_url'] = reverse_lazy('activos:plugin_list')
        context['entity'] = 'Plugin'
        context['action'] = "add"
        return context


class PluginUpdateView(UpdateView):
    model = Plugin
    form_class = PluginForm
    template_name = 'plugin/create.html'
    success_url = reverse_lazy('activos:plugin_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Plugin'
        context['list_url'] = reverse_lazy('activos:plugin_list')
        context['entity'] = 'Plugin'
        context['action'] = "edit"
        return context


class PluginDeleteView(DeleteView):
    model = Plugin
    template_name = 'plugin/delete.html'
    success_url = reverse_lazy('activos:plugin_list')

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
        context['title'] = 'Eliminación de un Plugin'
        context['list_url'] = reverse_lazy('activos:plugin_list')
        context['entity'] = 'Plugin'
        return context


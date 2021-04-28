from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.activos.forms import NubeForm
from core.activos.models import Nube


class NubeListView(ListView):
    model = Nube
    template_name = 'nube/list.html'

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
                for i in Nube.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Nube'
        context['create_url'] = reverse_lazy('activos:nube_add')
        context['list_url'] = reverse_lazy('activos:nube_list')
        context['entity'] = 'Nube'
        return context


class NubeCreateView(CreateView):
    model = Nube
    form_class = NubeForm
    template_name = 'nube/create.html'
    success_url = reverse_lazy('activos:nube_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Nube'
        context['list_url'] = reverse_lazy('activos:nube_list')
        context['entity'] = 'Nube'
        context['action'] = "add"
        return context


class NubeUpdateView(UpdateView):
    model = Nube
    form_class = NubeForm
    template_name = 'nube/create.html'
    success_url = reverse_lazy('activos:nube_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Nube'
        context['list_url'] = reverse_lazy('activos:nube_list')
        context['entity'] = 'Nube'
        context['action'] = "edit"
        return context


class NubeDeleteView(DeleteView):
    model = Nube
    template_name = 'nube/delete.html'
    success_url = reverse_lazy('activos:nube_list')

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
        context['title'] = 'Eliminación de una Nube'
        context['list_url'] = reverse_lazy('activos:nube_list')
        context['entity'] = 'Nube'
        return context


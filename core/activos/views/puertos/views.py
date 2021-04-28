from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.activos.forms import PuertoForm
from core.activos.models import Puerto


class PuertoListView(ListView):
    model = Puerto
    template_name = 'puerto/list.html'

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
                for i in Puerto.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Puertos'
        context['create_url'] = reverse_lazy('activos:puertos_add')
        context['list_url'] = reverse_lazy('activos:puertos_list')
        context['entity'] = 'Puertos'
        return context


class PuertoCreateView(CreateView):
    model = Puerto
    form_class = PuertoForm
    template_name = 'puerto/create.html'
    success_url = reverse_lazy('activos:puertos_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Puerto'
        context['list_url'] = reverse_lazy('activos:puertos_list')
        context['entity'] = 'Puertos'
        context['action'] = "add"
        return context


class PuertoUpdateView(UpdateView):
    model = Puerto
    form_class = PuertoForm
    template_name = 'puerto/create.html'
    success_url = reverse_lazy('activos:puertos_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Puerto'
        context['list_url'] = reverse_lazy('activos:puertos_list')
        context['entity'] = 'Puertos'
        context['action'] = "edit"
        return context


class PuertoDeleteView(DeleteView):
    model = Puerto
    template_name = 'puerto/delete.html'
    success_url = reverse_lazy('activos:puertos_list')

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
        context['title'] = 'Eliminación de un Puerto'
        context['list_url'] = reverse_lazy('activos:puertos_list')
        context['entity'] = 'Puertos'
        return context


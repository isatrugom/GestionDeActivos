from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.activos.forms import SoftwareForm
from core.activos.models import Software


class SoftwareListView(ListView):
    model = Software
    template_name = 'software/list.html'

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
                for i in Software.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Software'
        context['create_url'] = reverse_lazy('activos:software_add')
        context['list_url'] = reverse_lazy('activos:software_list')
        context['entity'] = 'Software'
        return context


class SoftwareCreateView(CreateView):
    model = Software
    form_class = SoftwareForm
    template_name = 'software/create.html'
    success_url = reverse_lazy('activos:software_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Software'
        context['list_url'] = reverse_lazy('activos:software_list')
        context['entity'] = 'Software'
        context['action'] = "add"
        return context


class SoftwareUpdateView(UpdateView):
    model = Software
    form_class = SoftwareForm
    template_name = 'software/create.html'
    success_url = reverse_lazy('activos:software_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Software'
        context['list_url'] = reverse_lazy('activos:software_list')
        context['entity'] = 'Software'
        context['action'] = "edit"
        return context


class SoftwareDeleteView(DeleteView):
    model = Software
    template_name = 'software/delete.html'
    success_url = reverse_lazy('activos:software_list')

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
        context['title'] = 'Eliminación de un Software'
        context['list_url'] = reverse_lazy('activos:software_list')
        context['entity'] = 'Software'
        return context


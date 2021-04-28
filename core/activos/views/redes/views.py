from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.activos.forms import RedForm
from core.activos.models import Red


class RedListView(ListView):
    model = Red
    template_name = 'red/list.html'

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
                for i in Red.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Redes'
        context['create_url'] = reverse_lazy('activos:red_add')
        context['list_url'] = reverse_lazy('activos:red_list')
        context['entity'] = 'Red'
        return context


class RedCreateView(CreateView):
    model = Red
    form_class = RedForm
    template_name = 'red/create.html'
    success_url = reverse_lazy('activos:red_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Red'
        context['list_url'] = reverse_lazy('activos:red_list')
        context['entity'] = 'Red'
        context['action'] = "add"
        return context


class RedUpdateView(UpdateView):
    model = Red
    form_class = RedForm
    template_name = 'red/create.html'
    success_url = reverse_lazy('activos:red_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Red'
        context['list_url'] = reverse_lazy('activos:red_list')
        context['entity'] = 'Red'
        context['action'] = "edit"
        return context


class RedDeleteView(DeleteView):
    model = Red
    template_name = 'red/delete.html'
    success_url = reverse_lazy('activos:red_list')

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
        context['title'] = 'Eliminación de una Red'
        context['list_url'] = reverse_lazy('activos:red_list')
        context['entity'] = 'Red'
        return context


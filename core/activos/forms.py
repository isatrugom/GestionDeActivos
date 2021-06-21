from django.forms import *

from core.activos.models import *


class ActivoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Activo
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
        }

    def save(self, commit=True):
        form = super()
        data = {}
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    def clean(self):
        cleaned = super().clean()
        # if condicion:
        #     raise forms.ValidationError('Validacion error')
        return cleaned


class PuertoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Puerto
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
            'numero': TextInput(
                attrs={
                    'placeholder': 'Escribe un número de puerto',
                }
            ),
        }


class DatoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Datos
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
            'ubicacion': TextInput(
                attrs={
                    'placeholder': 'Escribe la ubicación del archivo',
                }
            ),
        }


class EquipoRedForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = EquipoRed
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
            'modelo': TextInput(
                attrs={
                    'placeholder': 'Escribe un modelo',
                }
            ),
            'proveedor': TextInput(
                attrs={
                    'placeholder': 'Escribe un proveedor',
                }
            ),
            'numeroDeSerie': TextInput(
                attrs={
                    'placeholder': 'Escribe un número de serie',
                }
            ),
        }


class HardwareForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Hardware
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
            'modelo': TextInput(
                attrs={
                    'placeholder': 'Escribe un modelo',
                }
            ),
            'proveedor': TextInput(
                attrs={
                    'placeholder': 'Escribe un proveedor',
                }
            ),
            'numeroDeSerie': TextInput(
                attrs={
                    'placeholder': 'Escribe un número de serie',
                }
            ),
        }


class NoDeterminadoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = NoDeterminado
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
            'descripcion': TextInput(
                attrs={
                    'placeholder': 'Escribe la descripción',
                }
            ),
            'detalles': TextInput(
                attrs={
                    'placeholder': 'Añade algunos detalles',
                }
            ),
        }


class NubeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Nube
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
            'url': TextInput(
                attrs={
                    'placeholder': 'Escribe la url completa de acceso',
                }
            ),
            'dominio': TextInput(
                attrs={
                    'placeholder': 'Escribe el dominio',
                }
            ),
        }


class OrdenadorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Ordenador
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
            'modelo': TextInput(
                attrs={
                    'placeholder': 'Escribe un modelo',
                }
            ),
            'proveedor': TextInput(
                attrs={
                    'placeholder': 'Escribe un proveedor',
                }
            ),
            'numeroDeSerie': TextInput(
                attrs={
                    'placeholder': 'Escribe un número de serie',
                }
            ),
            'ram': TextInput(
                attrs={
                    'placeholder': 'Escribe la memoria RAM del ordenador',
                }
            ),
            'rom': TextInput(
                attrs={
                    'placeholder': 'Escribe la memoria ROM del ordenador',
                }
            ),
            'nucleos': TextInput(
                attrs={
                    'placeholder': 'Escribe el número de núcleos del ordenador',
                }
            ),
        }


class PluginForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Plugin
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
            'version': TextInput(
                attrs={
                    'placeholder': 'Escribe la versión del plugin',
                }
            ),
            'proveedor': TextInput(
                attrs={
                    'placeholder': 'Escribe el proveedor del plugin',
                }
            ),
            'fechaAdquisicion': DateInput(
                attrs={
                    'placeholder': 'Escribe la fecha de adquisión',
                }
            ),
            'fechaExpiracion': DateInput(
                attrs={
                    'placeholder': 'Escribe la fecha de expriación',
                }
            ),
        }


class ProtocoloForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Protocolo
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
            'version': TextInput(
                attrs={
                    'placeholder': 'Escribe la versión del protocolo',
                }
            ),

        }


class RedForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Red
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
            'cidr': TextInput(
                attrs={
                    'placeholder': 'Escribe el bloque CIDR que maneja la red',
                }
            ),

        }


class SoftwareForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Software
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Escribe un nombre',
                }
            ),
            'version': TextInput(
                attrs={
                    'placeholder': 'Escribe la versión del software',
                }
            ),
            'proveedor': TextInput(
                attrs={
                    'placeholder': 'Escribe el proveedor del software',
                }
            ),
            'fechaAdquisicion': DateInput(
                attrs={
                    'placeholder': 'Escribe la fecha de adquisión',
                }
            ),
            'fechaExpiracion': DateInput(
                attrs={
                    'placeholder': 'Escribe la fecha de expriación',
                }
            ),
        }

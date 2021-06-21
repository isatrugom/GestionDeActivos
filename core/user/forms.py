from django.forms import ModelForm, TextInput, PasswordInput

from core.user.models import User


class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'imagen'
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Introduce el nombre',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Introduce los apellidos',
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Introduce el email',
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder': 'Introduce el nombre de usuario',
                }
            ),
        }
        exclude = ['last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff', 'password']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                u = form.save(commit=False)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)



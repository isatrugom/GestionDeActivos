from django.urls import path

from core.user.views import *

app_name = 'usuario'


urlpatterns = [
    path('perfil/', UserProfileView.as_view(), name='user_profile'),
    path('cambiarContraseña/', UserChangePasswordView.as_view(), name='user_change_password'),
]

from config.wsgi import *
from core.activos.models import Activo
# Insercción
a = Activo()
a.nombre = "Prueba1"
a.impacto = "Alto"
a.save()
a = Activo()
a.nombre = "Prueba2"
a.impacto = "Medio"
a.save()
a = Activo()
a.nombre = "Prueba3"
a.impacto = "Bajo"
a.save()

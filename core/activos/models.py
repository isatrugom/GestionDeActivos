from django.db import models
from datetime import datetime

from django.forms import model_to_dict
from django.utils import timezone


# Activo
from config.settings import MEDIA_URL


class Activo(models.Model):
    IMPACTO = (
        ('Alto', 'Alto'),
        ('Medio', 'Medio'),
        ('Bajo', 'Bajo'),
    )
    nombre = models.TextField(verbose_name='Nombre')
    impacto = models.CharField(verbose_name='Impacto', max_length=5, choices=IMPACTO)
    timestamp = models.DateTimeField(default=timezone.now, verbose_name='Timestamp')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Activo"
        verbose_name_plural = "Activos"
        db_table = 'activo'
        ordering = ['id']


# Vulnerabilidad
class Vulnerabilidad(models.Model):
    id = models.TextField(verbose_name='Id', primary_key=True)
    archivo = models.FileField(upload_to='vulnerabilidades/%Y/%m/%d/', verbose_name='Archivo', null=True, blank=True)
    activo = models.ManyToManyField(Activo)

    def __str__(self):
        return self.id

    def toJSON(self):
        item = model_to_dict(self, exclude=["activo", "archivo"])
        activo_serializable = []
        for ac in self.activo.all():
            activo_serializable.append(ac.nombre)
        item['activo'] = activo_serializable
        if self.archivo:
            item['archivo'] = '{}{}'.format(MEDIA_URL, self.archivo)
        else:
            item['archivo'] = ""
        return item

    class Meta:
        verbose_name = "Vulnerabilidad"
        verbose_name_plural = "Vulnerabilidades"
        db_table = 'vulnerabilidad'
        ordering = ['id']


# Red
class Red(Activo):
    cidr = models.TextField(verbose_name='Bloque CIDR')
    nat = models.BooleanField(verbose_name='NAT')

    def __str__(self):
        return self.cidr

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Red"
        verbose_name_plural = "Redes"
        db_table = 'red'
        ordering = ['id']


# No determinado
class NoDeterminado(Activo):
    descripcion = models.TextField(verbose_name='Descripción')
    detalles = models.TextField(verbose_name='Detalles')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "No determinado"
        verbose_name_plural = "No determinados"
        db_table = 'noDeterminado'
        ordering = ['id']


# Nube
class Nube(Activo):
    url = models.TextField(verbose_name='URL')
    dominio = models.TextField(verbose_name='Dominio')

    def __str__(self):
        return self.url

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Nube"
        verbose_name_plural = "Nube"
        db_table = 'nube'
        ordering = ['id']


# Datos
class Datos(Activo):
    ubicacion = models.TextField(verbose_name='Ubicación')
    local = models.BooleanField(verbose_name='Local')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Dato"
        verbose_name_plural = "Datos"
        db_table = 'dato'
        ordering = ['id']


# Puerto
class Puerto(Activo):
    ESTADO = (
        ('Abiero', 'Abiero'),
        ('Cerrado', 'Cerrado'),
        ('Filtrado', 'Filtrado'),
    )
    numero = models.IntegerField(verbose_name='Número')
    estado = models.CharField(verbose_name='Estado', max_length=8, choices=ESTADO)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Puerto"
        verbose_name_plural = "Puertos"
        db_table = 'puerto'
        ordering = ['id']


# Protocolo
class Protocolo(Activo):
    puerto = models.ManyToManyField(Puerto, blank=True)
    version = models.TextField(verbose_name='Versión')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self, exclude='puerto')
        puerto_serializable = []
        for p in self.puerto.all():
            puerto_serializable.append(p.nombre)
        item['puerto'] = puerto_serializable
        return item

    class Meta:
        verbose_name = "Protocolo"
        verbose_name_plural = "Protocolos"
        db_table = 'protocolo'
        ordering = ['id']


# Plugin
class Plugin(Activo):
    protocolo = models.ManyToManyField(Protocolo, blank=True)
    version = models.TextField(verbose_name='Versión')
    proveedor = models.TextField(verbose_name='Proveedor')
    fechaAdquisicion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de adquisición")
    fechaExpiracion = models.DateTimeField(verbose_name="Fecha de expiración", null=True, blank=True)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self, exclude='protocolo')
        protocolo_serializable = []
        for p in self.protocolo.all():
            protocolo_serializable.append(p.nombre)
        item['protocolo'] = protocolo_serializable
        return item

    class Meta:
        verbose_name = "Plugin"
        verbose_name_plural = "Plugins"
        db_table = 'plugin'
        ordering = ['nombre']


# Software
class Software(Activo):
    TIPO = (
        ('Sistema operativo', 'Sistema operativo'),
        ('Firmware', 'Firmware'),
        ('Antivirus', 'Antivirus'),
        ('Aplicación Móvil', 'Aplicación Móvil'),
        ('Código', 'Código'),
    )
    plugin = models.ManyToManyField(Plugin, blank=True)
    datos = models.ManyToManyField(Datos, blank=True)
    version = models.TextField(verbose_name='Versión')
    proveedor = models.TextField(verbose_name='Proveedor')
    fechaAdquisicion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de adquisición")
    fechaExpiracion = models.DateTimeField(verbose_name="Fecha de expiración", null=True, blank=True)
    tipoSoftware = models.CharField(verbose_name="Tipo", max_length=17, choices=TIPO)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        plugin_serializable = []
        datos_serializable = []
        for p in self.plugin.all():
            plugin_serializable.append(p.nombre)
        item['plugin'] = plugin_serializable
        for d in self.datos.all():
            datos_serializable.append(d.nombre)
        item['datos'] = datos_serializable
        return item

    class Meta:
        verbose_name = "Software"
        verbose_name_plural = "Softwares"
        db_table = 'software'
        ordering = ['id']


# Hardware
class Hardware(Activo):
    TIPO = (
        ('Periférico', 'Periférico'),
        ('Servidor', 'Servidor'),
        ('Sensor', 'Sensor'),
        ('Actuador', 'Actuador'),
        ('Ordenador', 'Ordenador'),
        ('No determinado', 'No determinado'),
        ('Equipo de red', 'Equipo de red'),
        ('Smartphone', 'Smartphone'),
    )
    modelo = models.TextField(verbose_name='Modelo')
    proveedor = models.TextField(verbose_name='Proveedor')
    numeroDeSerie = models.TextField(verbose_name='Número de Serie')
    tipoHardware = models.CharField(verbose_name="Tipo", max_length=14, choices=TIPO)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Hardware"
        verbose_name_plural = "Hardware"
        db_table = 'hardware'
        ordering = ['id']


# Equipo de red
class EquipoRed(Hardware):
    TIPO = (
        ('Gateway', 'Gateway'),
        ('Interfaz', 'Interfaz'),
        ('Router', 'Router'),
        ('Switch', 'Switch'),
    )
    redAsociada = models.ForeignKey(Red, on_delete=models.CASCADE)
    tipoEquipo = models.CharField(verbose_name="Tipo", max_length=8, choices=TIPO)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Equipo de red"
        verbose_name_plural = "Equipos de red"
        db_table = 'equipo_red'
        ordering = ['id']


# Ordenador
class Ordenador(Hardware):
    software = models.ManyToManyField(Software, blank=True)
    datos = models.ManyToManyField(Datos, blank=True)
    ram = models.IntegerField(verbose_name='Memoria RAM')
    rom = models.IntegerField(verbose_name='Memoria ROM')
    nucleos = models.IntegerField(verbose_name='Número de núcleos')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self, exclude=['software','datos'])
        software_serializable = []
        datos_serializable = []
        for s in self.software.all():
            software_serializable.append(s.nombre)
        item['software'] = software_serializable
        for d in self.datos.all():
            datos_serializable.append(d.nombre)
        item['datos'] = datos_serializable
        return item

    class Meta:
        verbose_name = "Ordenador"
        verbose_name_plural = "Ordenadores"
        db_table = 'ordenador'
        ordering = ['id']

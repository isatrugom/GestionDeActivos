from django.conf.global_settings import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict


class User(AbstractUser):
    imagen = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/user.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'last_login', 'date_joined', 'imagen', 'full_name'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        return item


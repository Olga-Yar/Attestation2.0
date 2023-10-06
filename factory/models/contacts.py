from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Contacts(models.Model):
    email = models.EmailField(verbose_name='email', unique=True)
    country = models.CharField(max_length=20, verbose_name='страна')
    city = models.CharField(max_length=25, verbose_name='город')
    street = models.CharField(max_length=30, verbose_name='улица')
    house = models.IntegerField(verbose_name='номер дома')

    def __str__(self):
        return f'{self.email}, {self.country}, {self.city}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        
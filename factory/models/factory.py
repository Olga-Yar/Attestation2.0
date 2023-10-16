from django.db import models
from django.db.models import Sum

NULLABLE = {'blank': True, 'null': True}


class Factory(models.Model):
    name = models.CharField(max_length=50, verbose_name='название', unique=True)
    contact = models.ForeignKey('Contacts', on_delete=models.CASCADE, verbose_name='контакты')
    product = models.ManyToManyField('Products', verbose_name='продукция')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    level = models.IntegerField(default=0, verbose_name='уровень')

    def __str__(self):
        return f'{self.name} - {self.date_create}'

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'завод'

        
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Factory(models.Model):
    name = models.CharField(max_length=50, verbose_name='название', unique=True)
    contact = models.ForeignKey('Contacts', on_delete=models.CASCADE)
    product = models.ManyToManyField('Products')
    credit = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name='задолженность клиентов')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    level = models.IntegerField(default=0, verbose_name='уровень')

    def __str__(self):
        return f'{self.name} - {self.credit}'

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'завод'
        
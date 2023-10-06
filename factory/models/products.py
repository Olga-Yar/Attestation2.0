from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Products(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    model = models.CharField(max_length=50, verbose_name='модель')
    date_start_sell = models.DateTimeField(verbose_name='дата выхода на рынок')
    is_start_sell = models.BooleanField(default=False, verbose_name='старт продаж')

    def __str__(self):
        return f'{self.title}, {self.model}: {self.date_start_sell}, {self.is_start_sell}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        
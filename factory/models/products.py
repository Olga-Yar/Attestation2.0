from datetime import datetime

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Products(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    model = models.CharField(max_length=50, verbose_name='модель')
    date_start_sell = models.DateTimeField(verbose_name='дата выхода на рынок', **NULLABLE)
    is_start_sell = models.BooleanField(default=False, verbose_name='старт продаж')

    def __str__(self):
        return f'{self.title}, {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def save(self, *args, **kwargs):
        """Определение времени старта продаж"""
        if not self.is_start_sell:
            self.date_start_sell = None
        else:
            self.date_start_sell = datetime.now()

        super().save(*args, **kwargs)

from django.db import models
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class Company(models.Model):

    name = models.CharField(max_length=50, verbose_name='название', unique=True)
    contact = models.ForeignKey('Contacts', on_delete=models.CASCADE, verbose_name='контакты')
    product = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name='продукция')
    provider = models.ForeignKey('Contacts', on_delete=models.DO_NOTHING, related_name='company_provider')
    credit = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='задолженность')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    level = models.IntegerField(default=1, verbose_name='уровень')

    def __str__(self):
        return f'{self.name} - {self.credit}'

    class Meta:
        verbose_name = 'ИП'
        verbose_name_plural = 'ИП'

    def save(self, *args, **kwargs):
        """Определение уровня сети"""
        if self.provider.provider_type == "Factory":
            self.level = 1
        elif self.provider.provider_type == "Retail" or self.provider.provider_type == "Company":
            self.level = 2
        else:
            raise ValidationError(
                _('Ошибка в выборе поставщика.'),
            )
        super().save(*args, **kwargs)

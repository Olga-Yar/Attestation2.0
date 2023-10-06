from django.db import models
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class Company(models.Model):
    PROVIDER = [
        ('0', 'завод'),
        ('2', 'ИП'),
        ('1', 'розничная сеть'),
    ]

    name = models.CharField(max_length=50, verbose_name='название', unique=True)
    contact = models.ForeignKey('Contacts', on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    provider = models.CharField(choices=PROVIDER, verbose_name='поставщик')
    credit = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='задолженность')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    level = models.IntegerField(default=1, verbose_name='уровень')

    def __str__(self):
        return f'{self.name} - {self.credit}, {self.provider}'

    class Meta:
        verbose_name = 'ИП'
        verbose_name_plural = 'ИП'

    def save(self, *args, **kwargs):
        """Определение уровня сети"""
        if self.provider == 'завод':
            self.level = 1
        elif self.provider == 'розничная сеть':
            self.level = 2
        else:
            raise ValidationError(
                _('Поставщик должен быть: завод или розничная сеть'),
                code='invalid_choice_provider'
            )

        super().save(*args, **kwargs)
        
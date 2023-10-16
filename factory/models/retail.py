from django.db import models
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class Retail(models.Model):
    # PROVIDER = [
    #     ('Factory', 'Factory'),
    #     ('Company', 'Company'),
    #     ('Retail', 'Retail'),
    # ]

    name = models.CharField(max_length=50, verbose_name='название', unique=True)
    contact = models.ForeignKey('Contacts', on_delete=models.CASCADE, verbose_name='контакты')
    product = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name='продукция')
    provider = models.ForeignKey('Contacts', on_delete=models.DO_NOTHING, related_name='retail_provider')
    credit = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='задолженность')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    level = models.IntegerField(default=1, verbose_name='уровень')

    # def get_provider_model(self):
    #     """Определение модели поставщика"""
    #     if self.provider_type == 'Factory':
    #         return Factory
    #     elif self.provider_type == 'Company':
    #         return Company
    #     else:
    #         return ValidationError('Поставщик должен быть: Factory или Company')
    #
    # provider = models.ManyToManyField(get_provider_model)

    def __str__(self):
        return f'{self.name} - {self.credit}'

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'

    # def save(self, *args, **kwargs):
    #     """Определение уровня сети"""
    #     if self.provider == 'завод':
    #         self.level = 1
    #     elif self.provider == 'ИП':
    #         self.level = 2
    #     else:
    #         raise ValidationError(
    #             _('Поставщик должен быть: завод или ИП'),
    #             code='invalid_choice_provider'
    #         )
    #
    #     super().save(*args, **kwargs)
        
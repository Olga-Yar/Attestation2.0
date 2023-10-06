from django.db import models

from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class UserCustom(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    is_active = models.BooleanField(default=False, verbose_name='активный')

    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}: {self.is_active}, {self.role}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

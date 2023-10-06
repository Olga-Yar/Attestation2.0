from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.contrib import messages

from factory.models.factory import Factory


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contact', 'product',
        'provider', 'credit', 'date_create', 'level',
    )
    list_filter = ('contacts__city',)
        
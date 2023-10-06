from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.contrib import messages

from factory.models.products import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'model', 'date_start_sell', 'is_start_sell',
    )
            
from django.contrib import admin

from factory.models.products import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'model', 'date_start_sell', 'is_start_sell',
    )

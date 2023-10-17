from django.contrib import admin

from factory.models.factory import Factory


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contact',
        'get_city',
    )
    list_filter = ('contact__city',)

    def get_city(self, obj):
        """Получаем значение поля 'city' через связь с моделью Contacts"""
        return obj.contact.city

    get_city.short_description = 'город'

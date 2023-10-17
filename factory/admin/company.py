from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.utils.safestring import mark_safe

from factory.models.company import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contact', 'product',
        'credit', 'level', 'get_city',
        'provider_link',
    )
    list_display_links = ('name',)
    list_filter = ('contact__city', 'contact__country',)
    search_fields = ('name',)
    ordering = ('date_create',)
    actions = ['make_clear_credit']

    def get_city(self, obj):
        """Получаем значение поля 'city' через связь с моделью Contacts"""
        return obj.contact.city

    get_city.short_description = 'Город'

    def provider_link(self, obj):
        """Ссылка на поставщика"""
        return mark_safe(f'<a href="/admin/factory/contacts/{obj.provider.id}/change/">{obj.provider}</a>')

    provider_link.short_description = 'Поставщик'

    def make_clear_credit(self, request, queryset):
        """Очистка задолженности перед поставщиком"""
        for obj in queryset:
            obj.credit = 0
            obj.save()

        self.message_user(
            request,
            'Задолженность успешно очищена.'.format(messages.SUCCESS)
        )

        redirect_url = reverse('admin:factory_company_changelist')
        return HttpResponseRedirect(redirect_url)

    make_clear_credit.short_description = 'Очистить задолженность перед поставщиком у выбранных объектов'

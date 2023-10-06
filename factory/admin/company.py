from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.contrib import messages

from factory.models.company import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contact', 'product',
        'provider', 'credit', 'date_create', 'level', 'get_city',
    )
    list_filter = ('contact__city',)
    search_fields = ('name', 'provider',)
    ordering = ('date_create',)
    actions = ['make_clear_credit']

    def get_city(self, obj):
        """Получаем значение поля 'city' через связь с моделью Contacts"""
        return obj.contact.city

    get_city.short_description = 'city'

    def view_provider_list(self, obj):
        """Отображение ссылки на поставщика"""
        url = (
            reverse('admin:factory_company_changelist')
            + '?'
            + urlencode({'company__id': f'{obj.id}'})
        )
        return format_html('<a href="{}">{} providers</a>', url)

    view_provider_list.short_description = 'Provider'

    @admin.action(
        permissions=['change'],
        description='Очистить задолженность перед поставщиком у выбранных объектов',
    )
    def make_clear_credit(self, request, queryset):
        for item in queryset:
            item.credit = 0
            item.save()

        self.message_user(request,
                           'задолженность успешно очищена.'
                           % messages.SUCCESS
                           )

        selected = queryset.values_list('pk', flat=True)
        ct = ContentType.objects.get_for_model(queryset.model)
        return HttpResponseRedirect('/export/?ct=%s&ids=%s' % (
            ct.pk,
            ','.join(str(pk) for pk in selected),
        ))
        
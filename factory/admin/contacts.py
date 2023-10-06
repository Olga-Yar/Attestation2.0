from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.contrib import messages

from factory.models.contacts import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'country', 'city',
        'street', 'house',
    )
    list_filter = ('city',)
        
from django.contrib import admin


from factory.models.contacts import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'country', 'city',
        'street', 'house',
    )
    list_filter = ('city', 'country',)

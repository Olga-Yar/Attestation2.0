from rest_framework.viewsets import ModelViewSet

from factory.models.contacts import Contacts
from factory.serializers.contacts import ContactsSerializer


class ContactsViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    def get_permissions(self):
        """Проверка разрешения для различных методов"""
        pass

    def retrieve(self, request, pk=None, **kwargs):
        """Отображение личных записей"""
        pass

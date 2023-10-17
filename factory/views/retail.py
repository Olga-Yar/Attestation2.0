from rest_framework.viewsets import ModelViewSet

from factory.models.retail import Retail
from factory.permissions import IsActiveUser
from factory.serializers.retail import RetailSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    permission_classes = [IsActiveUser]

    def get_permissions(self):
        """Проверка разрешения для различных методов"""
        pass

    def retrieve(self, request, pk=None, **kwargs):
        """Отображение личных записей"""
        pass

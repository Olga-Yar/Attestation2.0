from rest_framework.viewsets import ModelViewSet

from factory.models.retail import Retail
from factory.serialzers.retail import RetailSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer

    def get_permissions(self):
        """Проверка разрешения для различных методов"""
        pass

    def retrieve(self, request, pk=None, **kwargs):
        """Отображение личных записей"""
        pass
        
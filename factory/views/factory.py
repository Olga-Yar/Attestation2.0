from rest_framework.viewsets import ModelViewSet

from factory.models.factory import Factory
from factory.permissions import IsActiveUser
from factory.serializers.factory import FactorySerializer


class CompanyViewSet(ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [IsActiveUser]

    def get_permissions(self):
        """Проверка разрешения для различных методов"""
        pass

    def retrieve(self, request, pk=None, **kwargs):
        """Отображение личных записей"""
        pass

from rest_framework.viewsets import ModelViewSet

from factory.models.company import Company
from factory.permissions import IsActiveUser
from factory.serializers.company import CompanySerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsActiveUser]

    def get_permissions(self):
        """Проверка разрешения для различных методов"""
        pass

    def retrieve(self, request, pk=None, **kwargs):
        """Отображение личных записей"""
        pass

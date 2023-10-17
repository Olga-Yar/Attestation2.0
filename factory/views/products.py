from rest_framework.viewsets import ModelViewSet

from factory.models.products import Products
from factory.serializers.products import ProductsSerializer


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def get_permissions(self):
        """Проверка разрешения для различных методов"""
        pass

    def retrieve(self, request, pk=None, **kwargs):
        """Отображение личных записей"""
        pass

from rest_framework import serializers

from factory.models.products import Products


class ProductsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Products
        fields = [
            'title', 'model', 'date_start_sell', 'is_start_sell',
        ]

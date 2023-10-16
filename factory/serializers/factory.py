from rest_framework import serializers

from factory.models.factory import Factory


class FactorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Factory
        fields = [
            'name', 'contact', 'product', 'provider',
            'date_create', 'level',
        ]

        
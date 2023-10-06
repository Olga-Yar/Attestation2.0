from rest_framework import serializers

from factory.models.retail import Retail


class RetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Retail
        fields = [
            'name', 'contact', 'product', 'provider', 'credit',
            'date_create', 'level',
        ]
        
        
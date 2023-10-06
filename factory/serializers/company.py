from rest_framework import serializers

from factory.models.company import Company


class CompanySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Company
        fields = [
            'name', 'contact', 'product', 'provider', 'credit',
            'date_create', 'level',
        ]
        
        
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

    def update(self, instance, validated_data):
        """Запрет на обновление поля задолженности перед поставщиком"""
        if 'credit' in validated_data:
            raise serializers.ValidationError("Обновление задолженности перед поставщиком запрещено.")

        return super().update(instance, validated_data)

        
        
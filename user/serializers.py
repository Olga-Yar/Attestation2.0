from rest_framework import serializers

from user.models import UserCustom


class UserCustomSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserCustom
        fields = [
            'username', 'email', 'password', 'role', 'is_active',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserCustom.objects.create_user(password=password, **validated_data)
        return user

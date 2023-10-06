from rest_framework import serializers

from factory.models.contacts import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Contacts
        fields = [
            'email', 'country', 'city', 'street', 'house',
        ]
        
        
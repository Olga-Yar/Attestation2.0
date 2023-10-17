
from rest_framework.viewsets import ModelViewSet

from user.models import UserCustom
from user.serializers import UserCustomSerializer


class UserCustomViewSet(ModelViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

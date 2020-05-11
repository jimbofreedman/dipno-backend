from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dipno_backend.users.models import User
from .serializers import UserSerializer
from .permissions import IsLoggedInUser


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsLoggedInUser]
    queryset = User.objects.filter()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

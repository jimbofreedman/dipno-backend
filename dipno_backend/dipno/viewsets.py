from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dipno_backend.users.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user, many=False)
        return Response(serializer.data)

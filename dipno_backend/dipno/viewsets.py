from django.db.models import Q

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dipno_backend.users.models import User
from dipno.models import Match
from .serializers import UserSerializer, MatchSerializer
from .permissions import IsLoggedInUser


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    resource_name = 'users'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    resource_name = 'users'
    permission_classes = [IsLoggedInUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class MatchViewSet(viewsets.ModelViewSet):
    resource_name = 'matches'
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.filter(Q(user1__id=self.request.user.id) | Q(user2__id=self.request.user.id))

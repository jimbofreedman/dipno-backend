from rest_framework_json_api import serializers
from ..users.models import User

from dipno.models import Match


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "available_from", "available_to", "facebook_link", "interests"]
        read_only_fields = ["id", "first_name", "last_name", "facebook_link"]


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ["user1", "user2", "accepted"]


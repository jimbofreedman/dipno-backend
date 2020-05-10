from rest_framework_json_api import serializers
from ..users.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]
        read_only_fields = ["id", "first_name", "last_name"]


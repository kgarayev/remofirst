import re

from rest_framework import serializers

from src.chatty.api.user.domain.exceptions import InvalidPasswordException
from src.chatty.api.user.domain.exceptions import InvalidUsernameException
from src.chatty.api.user.models.models import User


class User(serializers.ModelSerializer):

    # id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    # username = serializers.CharField(max_length=50)
    # email = serializers.EmailField()
    # password = serializers.CharField(min_length=8, max_length=128, required=True, write_only=True)
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "created_at", "updated_at"]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["id", "created_at", "updated_at"]
        ordering = ["created_at"]

    def validate_username(self, username):
        if not re.match(r"^[a-zA-Z0-9_]+$", username):
            raise InvalidUsernameException
        return username

    def validate_password(self, password):
        if len(password) < 8:
            raise InvalidPasswordException
        return password

    # email validation automatic

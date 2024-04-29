from api.chat.models import Session
from api.user.domain.models.models import User as UserModel
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ["id", "username", "email", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:

        fields = ["id", "username", "password"]

    def validate(self, data):
        query_set = UserModel.objects.filter(username=data.get("username"))

        if not query_set.exists():
            raise serializers.ValidationError("User does not exist.")

        user_model = query_set.first()

        if not user_model.check_password(data.get("password")):
            raise serializers.ValidationError("Invalid password.")

        return data


class RegisterUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=UserModel.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:

        model = UserModel

        fields = ["id", "username", "first_name", "last_name", "email", "password", "password_confirmation", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"required": True},
            "password": {"required": True},
        }

    def validate(self, data):
        if data["password"] != data["password_confirmation"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    @transaction.atomic
    def create(self, validated_data):
        validated_data.pop("password_confirmation")
        user = UserModel(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()
        # FIXME create chat session room automatically here; and add user.id to the room

        room_session = Session.objects.create()
        room_session.members.add(user.id)
        return user


# class User(serializers.ModelSerializer):

#     # id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
#     # username = serializers.CharField(max_length=50)
#     # email = serializers.EmailField()
#     # password = serializers.CharField(min_length=8, max_length=128, required=True, write_only=True)
#     # created_at = serializers.DateTimeField(read_only=True)
#     # updated_at = serializers.DateTimeField(read_only=True)

#     class Meta:
#         model = User
#         fields = ["id", "username", "email", "password", "created_at", "updated_at"]
#         extra_kwargs = {"password": {"write_only": True}}
#         read_only_fields = ["id", "created_at", "updated_at"]
#         ordering = ["created_at"]

#     def validate_username(self, username):
#         if not re.match(r"^[a-zA-Z0-9_]+$", username):
#             raise InvalidUsernameException
#         return username

#     def validate_password(self, password):
#         if len(password) < 8:
#             raise InvalidPasswordException
#         return password

#     # email validation automatic

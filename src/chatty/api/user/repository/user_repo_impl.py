from api.user.domain.serializers.entities import User
from chatty.api.user.models import User as UserModel
from api.user.repository.base import AbstractUserRepository


class UserRepository(AbstractUserRepository):
    "Coupling between the serializer and the model"

    def insert(self, user_payload):

        user = User(**user_payload)

        if user.is_valid():

            model = UserModel(**user_payload)
            model.password = model.hash_password(user_payload.get("password"))

            model.save()

            return user

        return user.errors

    def update(self, instance, user_payload): ...

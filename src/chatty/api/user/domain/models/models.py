from django.contrib.auth.models import AbstractUser

from src.chatty.api.user.models.base import BaseModel


class User(AbstractUser, BaseModel):

    class Meta:
        db_table = "users"

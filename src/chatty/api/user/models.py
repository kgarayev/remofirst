from django.contrib.auth.models import AbstractUser

from api.user.domain.models.base import BaseModel


class User(AbstractUser, BaseModel):

    class Meta:
        db_table = "users"
        verbose_name = 'user'
        verbose_name_plural = 'users'

# Create your models here.
from api.user.domain.models.base import BaseModel
from api.user.models import User as UserModel
from django.db import models


class Session(BaseModel):

    members = models.ManyToManyField(UserModel)

    def __str__(self):
        return f"{self.id} -- {self.members}"


class Message(BaseModel):

    session_id = models.ForeignKey(Session, on_delete=models.SET_NULL, related_name="messages", null=True)
    sender = models.ForeignKey(UserModel, on_delete=models.SET_NULL, related_name="sent_messages", null=True)
    message = models.TextField(null=False, blank=False)

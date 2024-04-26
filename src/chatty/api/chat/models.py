# Create your models here.
from django.db import models
from api.user.models import User as UserModel
from api.user.domain.models.base import BaseModel


class Session(BaseModel):
    
    members = models.ManyToManyField(UserModel, related_name="chat_sessions")


    def __str__(self):
        return f"{self.id} -- {self.members}"
    

class Message(BaseModel):

    session_id = models.ForeignKey(Session, on_delete=models.SET_NULL, related_name="messages", null=True)
    sender = models.ForeignKey(UserModel, on_delete=models.SET_NULL, related_name="sent_messages", null=True)
    message = models.TextField()
    
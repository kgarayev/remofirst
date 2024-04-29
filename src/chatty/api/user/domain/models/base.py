import uuid

from django.db import models


class BaseModel(models.Model):

    id = models.UUIDField(max_length=34, primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True
        ordering = ["created_at"]

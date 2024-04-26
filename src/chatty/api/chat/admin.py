from django.contrib import admin
from api.chat.models import Message, Session

admin.site.register(Message)
admin.site.register(Session)
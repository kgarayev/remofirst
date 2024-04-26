from django.urls import include, path
from api.chat.routers.views import ChatMessage

urlpatterns = [
    path('chat/<str:session_id>/messages', ChatMessage.as_view(), name='chat-message-list')
]
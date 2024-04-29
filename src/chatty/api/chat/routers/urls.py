from api.chat.routers.views import ChatMessageView, ChatSessionGetView, ChatSessionPostView, SendMessageView
from django.urls import path

urlpatterns = [
    path("chat/<str:session_id>/messages", ChatMessageView.as_view(), name="chat-message-list"),
    path("chat-sessions/", ChatSessionPostView.as_view(), name="chat-session"),
    path("users/<str:user_id>/chat-sessions", ChatSessionGetView.as_view(), name="user-chat-list"),
    path("send-message/", SendMessageView.as_view(), name="send-message"),
]

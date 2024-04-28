
from django.urls import re_path, path
from api.chat.websocket.consumers import ChatWSConsumer

# ws_patterns = [re_path(r"ws/chat/(?<session_id>\w+)", ChatWSConsumer.as_asgi())]

ws_patterns = [path(r"ws/chat/<session_id>", ChatWSConsumer.as_asgi())]
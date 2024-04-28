import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
import api.chat.websocket
import api.chat.websocket.routers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.infrastructure.settings")

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            api.chat.websocket.routers.ws_patterns
        )
    )
    # Just HTTP for now. (We can add other protocols later.)
})

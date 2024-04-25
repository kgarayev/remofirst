import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.chatty.core.infrastructure.settings")

application = get_asgi_application()

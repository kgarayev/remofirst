import os
import multiprocessing 
import api.chat.websocket
import api.chat.websocket.routers
from api.chat.broker.kafka_consumer import KafkaConsume
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.infrastructure.settings")

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(URLRouter(api.chat.websocket.routers.ws_patterns)),
        # Just HTTP for now. (We can add other protocols later.)
    }
)


# init kafka consumer
kafka_consumer = KafkaConsume(
    topic=os.getenv("KAFKA_TOPIC"),
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    client_id=os.getenv("KAFKA_PRODUCER_CLIENT_ID")
)


# spawn a kafka consumer in a separate process
# consumer_process = multiprocessing.Process(target=kafka_consumer.listen, daemon=True)
# consumer_process.start()
import json
import os

from api.chat.broker.kafka_producer import KafkaProduce
from django.utils.deprecation import MiddlewareMixin


class ApplyKafkaProducerMiddleware(MiddlewareMixin):

    # urls that are processed by the middleware
    WHITELISTED_URLS = ["/api/v1/chats/send-message/"]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print("CUSTOM MIDDLEWARE TRIGGERED: ", request.path)

        if request.path in self.WHITELISTED_URLS:
            # singleton instance of KafkaProduce

            # inject new attribute to request object
            request.kafka_producer = KafkaProduce(
                bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
                client_id=os.getenv("KAFKA_PRODUCER_CLIENT_ID"),
                value_serializer=lambda m: json.dumps(m).encode("ascii"),
                retries=os.getenv("KAFKA_PRODUCER_RETRIES"),
            )

            print(request.kafka_producer)

        response = self.get_response(request)

        return response


salam = ApplyKafkaProducerMiddleware()

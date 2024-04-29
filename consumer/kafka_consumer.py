import time
import websocket
import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
from models.models import MessageModel
from repository.connector import Factory
import sys

class KafkaConsume(KafkaConsumer):


    def __init__(self, topic, bootstrap_servers, client_id):
        
        super().__init__(topic, bootstrap_servers=bootstrap_servers, client_id=client_id, 
                        )
        
        self.repo = Factory(os.getenv("DB_CONN_STRING"))
    
    
    def add_to_table(self, model_cls, message):
        try:
            self.repo.create(model=model_cls(message=message.get('message_body', 'null'),
                                    sender_id=message.get('sender_user_id'),
                                    session_id_id=message.get('chat_session_id'),
                                    )
            )       
        except Exception as e:
            print(e)
    
    def send_to_ws(self, message, cookies_dict, ws_host):



        cookie = [f"{name}={value}" for name, value in cookies_dict.items()]
        cookie = "; ".join(cookie)
        
        try:
            ws = websocket.create_connection(ws_host, cookie=cookie)
            
            ws.send(json.dumps(message))

            print('WS message sent')
        except Exception as e:
            print(e)

        
    
    def listen(self, model_cls):

        while True:

            for message in self:
                
                # print(message.value.decode("utf-8"))
                try:
                    message_deserializer = json.loads(message.value.decode("utf-8"))
                except Exception as e:
                    print(e)
                    continue

                self.add_to_table(model_cls, message_deserializer)
                self.send_to_ws(message_deserializer,
                                message_deserializer.get('SENDER_CLIENT_COOKIES'),
                                f'ws://{os.getenv("DJANGO_CORE_HOST")}:8000/ws/chat/%s' % message_deserializer.get('chat_session_id'))



"""
value={
                "sender_user_id": str(request.user.id),
                "message_body": serializer.data["message"],
                "chat_session_id": str(serializer.data["session_id"]),
                "SENDER_CLIENT_COOKIES": request.COOKIES,
            }
"""
    
        


if __name__ == "__main__":

    load_dotenv('./.env', override=True)

    # print(os.getenv('DB_CONN_STRING'))

    print(os.getenv("KAFKA_BOOTSTRAP_SERVERS"))
    print(os.getenv("KAFKA_TOPIC"))

    time.sleep(10)

    kafka_consumer = KafkaConsume(
        topic=os.getenv("KAFKA_TOPIC"),
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
        client_id=os.getenv("KAFKA_PRODUCER_CLIENT_ID")
    )

    kafka_consumer.listen(MessageModel)


import json
from kafka import KafkaConsumer
from api.chat.models import Message


class KafkaConsume(KafkaConsumer):

    def __init__(self, topic, bootstrap_servers, client_id,  message_model=Message):
        
        super().__init__(topic, bootstrap_servers=bootstrap_servers, client_id=client_id, 
                        value_deserializer=lambda m: json.loads(m.decode("ascii")))
        
        self.message_model = message_model
    
    def listen(self):

        while True:

            for message in self:
                
                print(message)
                print(type(message))
                print(message.value)
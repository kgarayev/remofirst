from kafka import KafkaProducer
import json


class KafkaProduce(KafkaProducer):

    def __new__(cls, bootstrap_servers, client_id, key_serializer, value_serializer, retries):
        
        if not hasattr(cls, 'instance'):
            cls.instance = super(KafkaProduce, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, bootstrap_servers, client_id, key_serializer, value_serializer, retries):
        super().__init__(bootstrap_servers=bootstrap_servers, client_id=client_id, key_serializer=key_serializer, value_serializer=value_serializer, retries=retries)


if __name__ == "__main__":
    producer = KafkaProduce(bootstrap_servers='localhost:9092', client_id='remofirst_drf_producer', 
                            key_serializer=json.dumps, value_serializer=json.dumps, retries=3)
    


    producer.send('send_message', key='test', value='test')
    producer.flush()
    producer.close()
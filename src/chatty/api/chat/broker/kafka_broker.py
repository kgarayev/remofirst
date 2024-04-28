from kafka import KafkaProducer
import json


class KafkaProduce(KafkaProducer):

    def __new__(cls, bootstrap_servers, client_id, value_serializer, retries):
        
        # print("HEEEY", bootstrap_servers, client_id, value_serializer, retries)
        
        if not hasattr(cls, 'instance'):
            cls.instance = super(KafkaProduce, cls).__new__(cls)
        
        
        return cls.instance
    
    def __init__(self, bootstrap_servers, client_id, value_serializer, retries):
        
        super().__init__(bootstrap_servers=bootstrap_servers, client_id=client_id, value_serializer=value_serializer, retries=retries)


if __name__ == "__main__":
    producer = KafkaProduce(bootstrap_servers='localhost:29092', client_id='remofirst_drf_producer', 
                            value_serializer=lambda m: json.dumps(m).encode('ascii'), retries=3)


    meta = producer.send('send_message', {'key': 'value'})
    producer.flush()
    producer.close()

    print(meta)
    print(meta.get(timeout=10))
import json
from kafka import KafkaProducer
from common.message_type import MessageType

producer = KafkaProducer(bootstrap_servers=['172.1.1.3:9094'],
                         value_serializer=lambda m: json.dumps(m).encode('utf-8'))

data = {'message': {
    'image': None
}, 'metadata_type': MessageType.predict.name}
producer.send('IMAGES', data)
producer.flush()
print("message sent")

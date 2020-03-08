import json
from abc import ABC, abstractmethod

from generic_message import GenericMessage
from kafka import KafkaProducer
from message_type import MessageType


class GenericHandler(ABC):

    @abstractmethod
    def __init__(self, config):
        self.config = config
        self.producer = KafkaProducer(bootstrap_servers=config.get('kafka').get('bootstrap_servers'),
                                      value_serializer=lambda m: json.dumps(m).encode('utf-8'))
        self.is_prod_init = False
        self.output_topic = self.config.get('kafka').get('output_topic')

    @abstractmethod
    def handle(self, message):
        pass

    def init_handle(self, message):
        self.init_producer()
        self.handle(message)

    def write_message(self, message, output_topic=None):
        if (self.is_prod_init):
            if output_topic == None:
                output_topic = self.output_topic
            self.producer.send(output_topic, message)
            self.producer.flush()
        else:
            raise ValueError('Producer is not initialized.')

    def init_producer(self):
        self.producer = KafkaProducer(bootstrap_servers=self.config.get('kafka').get('bootstrap_servers'),
                                      value_serializer=lambda m: json.dumps(m).encode('utf-8'))
        self.is_prod_init = True

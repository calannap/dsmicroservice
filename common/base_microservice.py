import json
from abc import ABC, abstractmethod
from multiprocessing import Process

from kafka import KafkaConsumer

from generic_message import GenericMessage


class BaseMicroservice(ABC):
    def __init__(self, handlers, kafka_cfg):
        super().__init__()
        self.handlers = handlers
        #TODO da cambiare configurazione
        self.consumer = KafkaConsumer(
            kafka_cfg.get('input_topic'),
            bootstrap_servers=kafka_cfg.get('bootstrap_servers'),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=kafka_cfg.get('group_id'),
            value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    def run(self):
        for message in self.consumer:
            my_message = GenericMessage(json=message.value)
            self.is_my_message(my_message)

    def is_my_message(self, generic_message):
        if generic_message.metadata_type in self.handlers:
            self.on_message_received(generic_message)

    def on_message_received(self, generic_message):
        # self.dict.get(generic_message.metadata_type).handle(generic_message.message)
        p = Process(target=self.dict.get(generic_message.metadata_type).init_handle, args=(generic_message.message,))
        p.daemon = True
        p.start()


from yaml import safe_load

from base_microservice import BaseMicroservice
from message_type import MessageType
from model_serve import PredictHandler
from model_train import TrainHandler


class MsImageDetector(BaseMicroservice):

    def __init__(self):
        self.config = safe_load(open("..config/config.yaml"))
        self.dict = {
            MessageType.train_model.name: TrainHandler(self.config),
            MessageType.predict.name: PredictHandler(self.config)
        }
        super().__init__(self.dict, self.config.get('kafka'))


MsImageDetector().run()

from tensorflow import keras

from generic_handler import GenericHandler

class PredictHandler(GenericHandler):

    def __init__(self, config):
        super(PredictHandler, self).__init__(config)


    def handle(self, message):
        # load json and create model
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()

        json_file.close()
        loaded_model = keras.models.model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("model.h5")
        print("Loaded model from disk")

        # evaluate loaded model on test data
        loaded_model.compile(optimizer='adam',
                             loss='sparse_categorical_crossentropy',
                             metrics=['accuracy'])

        score = loaded_model.predict(image)
        return score
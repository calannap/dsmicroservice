from tensorflow import keras

from generic_handler import GenericHandler


class TrainHandler(GenericHandler):

    def __init__(self, config):
        super(TrainHandler, self).__init__(config)

    def handle(self, message):
        fashion_mnist = keras.datasets.fashion_mnist

        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

        test_images = test_images / 255.0

        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        model.fit(train_images, train_labels, epochs=10)

        test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

        print('\nTest accuracy:', test_acc)

        # serialize model to JSON
        model_json = model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        model.save_weights("model.h5")
        print("Saved model to disk")

import predict, train
import numpy as np
import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# train.train_model(train_images, train_labels, test_images, test_labels, class_names)

y = np.expand_dims(train_images[1], axis=0)
print(class_names[np.argmax(predict.predict(y))])

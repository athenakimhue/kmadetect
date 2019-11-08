#kmadetect
#By Mai Nghia

import tensorflow as tf
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers import regression
import numpy as np

PATH = "file path"


def builtModel(N_CLASSES, IMG_SIZE):
    tf.reset_default_graph()
    network = input_data(
        shape=[None, IMG_SIZE, IMG_SIZE, 1])  # 1   #ĐIền 1 nếu là ảnh đen trắng, 3 nếu là ảnh màu ở thông số cuối cùng.

    network = conv_2d(network, 32, 3, activation='relu')  # 2
    network = max_pool_2d(network, 2)  # 3

    network = conv_2d(network, 64, 3, activation='relu')
    network = max_pool_2d(network, 2)

    network = conv_2d(network, 32, 3, activation='relu')
    network = max_pool_2d(network, 2)

    network = conv_2d(network, 64, 3, activation='relu')
    network = max_pool_2d(network, 2)

    network = conv_2d(network, 32, 3, activation='relu')
    network = max_pool_2d(network, 2)

    network = conv_2d(network, 64, 3, activation='relu')
    network = max_pool_2d(network, 2)

    network = fully_connected(network, 1024, activation='relu')  # 4
    network = dropout(network, 0.8)  # 5

    network = fully_connected(network, N_CLASSES, activation='softmax')  # 6
    network = regression(network)

    model = tflearn.DNN(network)

    return model


def train(model, train_data, train_label, val_data, val_label, N_EPOCHS, pathModel):
    model.fit(train_data, train_label, n_epoch=N_EPOCHS, validation_set=(val_data, val_label), show_metric=True)
    model.save(pathModel)

    return model


def tranfer(model, train_data, train_label, val_data, val_label, N_EPOCHS, pathModel):
    model.load(pathModel)
    model.fit(train_data, train_label, n_epoch=N_EPOCHS, validation_set=(val_data, val_label), show_metric=True)
    model.save(pathModel)

    return model


def predict(model, test_data, pathModel):
    model.load(pathModel)
    test_logits = model.predict(test_data)
    
    test_logits = np.argmax(test_logits, axis=-1)

    return test_logits



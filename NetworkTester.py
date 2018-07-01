
import keras

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop


num_classes = 10
batch_size = 128
epochs = 20

# the data shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

x_train = x_train.astype("float32")
x_test = x_test.astype("float32")

x_train /= 255
x_test /= 255

print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

# conver class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


def model_create_and_run(number_of_hidden_layers, nodes_per_hidden_layer):

    # defining model
    model = Sequential()

    model.add(Dense(400, activation="relu", input_shape=(784,)))
    model.add(Dropout(0, 2))

    for _ in range(number_of_hidden_layers):

        model.add(Dense(nodes_per_hidden_layer, activation="relu"))
        model.add(Dropout(0, 2))

    model.add(Dense(num_classes, activation="softmax"))

    model.summary()

    model.compile(loss="categorical_crossentropy",
                  optimizer=RMSprop(),
                  metrics=["accuracy"])

    early_stop = keras.callbacks.EarlyStopping(monitor='val_loss',
                                               min_delta=0.001,
                                               patience=0,
                                               verbose=0,
                                               mode='auto',
                                               baseline=None)

    history = model.fit(x_train, y_train,
                        batch_size=batch_size,
                        epochs=epochs,
                        callbacks=[early_stop],
                        verbose=1,
                        validation_data=(x_test, y_test))

    score = model.evaluate(x_test, y_test, verbose=1)
    print("Test loss: ", score[0])
    print("test accuracy: ", score[1])
    print("This is the value from history and should be the same \
            as test accuracy", history["val_acc"])

    print("This is training accuracy", history["acc"])

    return [score[0], score[1]]


for num_layers in range(9, 10):
    for nodes_per in range(9, 10):
        appender = open("values.txt", "a")
        values = model_create_and_run(num_layers, nodes_per)
        appender.write(' '.join(values))
        appender.close()

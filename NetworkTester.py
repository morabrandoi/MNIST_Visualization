#mnistTut

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

batch_size = 512
num_classes = 10
epochs = 400
dummy = 0
# the data shuffled and split between train and test sets
(x_train, y_train),(x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000,784)
x_test = x_test.reshape(10000, 784)

x_train = x_train.astype("float32")
x_test = x_test.astype("float32")

x_train /= 255
x_test /= 255

print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

#conver class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


#defining model
model = Sequential()
model.add(Dense(400, activation="relu", input_shape=(784,)))
model.add(Dropout(0,2))

model.add(Dense(200, activation="relu"))
model.add(Dropout(0,2))

model.add(Dense(100, activation="relu"))
model.add(Dropout(0,2))

model.add(Dense(50, activation="relu"))
model.add(Dropout(0,2))

model.add(Dense(25, activation="relu"))
model.add(Dropout(0,2))

model.add(Dense(num_classes, activation="softmax"))

model.summary()



model.compile(loss="categorical_crossentropy",
              optimizer= RMSprop(),
              metrics=["accuracy"])


history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
model.save("./mnistNet.hdf5")

score = model.evaluate(x_test, y_test, verbose = 1)
print("Test loss: ", score[0])
print("test accuracy: ", score[1])

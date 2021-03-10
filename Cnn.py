import tensorflow as tf
import numpy as np


class Cnn:
    # adapted from Python 3 for Machine Learning by Oswald Campesato

    # This is a "vanilla" Convolutional Neural Network (CNN)

    batch_size = 32
    # how many images are put in for training at a time

    num_classes = 47
    # How many possible parts there are

    epochs = 100
    # How many times the entire data set goes through

    num_predictions = 20
    # how many prediction examples to be visible

    img_size = 50
    # width and height of the image

    # cifar10 = tf.keras.datasets.cifar10
    # This will be replaced by our data

    # The data, split between train and test sets:
    # (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    # Convert class vectors to binary class matrices
    y_train = tf.keras.utils.to_categorical(y_train, num_classes)
    y_test = tf.keras.utils.to_categorical(y_test, num_classes)

    # conv2d: size of output, stride, padding, input shape (obtained from image files itself
    #note: stride decreases by the value in both x and y
    #note: can use model.summary to see how data transforms
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(5, (3, 3), padding='same', input_shape=x_train.shape[1:]))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.Conv2D(5, (3, 3), padding='same'))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Dropout(0.25))

    # you can also duplicate the preceding code block here

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(512))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(num_classes))
    model.add(tf.keras.layers.Activation('softmax'))

    # use RMSprop optimizer to train the model
    model.compile(loss='categorical_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255

    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              validation_data=(x_test, y_test),
              shuffle=True)
    def getShape(self):
        value = "e"

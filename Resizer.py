import tensorflow as tf
import numpy as np
import imageio
import matplotlib.pyplot as plt
class Resizer:
    #This code will resize the image
    #adapted to code from Python 3 for Machine Learning by Oswald Campesato


    #set size to 50 to get the image prepared for the CNN

    #channels is one for black and white, and three for RGB

    def resizeShow(imageLocation,channels,size):
        #Resizes image and shows the original and resized images
        inp = tf.keras.layers.Input(shape=(None, None, channels))
        out = tf.keras.layers.Lambda(lambda image: tf.image.resize(image, (size, size)))(inp)

        model = tf.keras.Model(inputs=inp, outputs=out)
        model.summary()

        # read the contents of a PNG or JPG
        X = imageio.imread(imageLocation)

        out = model.predict(X[np.newaxis, ...])

        fig, axes = plt.subplots(nrows=1, ncols=2)
        axes[0].imshow(X)
        axes[1].imshow(np.int8(out[0,...]))

        plt.show()
        return out
    def resize(imageLocation,channels,size):
       #Resizes image to the desired size
        inp = tf.keras.layers.Input(shape=(None, None, 3))
        out = tf.keras.layers.Lambda(lambda image: tf.image.resize(imageLocation, (128, 128)))(inp)

        model = tf.keras.Model(inputs=inp, outputs=out)
        model.summary()

        # read the contents of a PNG or JPG
        X = imageio.imread('sample3.png')

        out = model.predict(X[np.newaxis, ...])
        return out

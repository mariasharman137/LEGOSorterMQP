import PIL
import numpy as np


class PhotoImporter:


    def photoToArray(photo_name):
        """

        :param photo_name: String containing the location of the photo
        :return NumPy array containing picture values
        """
        return np.asarray(photo_name)

    def resizeArray(array, size):
        """
        :param array: the photo array to be resized
        :param size: the size and length of the array
        :rtype: numpy array
        """
        if array.shape[0] > size and array.shape[1] > size:
            return np.resize(array, (size, size))
        else:
            print("image too small")




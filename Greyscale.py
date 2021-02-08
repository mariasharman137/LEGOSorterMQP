from PIL import Image
import numpy as np

class Greyscale:
    def ArraytoGreyscale(array):
        """

        :param photo_name: String containing the location of the photo
        :return NumPy array containing picture values
        """

        rows = array.shape[0]
        cols = array.shape[1]
        depth = 3
        gs = np.zeros((rows,cols))
        for i in range(0, rows):
            for j in range(0, cols):
                if not (array[i][j][0] == 0 and array[i][j][1] == 0 and array[i][j][2] == 0):
                    gs[i][j] = 1
        return gs
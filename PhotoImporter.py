from PIL import Image
import numpy as np
import glob
import Greyscale



class PhotoImporter:


    def photoToArray(self,photo_path):
        """

        :param photo_name: String containing the location of the photo
        :return NumPy array containing picture values
        """
        img = Image.open(photo_path)
        return np.asarray(img)

    def printArray(self,array,name):
        """
        :param array: any numpy array
        :param name: the desired filename
        :rtype: none, puts saved image in directory
        """
        im = Image.fromarray(array)
        im.save(name +".png")
    def imagesFromFolder(self,folderPath):
        image_list = []
        GS = Greyscale.Greyscale()
        for filename in glob.iglob(folderPath + '**/*.png', recursive=True):
            newImage = self.photoToArray(filename)
            image_list.append(GS.arraytoGreyscale(newImage))
        for array in image_list:
            np.delete(array,3,1)
        return image_list





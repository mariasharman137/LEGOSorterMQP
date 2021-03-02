from ColorDB import ColorDB


class ColorChoice:

    # This code will determine the color of the photo
    def chooseColor(image):
        """
        :param image: int[][][]
        :return: String: Name of the Color
        #for loop works correctly, navigates to all pixels
        #ignores pure balck pixels [0,0,0]
        #To work, images must have all of the non-lego portion filled with pure black
        """
        averageColor = [0, 0, 0]
        counter = 0
        rows = image.shape[0]
        cols = image.shape[1]
        depth = 3
        for i in range(0, rows):
            for j in range(0, cols):
                if not (image[i][j][0] == 0 and image[i][j][1] == 0 and image [i][j][2] == 0):
                    for k in range(0, depth):
                        averageColor[k] += image[i][j][k]


                    counter += 1
        if counter == 0:
            averageColor=[0, 0, 0]
        else:
            for k in range(0,len(averageColor)):
                averageColor[k] /= counter

        cdb = ColorDB()

        return cdb.getColor(averageColor)

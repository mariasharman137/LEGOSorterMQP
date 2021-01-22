


class ColorChoice:
    import numpy as np
    #This code will determine the color of the photo, and will return the color and the black and white version of the photo
    def chooseColor(image):
        averageColor = [0,0,0]
        counter = 0;
        for i in image:
            for j in image[i]:
                if image[i][j] != [0,0,0]:
                    for k in image[i][j]
                        averageColor[k] += image[i][j][k]

                    counter += 1
        for k in averageColor:
            averageColor[k] /= counter
        #TODO: Add comparisons to each color in colorsAvailable


import ColorDB


class ColorChoice:

    #This code will determine the color of the photo
    def chooseColor(self,image):
        """
        :param image: int[][][]
        :return: String: Name of the Color
        """
        averageColor = [0,0,0]
        counter = 0;
        for i in image:
            for j in image[i]:
                if image[i][j] != [0,0,0]:
                    for k in image[i][j]:
                        averageColor[k] += image[i][j][k]

                    counter += 1
        for k in averageColor:
            averageColor[k] /= counter
        return ColorDB.getColor(averageColor)



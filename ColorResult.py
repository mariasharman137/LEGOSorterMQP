class ColorResult:
    def __init__(self, color, image):
        """
        Custom type for returning color name and the image
        Intended for
        :type color: String
        :type image: Array[][][]
        """
        self.color = color
        self.image = image

class ColorDB:
    # this file contains all of the colors available
    # List of color names and values
    # list of RGB values can be found on partdata.xlsx
    def __init__(self):
        """
        contains color names and values
        """
        self.ColorDBvals = [["Dark Grey", [108, 110, 104]],
                            ["Light Grey", [201, 202, 226]],
                            ["Blue", [0, 85, 191]],
                            ["Red", [201, 26, 9]],
                            ["Tan", [228, 205, 158]],
                            ["Yellow", [242, 205, 55]],
                            ["Black", [5, 19, 29]]]

    def getColor(self,average):
        """
        :return: String, Name of the color
        :param average: int[], an r,g,b, value
        """
        score = 1000
        color = ""
        for i in range(0,len(self.ColorDBvals)):
            if self.getScore(average, self.ColorDBvals[i][1]) < score:
                color = self.ColorDBvals[i][0]
                score = self.getScore(average, self.ColorDBvals[i][1])
        return color

    def getScore(self, average, vals):
        """
        :param average: int[], average color value
        :param vals: int[], reference values for the color being checked
        :return: int, score for the color being tested
        """
        score = 0
        for j in range(0,len(vals)):
            score += abs(average[j] - vals[j])
        return score

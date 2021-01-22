class ColorDB:
    import ColorData
    # this file contains all of the colors available
    # List of color names and values
    # list of RGB values can be found on partdata.xlsx
    def __init__(self):
        self.ColorDBvals = [["Dark Grey", [108, 110, 104]],
                            ["Light Grey", [201, 202, 226]],
                            ["Blue", [0, 85, 191]],
                            ["Red", [201, 26, 9]],
                            ["Tan", [228, 205, 158]],
                            ["Yellow", [242, 205, 55]],
                            ["Black", [5, 19, 29]]]

    def getColor(self, average):
        score = 1000
        color = ""
        for i in self.ColorDBvals:
            if self.getScore(average, self.ColorDBvals[i][1]) < score:
                color = self.ColorDBvals[i][0]
        return color

    def getScore(self, average, vals):
        score = 0
        for j in vals:
            score += abs(average[j] - vals[j])

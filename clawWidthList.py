class clawWidthList:
    def __init__(self):
        self.cw = dict()
        self.addPartToCW(1,40)
        self.addPartToCW(2,50)
        self.addPartToCW(3,40)
        self.addPartToCW(4,20)
        self.addPartToCW(5,40)
        self.addPartToCW(6,20)
        self.addPartToCW(7,20)
        self.addPartToCW(8,20)
        self.addPartToCW(9,20)
        self.addPartToCW(10,30)
        self.addPartToCW(11,30)
        self.addPartToCW(12,50)
        self.addPartToCW(13,30)
    def addPartToCW(self, pocket, width):
        """ Adds an entry to the dictionary with the pocket as the key and the width for the claw to open as the value.

        Widths are the longest width +10mm
        """
        self.cw[pocket] = width

    def getWidth(self,pocket):
        return self.cw[pocket]
        

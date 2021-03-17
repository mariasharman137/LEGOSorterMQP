class Tray:
    def __init__(self):
        """
        :type height: int
        :param height Height in mm manipulator must reach to deposit part
        :type pockets: Pocket[]
        """
        self.height = 0
        self.pockets = []

    def addPocket(self, pocket):
        self.pockets.append(pocket)

    def addHeight(self, height):
        self.height = height

    def addPartToTray(self,partName):
        partName = str(partName)
        for index,item in enumerate(self.pockets, start = 0):
            print("\n")
            print("Pocket number: " +str(index))
            print("Part is:" +str(partName) )
            print("Entering Pocket Function:\n\n")
            item.addPartToPocket(partName,self.height)





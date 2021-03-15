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
        self.pockets.add(pocket)

    def addHeight(self, height):
        self.height = height

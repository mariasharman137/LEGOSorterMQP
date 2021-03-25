import Pocket


class Tray:
    def __init__(self):
        """
        :type height: int
        :param height Height in mm manipulator must reach to deposit part
        :type pockets: Pocket[]
        """
        self.height = 0
        self.pockets = []

    def intializeTray(self):
        pocket1 = Pocket.Pocket()
        pocket2 = Pocket.Pocket()
        pocket3 = Pocket.Pocket()
        pocket4 = Pocket.Pocket()
        pocket5 = Pocket.Pocket()
        pocket6 = Pocket.Pocket()
        pocket7 = Pocket.Pocket()
        pocket8 = Pocket.Pocket()
        pocket9 = Pocket.Pocket()
        pocket10 = Pocket.Pocket()
        pocket11 = Pocket.Pocket()
        pocket12 = Pocket.Pocket()
        pocket13 = Pocket.Pocket()

        # Pocket 1 Parts
        pocket1.addNewPartData("Light Grey Crank", 2)
        pocket1.addNewPartData("Black Double Pin with Axle Hole", 2)
        pocket1.addNewPartData("Light Grey Wedge Wheel / Pulley", 4)
        pocket1.addNewPartData("Light Grey 3L Pin Connector 4 Pin", 2)
        pocket1.addNewPartData("Dark Grey Liftarm L 3x5 Quarter Ellipse", 4)
        pocket1.addNewPartData("Black Pulley Tire", 4)

        # Pocket 2 Parts
        pocket2.addNewPartData("Light Grey Axle and Pin Connector Perpendicular", 20)
        pocket2.addNewPartData("Black Technic, Axle Connector 2L", 4)
        pocket2.addNewPartData("Dark Grey 2L Perpendicular 2 Pin 1 Axle Connector", 2)
        pocket2.addNewPartData("Dark Grey 3L 2 Pin 1 Axle Perpendicular Connector", 4)
        pocket2.addNewPartData("Black Technic, Axle and Pin Connector Perpendicular", 8)
        pocket2.addNewPartData("Black Technic, Axle and Pin Connector 180 degrees", 2)

        # Pocket 3 Parts
        pocket3.addPartToPocket("Light Grey 8T Gear", 4)
        pocket3.addPartToPocket("Light Grey 18T Gear", 4)
        pocket3.addPartToPocket("Light Grey 20T Gear", 2)
        pocket3.addPartToPocket("Light Grey 24T Gear", 4)
        pocket3.addPartToPocket("Light Grey 24T Gear: Crown", 2)
        pocket3.addPartToPocket("Light Grey 40T Gear", 2)
        pocket3.addPartToPocket("Black 12T Gear", 4)
        pocket3.addPartToPocket("Black 36T Gear", 2)
        pocket3.addPartToPocket("Black Worm Screw Long", 2)
        pocket3.addPartToPocket("Black Knob Wheel", 4)

        # Pocket 4 Parts
        pocket4.addPartToPocket("Red 2L Axle")
        pocket4.addPartToPocket("Black Technic Axle 4", 6)
        pocket4.addPartToPocket("Black Technic Axle 6", 4)
        pocket4.addPartToPocket("Black Technic Axle 8", 2)
        pocket4.addPartToPocket("Black Technic Axle 10", 2)
        pocket4.addPartToPocket("Black Technic Axle 12", 2)
        pocket4.addPartToPocket("Dark Grey Axle 5.5 with Stop", 2)
        pocket4.addPartToPocket("Light Grey 3L Axle", 14)
        pocket4.addPartToPocket("Light Grey 5l Axle", 8)

        # Pocket 5 Parts
        pocket5.addPartToPocket("Green 1x2 Trans Brick", 1)
        pocket5.addPartToPocket("Red 1x2 Trans Brick", 1)
        pocket5.addPartToPocket("Yellow 1x2 Trans Brick", 1)
        pocket5.addPartToPocket("Light Grey 18mm Wheel", 2)
        pocket5.addPartToPocket("Black 24mm Tire", 2)

        # Pocket 6 Parts
        pocket6.addPartToPocket("Tan Axle and Pin", 8)
        pocket6.addPartToPocket("Blue Technic Axle with Pin", 10)
        pocket6.addPartToPocket("Black 3L Pin with Bush" ,8)

        # Pocket 7 Parts
        pocket7.addPartToPocket("Black 3L Pin", 36)

        # Pocket 8 Parts
        pocket8.addPartToPocket("Black Technic Pin 2L", 60)

        # Pocket 9 Parts
        pocket9.addPartToPocket("Yellow 1/2 Bush", 10)
        pocket9.addPartToPocket("Light Grey Bush", 10)

        # Pocket 10 Parts
        pocket10.addPartToPocket("Liftarm Thick 1x3", 10)
        pocket10.addPartToPocket("Liftarm Thick 1x5", 4)
        pocket10.addPartToPocket("Liftarm Thick 1x7", 4)
        pocket10.addPartToPocket("Liftarm Thick 1x9", 6)
        pocket10.addPartToPocket("Liftarm Thick 1x11", 2)
        pocket10.addPartToPocket("Liftarm Thick 1x13", 2)
        pocket10.addPartToPocket("Liftarm Thick 1x15", 4)

        # Pocket 11 Parts
        pocket11.addPartToPocket("Dark Grey Liftarm Bent 6-4", 4)
        pocket11.addPartToPocket("Dark Grey Liftarm Bent 7-4-3", 4)
        pocket11.addPartToPocket("Dark Grey Liftarm L 2x4", 4)
        pocket11.addPartToPocket("Dark Grey Liftawm L 3x5", 8)

        # Pocket 12 Parts
        pocket12.addPartToPocket("Dark Grey 1x2 Tile", 2)
        pocket12.addPartToPocket("Light Grey Brick 1x2", 8)
        pocket12.addPartToPocket("Light Grey Brick 2x2", 4)
        pocket12.addPartToPocket("Light Grey Plate 1x2", 4)
        pocket12.addPartToPocket("Light Grey Plate 1x4", 4)
        pocket12.addPartToPocket("Light Grey 2x4 Plate 3 Holes", 2)
        pocket12.addPartToPocket("Light Grey 2x6 Plate 5 Holes", 2)
        pocket12.addPartToPocket("Light Grey 2x8 Plate 7 Holes", 2)

        # Pocket 13 Parts
        pocket13.addPartToPocket("Dark Grey 1x2 Brick with Axle hole", 2)
        pocket13.addPartToPocket("Light Grey Brick 1x2 with Round Hole", 4)
        pocket13.addPartToPocket("Light Grey Brick 1x4 with Round Holes", 4)
        pocket13.addPartToPocket("Light Grey Brick 1x6 with Round Holes", 4)
        pocket13.addPartToPocket("Light Grey Brick 1x8 with Round Holes", 4)
        pocket13.addPartToPocket("Light Grey Brick 1x16 with Round Holes", 4)

        self.addPocket(pocket1)
        self.addPocket(pocket2)
        self.addPocket(pocket3)
        self.addPocket(pocket4)
        self.addPocket(pocket5)
        self.addPocket(pocket6)
        self.addPocket(pocket7)
        self.addPocket(pocket8)
        self.addPocket(pocket9)
        self.addPocket(pocket10)
        self.addPocket(pocket11)
        self.addPocket(pocket12)
        self.addPocket(pocket13)




    def addPocket(self, pocket):
        self.pockets.append(pocket)

    def addHeight(self, height):
        self.height = height

    def addPartToTray(self, partName):
        partName = str(partName)
        for index, item in enumerate(self.pockets, start=0):
            print("\n")
            print("Pocket number: " + str(index))
            print("Part is:" + str(partName))
            print("Entering Pocket Function:\n\n")
            sum1 = item.partsSum()
            item.addPartToPocket(partName, self.height)
            sum2 = item.partsSum()
            if sum1 != sum2:
                return

    def partsSum(self):
        sum = 0
        for item in self.pockets:
            sum = sum + item.partsSum()
        return sum

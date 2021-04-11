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
        #TODO: Flip x
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

        #Locations will go with its parts once calculated
        #Locations assume 0,0 is top left of Pocketnumbers.png/tray mechanism
        # Pocket 1 Parts
        pocket1.addNewPartData("Light Grey Crank", 2)
        pocket1.addNewPartData("Black Double Pin with Axle Hole", 2)
        pocket1.addNewPartData("Light Grey Wedge Wheel / Pulley", 4)
        pocket1.addNewPartData("Light Grey 3L Pin Connector 4 Pin", 2)
        pocket1.addNewPartData("Dark Grey Liftarm L 3x5 Quarter Ellipse", 4)
        pocket1.addNewPartData("Black Pulley Tire", 4)
        pocket1.setLocation(230,80)

        # Pocket 2 Parts
        pocket2.addNewPartData("Light Grey Axle and Pin Connector Perpendicular", 20)
        pocket2.addNewPartData("Black Technic, Axle Connector 2L", 4)
        pocket2.addNewPartData("Dark Grey 2L Perpendicular 2 Pin 1 Axle Connector", 2)
        pocket2.addNewPartData("Dark Grey 3L 2 Pin 1 Axle Perpendicular Connector", 4)
        pocket2.addNewPartData("Black Technic, Axle and Pin Connector Perpendicular", 8)
        pocket2.addNewPartData("Black Technic, Axle and Pin Connector 180 degrees", 2)
        pocket2.setLocation(155,80)

        # Pocket 3 Parts
        pocket3.addNewPartData("Light Grey 8T Gear", 4)
        pocket3.addNewPartData("Light Grey 18T Gear", 4)
        pocket3.addNewPartData("Light Grey 20T Gear", 2)
        pocket3.addNewPartData("Light Grey 24T Gear", 4)
        pocket3.addNewPartData("Light Grey 24T Gear: Crown", 2)
        pocket3.addNewPartData("Light Grey 40T Gear", 2)
        pocket3.addNewPartData("Black 12T Gear", 4)
        pocket3.addNewPartData("Black 36T Gear", 2)
        pocket3.addNewPartData("Black Worm Screw Long", 2)
        pocket3.addNewPartData("Black Knob Wheel", 4)
        pocket3.setLocation(80, 80)

        # Pocket 4 Parts
        pocket4.addNewPartData("Red 2L Axle",8)
        pocket4.addNewPartData("Black Technic Axle 4", 6)
        pocket4.addNewPartData("Black Technic Axle 6", 4)
        pocket4.addNewPartData("Black Technic Axle 8", 2)
        pocket4.addNewPartData("Black Technic Axle 10", 2)
        pocket4.addNewPartData("Black Technic Axle 12", 2)
        pocket4.addNewPartData("Dark Grey Axle 5.5 with Stop", 2)
        pocket4.addNewPartData("Light Grey 3L Axle", 14)
        pocket4.addNewPartData("Light Grey 5l Axle", 8)
        pocket4.setLocation(200, 150)

        # Pocket 5 Parts
        pocket5.addNewPartData("Green 1x2 Trans Brick", 1)
        pocket5.addNewPartData("Red 1x2 Trans Brick", 1)
        pocket5.addNewPartData("Yellow 1x2 Trans Brick", 1)
        pocket5.addNewPartData("Light Grey 18mm Wheel", 2)
        pocket5.addNewPartData("Black 24mm Tire", 2)
        pocket5.setLocation(200,190)

        # Pocket 6 Parts
        pocket6.addNewPartData("Tan Axle and Pin", 8)
        pocket6.addNewPartData("Blue Technic Axle with Pin", 10)
        pocket6.addNewPartData("Black 3L Pin with Bush" ,8)
        pocket6.setLocation(130,135)

        # Pocket 7 Parts
        pocket7.addNewPartData("Black 3L Pin", 36)
        pocket7.setLocation(130, 185)

        # Pocket 8 Parts
        pocket8.addNewPartData("Black Technic Pin 2L", 60)
        pocket8.setLocation(70,150)

        # Pocket 9 Parts
        pocket9.addNewPartData("Yellow 1/2 Bush", 10)
        pocket9.addNewPartData("Light Grey Bush", 10)
        pocket9.setLocation(70,190)

        # Pocket 10 Parts
        pocket10.addNewPartData("Liftarm Thick 1x3", 10)
        pocket10.addNewPartData("Liftarm Thick 1x5", 4)
        pocket10.addNewPartData("Liftarm Thick 1x7", 4)
        pocket10.addNewPartData("Liftarm Thick 1x9", 6)
        pocket10.addNewPartData("Liftarm Thick 1x11", 2)
        pocket10.addNewPartData("Liftarm Thick 1x13", 2)
        pocket10.addNewPartData("Liftarm Thick 1x15", 4)
        pocket10.setLocation(200,255)

        # Pocket 11 Parts
        pocket11.addNewPartData("Dark Grey Liftarm Bent 6-4", 4)
        pocket11.addNewPartData("Dark Grey Liftarm Bent 7-4-3", 4)
        pocket11.addNewPartData("Dark Grey Liftarm L 2x4", 4)
        pocket11.addNewPartData("Dark Grey Liftawm L 3x5", 8)
        pocket11.setLocation(80,255)

        # Pocket 12 Parts
        pocket12.addNewPartData("Dark Grey 1x2 Tile", 2)
        pocket12.addNewPartData("Light Grey Brick 1x2", 8)
        pocket12.addNewPartData("Light Grey Brick 2x2", 4)
        pocket12.addNewPartData("Light Grey Plate 1x2", 4)
        pocket12.addNewPartData("Light Grey Plate 1x4", 4)
        pocket12.addNewPartData("Light Grey 2x4 Plate 3 Holes", 2)
        pocket12.addNewPartData("Light Grey 2x6 Plate 5 Holes", 2)
        pocket12.addNewPartData("Light Grey 2x8 Plate 7 Holes", 2)
        pocket12.setLocation(200,340)

        # Pocket 13 Parts
        pocket13.addNewPartData("Dark Grey 1x2 Brick with Axle hole", 2)
        pocket13.addNewPartData("Light Grey Brick 1x2 with Round Hole", 4)
        pocket13.addNewPartData("Light Grey Brick 1x4 with Round Holes", 4)
        pocket13.addNewPartData("Light Grey Brick 1x6 with Round Holes", 4)
        pocket13.addNewPartData("Light Grey Brick 1x8 with Round Holes", 4)
        pocket13.addNewPartData("Light Grey Brick 1x16 with Round Holes", 4)
        pocket13.setLocation(80,340)

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

    def addPartToTray(self, partName, pocket):
        sum1 = self.pockets[pocket].partsSum()
        self.pockets[pocket].addPartToPocket(partName, self.height)
        sum2 = self.pockets[pocket].partsSum()
        if sum1 != sum2:
            return

    def partsSum(self):
        sum = 0
        for item in self.pockets:
            sum = sum + item.partsSum()
        return sum

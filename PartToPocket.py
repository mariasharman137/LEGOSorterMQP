class PartToPocket:
    def __init__(self):
        self.ptp = dict()
        self.addPartToPTP("Light Grey Crank", 1)
        self.addPartToPTP("Black Double Pin with Axle Hole", 1)
        self.addPartToPTP("Light Grey Wedge Wheel / Pulley", 1)
        self.addPartToPTP("Light Grey 3L Pin Connector 4 Pin", 1)
        self.addPartToPTP("Dark Grey Liftarm L 3x5 Quarter Ellipse", 1)
        self.addPartToPTP("Black Pulley Tire", 1)

        self.addPartToPTP("Light Grey Axle and Pin Connector Perpendicular", 2)
        self.addPartToPTP("Black Technic, Axle Connector 2L", 2)
        self.addPartToPTP("Dark Grey 2L Perpendicular 2 Pin 1 Axle Connector", 2)
        self.addPartToPTP("Dark Grey 3L 2 Pin 1 Axle Perpendicular Connector", 2)
        self.addPartToPTP("Black Technic, Axle and Pin Connector Perpendicular", 2)
        self.addPartToPTP("Black Technic, Axle and Pin Connector 180 degrees", 2)

        self.addPartToPTP("Light Grey 8T Gear", 3)
        self.addPartToPTP("Light Grey 18T Gear", 3)
        self.addPartToPTP("Light Grey 20T Gear", 3)
        self.addPartToPTP("Light Grey 24T Gear", 3)
        self.addPartToPTP("Light Grey 24T Gear: Crown", 3)
        self.addPartToPTP("Light Grey 40T Gear", 3)
        self.addPartToPTP("Black 12T Gear", 3)
        self.addPartToPTP("Black 36T Gear", 3)
        self.addPartToPTP("Black Worm Screw Long", 3)
        self.addPartToPTP("Black Knob Wheel", 3)

        self.addPartToPTP("Red 2L Axle", 4)
        self.addPartToPTP("Black Technic Axle 4", 4)
        self.addPartToPTP("Black Technic Axle 6", 4)
        self.addPartToPTP("Black Technic Axle 8", 4)
        self.addPartToPTP("Black Technic Axle 10", 4)
        self.addPartToPTP("Black Technic Axle 12", 4)
        self.addPartToPTP("Dark Grey Axle 5.5 with Stop", 4)
        self.addPartToPTP("Light Grey 3L Axle", 4)
        self.addPartToPTP("Light Grey 5l Axle", 4)

        self.addPartToPTP("Green 1x2 Trans Brick", 5)
        self.addPartToPTP("Red 1x2 Trans Brick", 5)
        self.addPartToPTP("Yellow 1x2 Trans Brick", 5)
        self.addPartToPTP("Light Grey 18mm Wheel", 5)
        self.addPartToPTP("Black 24mm Tire", 5)

        self.addPartToPTP("Tan Axle and Pin", 6)
        self.addPartToPTP("Blue Technic Axle with Pin", 6)
        self.addPartToPTP("Black 3L Pin with Bush", 6)

        self.addPartToPTP("Black 3L Pin", 7)

        self.addPartToPTP("Black Technic Pin 2L", 8)

        self.addPartToPTP("Yellow 1/2 Bush", 9)
        self.addPartToPTP("Light Grey Bush", 9)

        self.addPartToPTP("Liftarm Thick 1x3", 10)
        self.addPartToPTP("Liftarm Thick 1x5", 10)
        self.addPartToPTP("Liftarm Thick 1x7", 10)
        self.addPartToPTP("Liftarm Thick 1x9", 10)
        self.addPartToPTP("Liftarm Thick 1x11", 10)
        self.addPartToPTP("Liftarm Thick 1x13", 10)
        self.addPartToPTP("Liftarm Thick 1x15", 10)

        self.addPartToPTP("Dark Grey Liftarm Bent 6-4", 11)
        self.addPartToPTP("Dark Grey Liftarm Bent 7-4-3", 11)
        self.addPartToPTP("Dark Grey Liftarm L 2x4", 11)
        self.addPartToPTP("Dark Grey Liftawm L 3x5", 11)

        self.addPartToPTP("Dark Grey 1x2 Tile", 12)
        self.addPartToPTP("Light Grey Brick 1x2", 12)
        self.addPartToPTP("Light Grey Brick 2x2", 12)
        self.addPartToPTP("Light Grey Plate 1x2", 12)
        self.addPartToPTP("Light Grey Plate 1x4", 12)
        self.addPartToPTP("Light Grey 2x4 Plate 3 Holes", 12)
        self.addPartToPTP("Light Grey 2x6 Plate 5 Holes", 12)
        self.addPartToPTP("Light Grey 2x8 Plate 7 Holes", 12)

        self.addPartToPTP("Dark Grey 1x2 Brick with Axle hole", 13)
        self.addPartToPTP("Light Grey Brick 1x2 with Round Hole", 13)
        self.addPartToPTP("Light Grey Brick 1x4 with Round Holes", 13)
        self.addPartToPTP("Light Grey Brick 1x6 with Round Holes", 13)
        self.addPartToPTP("Light Grey Brick 1x8 with Round Holes", 13)
        self.addPartToPTP("Light Grey Brick 1x16 with Round Holes", 13)

    def addPartToPTP(self, name, pocket):
        """ Adds an entry to the dictionary with name as key and value as pocket
        :param color: String
        :param shape: String
        :param name: String
        :return: none
        """
        key = name

        self.ptp[key] = pocket

    def getPocket(self,name):
        return self.ptp[name]

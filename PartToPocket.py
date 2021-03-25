class PartToPocket:
    def __init__(self):
        self.ptp = dict()
        self.addPartToPTP("Light Grey Crank", 0)
        self.addPartToPTP("Black Double Pin with Axle Hole", 0)
        self.addPartToPTP("Light Grey Wedge Wheel / Pulley", 0)
        self.addPartToPTP("Light Grey 3L Pin Connector 4 Pin", 0)
        self.addPartToPTP("Dark Grey Liftarm L 3x5 Quarter Ellipse", 0)
        self.addPartToPTP("Black Pulley Tire", 0)

        self.addPartToPTP("Light Grey Axle and Pin Connector Perpendicular", 1)
        self.addPartToPTP("Black Technic, Axle Connector 2L", 1)
        self.addPartToPTP("Dark Grey 2L Perpendicular 1 Pin 1 Axle Connector", 1)
        self.addPartToPTP("Dark Grey 3L 1 Pin 1 Axle Perpendicular Connector", 1)
        self.addPartToPTP("Black Technic, Axle and Pin Connector Perpendicular", 1)
        self.addPartToPTP("Black Technic, Axle and Pin Connector 180 degrees", 1)

        self.addPartToPTP("Light Grey 8T Gear", 2)
        self.addPartToPTP("Light Grey 18T Gear", 2)
        self.addPartToPTP("Light Grey 20T Gear", 2)
        self.addPartToPTP("Light Grey 24T Gear", 2)
        self.addPartToPTP("Light Grey 24T Gear: Crown", 2)
        self.addPartToPTP("Light Grey 40T Gear", 2)
        self.addPartToPTP("Black 12T Gear", 2)
        self.addPartToPTP("Black 36T Gear", 2)
        self.addPartToPTP("Black Worm Screw Long", 2)
        self.addPartToPTP("Black Knob Wheel", 2)

        self.addPartToPTP("Red 2L Axle", 3)
        self.addPartToPTP("Black Technic Axle 4", 3)
        self.addPartToPTP("Black Technic Axle 6", 3)
        self.addPartToPTP("Black Technic Axle 8", 3)
        self.addPartToPTP("Black Technic Axle 10", 3)
        self.addPartToPTP("Black Technic Axle 12", 3)
        self.addPartToPTP("Dark Grey Axle 5.5 with Stop", 3)
        self.addPartToPTP("Light Grey 3L Axle", 3)
        self.addPartToPTP("Light Grey 5l Axle", 3)

        self.addPartToPTP("Green 1x2 Trans Brick", 4)
        self.addPartToPTP("Red 1x2 Trans Brick", 4)
        self.addPartToPTP("Yellow 1x2 Trans Brick", 4)
        self.addPartToPTP("Light Grey 18mm Wheel", 4)
        self.addPartToPTP("Black 24mm Tire", 4)

        self.addPartToPTP("Tan Axle and Pin", 5)
        self.addPartToPTP("Blue Technic Axle with Pin", 5)
        self.addPartToPTP("Black 3L Pin with Bush", 5)

        self.addPartToPTP("Black 3L Pin", 6)

        self.addPartToPTP("Black Technic Pin 2L", 7)

        self.addPartToPTP("Yellow 1/2 Bush", 8)
        self.addPartToPTP("Light Grey Bush", 8)

        self.addPartToPTP("Liftarm Thick 1x3", 9)
        self.addPartToPTP("Liftarm Thick 1x5", 9)
        self.addPartToPTP("Liftarm Thick 1x7", 9)
        self.addPartToPTP("Liftarm Thick 1x9", 9)
        self.addPartToPTP("Liftarm Thick 1x11", 9)
        self.addPartToPTP("Liftarm Thick 1x13", 9)
        self.addPartToPTP("Liftarm Thick 1x15", 9)

        self.addPartToPTP("Dark Grey Liftarm Bent 6-4", 10)
        self.addPartToPTP("Dark Grey Liftarm Bent 7-4-3", 10)
        self.addPartToPTP("Dark Grey Liftarm L 2x4", 10)
        self.addPartToPTP("Dark Grey Liftawm L 3x5", 10)

        self.addPartToPTP("Dark Grey 1x2 Tile", 11)
        self.addPartToPTP("Light Grey Brick 1x2", 11)
        self.addPartToPTP("Light Grey Brick 2x2", 11)
        self.addPartToPTP("Light Grey Plate 1x2", 11)
        self.addPartToPTP("Light Grey Plate 1x4", 11)
        self.addPartToPTP("Light Grey 2x4 Plate 3 Holes", 11)
        self.addPartToPTP("Light Grey 2x6 Plate 5 Holes", 11)
        self.addPartToPTP("Light Grey 2x8 Plate 7 Holes", 11)

        self.addPartToPTP("Dark Grey 1x2 Brick with Axle hole", 12)
        self.addPartToPTP("Light Grey Brick 1x2 with Round Hole", 12)
        self.addPartToPTP("Light Grey Brick 1x4 with Round Holes", 12)
        self.addPartToPTP("Light Grey Brick 1x6 with Round Holes", 12)
        self.addPartToPTP("Light Grey Brick 1x8 with Round Holes", 12)
        self.addPartToPTP("Light Grey Brick 1x16 with Round Holes", 12)

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

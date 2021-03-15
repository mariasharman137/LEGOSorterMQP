
class PartDatabase:
    """
    This contains a dictionary which contains all parts in the set.
    If it isnt in the dictionary, it is not a valid part in this set
    If it is, the name of the part is returned

    """
    def __init__(self):
        self.pdb = dict()
        self.addPartToDB("Black", "3705", "Technic Axle 4")
        self.addPartToDB("Black", "3706", "Technic Axle 6")
        self.addPartToDB("Black", "3707", "Technic Axle 8")
        self.addPartToDB("Black", "3737", "Technic Axle 10")
        self.addPartToDB("Black", "3708", "Technic Axle 12")
        self.addPartToDB("Black", "32034", "Technic, Axle and Pin Connector 180 degrees")
        self.addPartToDB("Black", "32184", "Technic, Axle and Pin Connector Perpendicular")
        self.addPartToDB("Black", "36538b", "Technic, Axle Connector 2L")
        self.addPartToDB("Black", "32270", "12 Tooth Gear")
        self.addPartToDB("Black", "32498", "36 Tooth Gear")
        self.addPartToDB("Black", "4716", "BWorm Screw Long")
        self.addPartToDB("Black", "32072", "Knob Wheel")
        self.addPartToDB("Black", "6558", "3L Pin")
        self.addPartToDB("Black", "32054", "3L Pin with Bush")
        self.addPartToDB("Black", "32138", "Double Pin with Axle Hole")
        self.addPartToDB("Black", "2780", "Technic Pin 2L")
        self.addPartToDB("Black", "2815", "Pulley Tire")
        self.addPartToDB("Blue", "43093", "Technic Axle with Pin")
        self.addPartToDB("Dark Grey", "32209", "Axle 5.5 with Stop")
        self.addPartToDB("Dark Grey", "32291", "Perpendicular 2 Pin 1 Axle connector")
        self.addPartToDB("Dark Grey", "32064b", "1x2 Brick with Axle hole")
        self.addPartToDB("Dark Grey", "32523", "Liftarm Thick 1x3")
        self.addPartToDB("Dark Grey", "32316", "Liftarm Thick 1x5")
        self.addPartToDB("Dark Grey", "32524", "Liftarm Thick 1x7")
        self.addPartToDB("Dark Grey", "40490", "Liftarm Thick 1x9")
        self.addPartToDB("Dark Grey", "32525", "Liftarm Thick 1x11")
        self.addPartToDB("Dark Grey", "41239", "Liftarm Thick 1x13")
        self.addPartToDB("Dark Grey", "32278", "Liftarm Thick 1x15")
        self.addPartToDB("Dark Grey", "6629", "Liftarm Bent 6-4")
        self.addPartToDB("Dark Grey", "32009", "Liftarm Bent 7-4-3")
        self.addPartToDB("Dark Grey", "32140", "Liftarm L 2x4")
        self.addPartToDB("Dark Grey", "32526", "Liftarm L 3x5")
        self.addPartToDB("Dark Grey", "32250", "Liftarm L 3x5 Quarter Elipse")
        self.addPartToDB("Dark Grey", "3069b", "1x2 Tile")
        self.addPartToDB("Light Grey", "3004", "Brick 1x2")
        self.addPartToDB("Light Grey", "3003", "Brick 2x2")
        self.addPartToDB("Light Grey", "3023", "Plate 1x2")
        self.addPartToDB("Light Grey", "3710", "Plate 1x4")
        self.addPartToDB("Light Grey", "4185", "Wedge Wheel / Pulley")
        self.addPartToDB("Light Grey", "4519", "3L Axle")
        self.addPartToDB("Light Grey", "32073", "5L Axle")
        self.addPartToDB("Light Grey", "6536", "Axle and Pin Connector Perpendicular")
        self.addPartToDB("Light Grey", "3700", "Brick 1x2 with Round Hole")
        self.addPartToDB("Light Grey", "3701", "Brick 1x4 with Round Holes")
        self.addPartToDB("Light Grey", "3894", "Brick 1x6 with Round Holes")
        self.addPartToDB("Light Grey", "3702", "Brick 1x8 with Round Holes")
        self.addPartToDB("Light Grey", "3703", "Brick 1x16 with Round Holes")
        self.addPartToDB("Light Grey", "3713", "Bush")
        self.addPartToDB("Light Grey", "3647", "8T Gear")
        self.addPartToDB("Light Grey", "4019", "16T Gear")
        self.addPartToDB("Light Grey", "32269", "20T Gear")
        self.addPartToDB("Light Grey", "3648", "24T Gear")
        self.addPartToDB("Light Grey", "3650b", "24T Gear: Crown")
        self.addPartToDB("Light Grey", "3649", "40T Gear")
        self.addPartToDB("Light Grey", "33299", "Crank")
        self.addPartToDB("Light Grey", "48989", "3L Pin Connector 4 Pin")
        self.addPartToDB("Light Grey", "3709b", "2x4 Plate 3 Holes")
        self.addPartToDB("Light Grey", "32001", "2x6 Plate 5 Holes")
        self.addPartToDB("Light Grey", "3738", "2x8 Plate 7 Holes")
        self.addPartToDB("Red", "3709b", "2L Axle")
        self.addPartToDB("Tan", "3709b", "Axle and Pin")
        self.addPartToDB("Light Grey", "3709b", "2x4 Plate 3 Holes")
        self.addPartToDB("Green", "3065", "1x2 Trans Brick")
        self.addPartToDB("Red", "3065", "1x2 Trans Brick")
        self.addPartToDB("Yellow", "3065", "1x2 Trans Brick")
        self.addPartToDB("Yellow", "4265c", "1/2 Bush")
















    def addPartToDB(self, color, shape, name):
        """ Adds an entry to the dictionary with color and shape concatenated
         to make the key, and the value is the name of the part
        :param color: String
        :param shape: String
        :param name: String
        :return: none
        """
        key = color + shape
        #dict value now has color so it adds itself to the value with the part name
        self.pdb[key] = color + name
    def removePartFromDB(self,color,shape):
        """
        :param color: String
        :param shape: String
        :return none
        """
        key = color+shape
        del self.pdb[key]

    def checkIfPart(self, color, shape):
        key = color + shape
        if key in self.pdb.keys():
            return True
        else:
            return False

    def returnPart(self, color, shape):
        """ gives the name of the part from the dictionary given a color and string

        :param color: String
        :param shape: String
        :rtype String
        :return The name of the part
        """
        return self.pdb[color + shape]


import PartDatabase
import Motors


class TrayDB:
    partNotFound = True
    #Tray 0 is the top tray
    def __init__(self):
        self.trays = []
        self.PDb = PartDatabase.PartDatabase()

        #Location for where unknown parts go
        self.UnknownX = 100
        self.UnknownY = 100
        self.UnknownZ = 100
        self.Unknown = [self.UnknownX,self.UnknownY,self.UnknownZ]

        #Location for Overflow parts
        self.OverflowX = 200
        self.OverflowY = 200
        self.OverflowZ = 200
        self.Overflow = [self.OverflowX,self.OverflowY, self.OverflowZ]

        self.motors = Motors.Motors()

        #TODO: Possibly add something that can check if a tray is tottaly full
        # This would allow for trays, and maybe pockets, to be skipped




    def addTray(self, tray):
        """This function adds a tray to the TrayDB

        :param tray: Tray
        :return: none
        """
        self.trays.append(tray)

    def removeTray(self, index):
        """This function removes a Tray from TrayDB
        :param index: the index of the tray to be removed
        :return: none
        """
        del self.trays[index]

    def setHeights(self, x0, x1):
        """

        :type x0: int, distance from top to first tray, mm
        :type x1 int, distance between trays, mm
        :return none
        """
        for index,item in enumerate(self.trays, start = 0):
            item.addHeight(x0 + x1 * index)

    def placePart(self, color,shape):
        """ This function finds where there is room for the part, starting from the top tray and moving down

        :param name: String, the name of the part being placed
        :return: none
        """
        color = str(color)
        shape = str(shape)

        if self.PDb.checkIfPart(color, shape):
            for index,item in enumerate(self.trays, start = 0):
                print("Item being tested is: " + str(self.PDb.returnPart(color,shape)))
                print("Tray #" + str(index) )
                sum1 = item.partsSum()
                item.addPartToTray(self.PDb.returnPart(color,shape))
                sum2 = item.partsSum()
                if sum1 != sum2:
                    return
                #Quick note: return with no value is used to end a function immeadiately.
                # It is used in this loop to ensure only a single piece is added


            print("Tray DB has too many of this item. Sending item to Overflow")
            self.motors.goTo(self.Overflow)
            return
        else:
            print("Part is Unknown. Sending item to Unknown.")
            self.motors.goTo(self.Unknown)
            return

    def partsSum(self):
        sum = 0
        for item in self.trays:
            sum = sum +item.partsSum()
        return sum


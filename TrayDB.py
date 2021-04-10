import PartDatabase
import Motors
import Tray
import PartToPocket


class TrayDB:
    partNotFound = True
    #Tray 0 is the top tray
    def __init__(self,number):
        self.trays = []
        self.PDb = PartDatabase.PartDatabase()
        self.ptp = PartToPocket.PartToPocket()

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

        i = 0
        while i < number:
            tray = Tray.Tray()
            self.addTray(tray)
            i = i + 1
        for tray in self.trays:
            tray.intializeTray()

        self.setHeights(0,65)








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
            partName = (self.PDb.returnPart(color, shape))
            partPocket = self.ptp.getPocket(partName)
            for index,item in enumerate(self.trays, start = 0):
                #print("Item being tested is: " + str(self.PDb.returnPart(color,shape)))

                sum1 = item.partsSum()
                item.addPartToTray(self.PDb.returnPart(color,shape),partPocket)
                sum2 = item.partsSum()
                if sum1 != sum2:
                    print("This item was placed in: Tray #" + str(index))
                    print("\n\n\n\n\n")
                    return
                #Quick note: return with no value is used to end a function immeadiately.
                # It is used in this loop to ensure only a single piece is added


            print("Tray DB has too many of this item. Sending item to Overflow")
            self.motors.goTo(self.Overflow)
            print("\n\n\n\n\n")
            return
        else:
            print("Part is Unknown. Sending item to Unknown.")
            self.motors.goTo(self.Unknown)
            print("\n\n\n\n\n")
            return

    def partsSum(self):
        sum = 0
        for item in self.trays:
            sum = sum +item.partsSum()
        return sum


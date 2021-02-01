import PartDatabase


class TrayDB:
    #Tray 0 is the top tray
    def __init__(self):
        trays = []

    def addTray(self, tray):
        """This function adds a tray to the TrayDB

        :param tray: Tray
        :return: none
        """
        self.trays.add(tray)

    def removeTray(self, index):
        """This function removes a Tray from TrayDB
        :param index: the index of the tray to be removed
        :return: none
        """
        del self.trays[index]

    def setHeights(self, x0, x1):
        """

        :type x0: int, distance from floor to first tray, mm
        :type x1 int, distance between trays, mm
        :return none
        """
        for i in self.trays:
            self.trays[i].addHeight(x0 + x1 * i)

    def placePart(self, name):
        """ This function finds where there is room for the part, starting from the top tray and moving down

        :param name: String, the name of the part being placed
        :return: none
        """
        # this flag turns False once the part had been placed
        iterator = True
        # This Flag becomes true if the part cannot be placed because the pocket is full. Is reset if the part is placed.
        full = False
        if PartDatabase.checkIfPart(name, ""):
            while iterator == True:
                for i in self.trays:
                    for j in self.trays.pockets:
                        for k in self.trays.pockets.currParts:
                            if self.trays[i].pockets[j].currParts[k].partName == name:
                                if self.trays[i].pockets[j].currParts[k].maxNum > self.trays[i].pockets[j].currParts[
                                    k].currNum:
                                    self.trays[i].pockets[j].currParts[k].currNum += 1
                                    full = False
                                    # goTo(self.trays[i].pockets[j].location.x,self.trays[i].pockets[j].location.y,trays[i].height)
                                    iterator = False
                                else:
                                    full = True
            # if full:
            # goto(LocationForOverflow)
        # else:
        # goTo(LocationForUnknown)

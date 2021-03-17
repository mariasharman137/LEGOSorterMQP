import Location
import NumberOfPart
import Motors
import TrayDB

class Pocket:
    partNotFound = True
    def __init__(self):
        """
        :type maxParts: NumberOfPart[]
        :type currParts: NumberOfPart[]
        :type location: Location
        """
        self.location = Location.Location()
        self.maxParts = []
        self.currParts = []
        self.motors = Motors.Motors()

        self.isDone = False


    def setLocation(self,x,y):
        self.location.addx(x)
        self.location.addy(y)

    def addNewPartData(self,partName,maxAmt):
        NoPM = NumberOfPart.NumberOfPart(maxAmt,str(partName))
        NoPC = NumberOfPart.NumberOfPart(0,str(partName))
        self.maxParts.append(NoPM)
        self.currParts.append(NoPC)

    def isPartInPocket(self,partName):
        partName = str(partName)
        for item in self.maxParts:
            #print("Checking if part in pocket:")
            #print(item.partName)
            if item.partName == partName:
                #print("Part found in Pocket:")
                #print(item.partName)
                #print("End of iPIP Loop")
                return True

        return False

    def canAddPartToPocket(self,partName):
        partName = str(partName)
        for index,item in enumerate(self.maxParts, start = 0):
            if item.partName == partName:
                maxAmt = item.num
                #print("Max:")
                #print(item.num)
                #print("Part Name:")
                #print(item.partName)
                #print("Item index is:")
                #print(index)
                currentAmt = self.currParts[index].num
                #print ("curr:")
                #print(currentAmt)
                if currentAmt + 1 <= maxAmt:
                    return True
                else:
                    return False

    def addPartToPocket(self,partName,height):
        if not self.isDone:
            if self.isPartInPocket(partName) and self.canAddPartToPocket(partName):
                print("Is Part in Pocket?")
                print(self.isPartInPocket(partName))
                print("Can this part be added to this pocket?")
                print(self.canAddPartToPocket(partName))
                for index,item in enumerate(self.maxParts, start = 0):
                    print("Item being tested is:" + str(self.maxParts[index].partName)+"\n")
                    if item.partName == partName:
                        self.currParts[index].num = self.currParts[index].num + 1
                        print("Part added is:" + str(self.currParts[index].partName))
                        print("Amount is " + str(self.currParts[index].num))
                        destination = [self.location.x, self.location.y, height]
                        self.motors.goTo(destination)
                        self.isDone = True

                        return
            else:
                print("Part does not belong in this pocket\n\n")
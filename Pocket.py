import Location
import NumberOfPart
import Motors
import TrayDB


class Pocket:
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
        self.name = 0


    def setLocation(self, x, y):
        self.location.addx(x)
        self.location.addy(y)

    def addNewPartData(self, partName, maxAmt):
        NoPM = NumberOfPart.NumberOfPart(maxAmt, str(partName))
        NoPC = NumberOfPart.NumberOfPart(0, str(partName))
        self.maxParts.append(NoPM)
        self.currParts.append(NoPC)


    def canAddPartToPocket(self, partName):
        partName = str(partName)
        for index, item in enumerate(self.maxParts, start=1):
            if item.partName == partName:
                maxAmt = item.num
                #print("Max:")
                #print(item.num)
                #print("Part Name:")
                #print(item.partName)
                #print("Item index is:")
                #print(index)
                currentAmt = self.currParts[index-1].num
                #print ("curr:")
                #print(currentAmt)
                print("Pocket #" + str(index))
                print(str(maxAmt) + "Max Amt")
                if currentAmt + 1 <= maxAmt:
                    print("pocket location is" + str(self.location.x) +str(self.location.y))
                    return True
                else:
                    return False

    def addPartToPocket(self, partName,height):
        if self.canAddPartToPocket(partName):
            #print("Can this part be added to this pocket?")
            #print(str(self.canAddPartToPocket(partName)))
            for index, item in enumerate(self.maxParts, start=0):
                #print("Item being tested is:" + str(self.maxParts[index].partName) + "\n")
                if item.partName == partName:
                    self.currParts[index].num = self.currParts[index].num + 1
                    print("Part added is:" + str(self.currParts[index].partName))
                    print("Amount is " + str(self.currParts[index].num)+"\n\n")
                    destination = [self.location.x, self.location.y, height]
                    self.motors.goTo(destination,self.name)
                    return
        else:
            print("Part does not belong in this pocket\n\n")

    def partsSum(self):
        sum = 0
        for item in self.currParts:
            sum = sum + item.num
        return sum
    def addName(self,name):
        self.name = name
class NumberOfPart:
    def __init__(self,num, partName):
        """
        :type num: int
        :type partName: String
        """
        self.num = num
        self.partName = partName

    def setNum(self, num):
        self.num = num

    def setName(self, name):
        self.partName = str(name)

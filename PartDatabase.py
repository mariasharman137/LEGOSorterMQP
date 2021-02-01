class PartDatabase:
    """
    This contains a dictionary which contains all parts in the set.
    If it isnt in the dictionary, it is not a valid part in this set
    If it is, the name of the part is returned

    """
    def __init__(self):
        self.pdb = dict()

    def addPartToDB(self, color, shape, name):
        """ Adds an entry to the dictionary with color and shape concatenated
         to make the key, and the value is the name of the part
        :param color: String
        :param shape: String
        :param name: String
        :return: none
        """
        key = color + shape
        self.pdb[key] = name
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

import PartDatabase as PDb
import PhotoImporter as PhI
import Cnn
import ColorChoice as CC
import numpy as np
import TrayDB as TDb


class StateMachine:
    def __init__(self):
        # The color of the part
        self.color = ''

        # The numpy array from the most recent image
        self.imgArray = np.zeros((1, 1))

        # The shape returned by the NN
        self.shape = ""

        # The folder where the picture is sent
        self.imageLocation = r""  # ImageLocation will go here

        # the name of the part as held in the Part DB
        self.part = ""

        # If the part has been found or not yet in identify_part
        self.part_found = False

        # How any times the part has attempted to be found
        self.part_attempts = 0

        #Starting state
        self.state = 0

        # Declarations of other classes needed
        self.SMPhI = PhI.PhotoImporter()
        self.CC = CC.ColorChoice()
        self.PDb = PDb.PartDatabase()
        self.TDb = TDb.TrayDB(5)
        self.Cnn = Cnn.Cnn()

    def stateMachine(self):
        while (True):
            while self.state == 0:
                self.findPart()
            while self.state == 1:
                self.identify_Part()
            while self.state == 2:
                self.place_Part()
            while self.state == 3:
                self.Reset()
    def findPart(self):
        print("Looking for part")
        print("Part found!")
        self.state = 1

    def identify_Part(self):
        # Run camera until a part is found
        self.color = self.CC.chooseColor(self.SMPhI.imagesFromFolder(self.imageLocation))
        self.imgArray = self.SMPhI.photoToArray(self.imageLocation)
        self.shape = self.Cnn.getShape(self.imageLocation)
        while self.part_found == False or self.part_attempts < 3:
            self.part_found = self.PDb.checkIfPart(self.color, self.shape)
            self.part_attempts = self.part_attempts + 1
        if self.part_attempts == 3 and self.part_found == False:
            self.part = "INVALID"
        elif self.part_attempts <= 3 and self.part_found == True:
            self.part = self.PDb.returnPart(self.color, self.shape)
        else:
            self.part = "ERROR"
        self.state = 2

    def place_Part(self):
        TDb.placePart(self.color, self.shape)
        self.state = 3

    def Reset(self):
        self.color = ""
        self.imgArray = np.zeros((1, 1))
        self.shape = ""
        self.imageLocation = r""  # ImageLocation will go here
        self.part = ""
        self.part_found = False
        self.part_attempts = 0
        self.state = 0




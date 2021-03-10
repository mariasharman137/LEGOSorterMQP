import PartDatabase as PDb
import PhotoImporter as PhI
import Cnn
import ColorChoice as CC
import numpy as np
import TrayDB as TDb


class StateMachine:
    def states(self,state):
        global color = ''
        global imgArray =np.zeros((1,1))
        global part = ""
        while state == 1:
            self.identify_Part()
        while state == 2:
            self.place_Part()
        while state == 3:
            self.Reset()

    def identify_Part(self):
        # Run camera until a part is found
        part_found: bool = False
        part_attempts: int = 0
        global color = CC.getColor(image)
        global imgArray = PhI.photoToArray(imageLocation)
        global shape = Cnn.getShape(imageLocation)
        while part_found == false or part_attempts < 3:
           global part_found = PDb.checkIfPart(color,shape)
           part_attempts = part_attempts + 1
        if part_attempts = 3 and part_found = false:
           global part = "INVALID"
        elif part_attempts <= 3 and part_found = true:
           global part = PDb.returnPart(color,shape)
        else:
           part = "ERROR"
        global state = 2


    def place_Part(self):
        TDb.placePart(part)
        global state = 3

    def Reset(self):
        global color = ''
        global imgArray =np.zeros((1, 1))
        global part = ''
        global shape = ''

    if __name__ == "__main__":
        # execute only if run as a script
        states(1)



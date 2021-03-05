from PhotoImporter import PhotoImporter as PhI
import ColorDB
from ColorChoice import ColorChoice as CC
from Greyscale import Greyscale
import numpy as np

class TestFunctions:

    # PhotoImporter.py
    def testphotoToArray():
        testimg = PhI.photoToArray("ColorFiles/Blue.png")
        print("Image tested")
        for r in testimg:
            for c in r:
                print(c, end=" ")
            print()
        return True

    def testBlue():
        testimg = PhI.photoToArray("ColorFiles/Blue.png")
        print (CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Blue"

    def testRed():
        testimg = PhI.photoToArray("ColorFiles/Red.png")
        print (CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Red"

    def testDarkGrey():
        testimg = PhI.photoToArray("ColorFiles/DarkGrey.png")
        print (CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Dark Grey"

    def testLightGrey():
        testimg = PhI.photoToArray("ColorFiles/LightGrey.png")
        print(CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Light Grey"

    def testTan():
        testimg = PhI.photoToArray("ColorFiles/Tan.png")
        print (CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Tan"

    def testYellow():
        testimg = PhI.photoToArray("ColorFiles/Yellow.png")
        print (CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Yellow"

    def testDarkGreyLego():
        testimg = PhI.photoToArray("ColorFiles/DarkGreyLegoCrop.png")
        print(CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Dark Grey"

    def testBlankBlue():
        testimg = PhI.photoToArray("ColorFiles/BlankBlue.png")
        print(CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Blue"

    def testGreyscale():
        testimg = PhI.photoToArray("ColorFiles/BlankBlue.png")
        tgs = Greyscale.ArraytoGreyscale(testimg)
        for r in tgs:
            for c in r:
                print(c, end=" ")
            print()
        assert tgs[0][0] == 0 and tgs[3][3] == 239


    def testPrint():
        testimg = PhI.photoToArray("ColorFiles/BlankBlue.png")
        PhI.printArray(testimg,"GSTest")
        assert np.allclose((PhI.photoToArray("ColorFiles/BlankBlue.png")),(PhI.photoToArray("GSTest.png")))




    if __name__ == "__main__":
        testphotoToArray()
        testBlue()
        testRed()
        testLightGrey()
        testDarkGrey()
        testYellow()
        testDarkGreyLego()
        testBlankBlue()
        testGreyscale()
        testPrint()
        print("Everything passed")

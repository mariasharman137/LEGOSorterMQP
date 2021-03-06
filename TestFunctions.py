from PhotoImporter import PhotoImporter as PhI
import ColorDB
from ColorChoice import ColorChoice as CC
from Greyscale import Greyscale
import numpy as np
import PartDatabase as PDb
import Tray
import Pocket
import TrayDB


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
        print(CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Blue"

    def testRed():
        testimg = PhI.photoToArray("ColorFiles/Red.png")
        print(CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Red"

    def testDarkGrey():
        testimg = PhI.photoToArray("ColorFiles/DarkGrey.png")
        print(CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Dark Grey"

    def testLightGrey():
        testimg = PhI.photoToArray("ColorFiles/LightGrey.png")
        print(CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Light Grey"

    def testTan():
        testimg = PhI.photoToArray("ColorFiles/Tan.png")
        print(CC.chooseColor(testimg))
        assert (CC.chooseColor(testimg)) == "Tan"

    def testYellow():
        testimg = PhI.photoToArray("ColorFiles/Yellow.png")
        print(CC.chooseColor(testimg))
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
        assert tgs[0][0] == 0 and tgs[3][3] == 131

    def testPrint():
        testimg = PhI.photoToArray("ColorFiles/BlankBlue.png")
        PhI.printArray(testimg, "GSTest")
        assert np.allclose((PhI.photoToArray("ColorFiles/BlankBlue.png")), (PhI.photoToArray("GSTest.png")))

    def testPartDB1():
        testPDb = PDb.PartDatabase()
        assert testPDb.checkIfPart("Black", "4716")

    def testPartDB2():
        testPDb = PDb.PartDatabase()
        assert not testPDb.checkIfPart("Purple", "22222")

    def testPartDB3():
        testPDb = PDb.PartDatabase()
        assert testPDb.returnPart("Black", "4716"), "Worm Screw Long"

    def testPocket1():
        testPocket = Pocket.Pocket()
        testPocket.setLocation(10,20)
        testPocket.addNewPartData(5334,5)
        assert testPocket.currParts[0].num == 0
        assert testPocket.maxParts[0].num == 5
        assert testPocket.maxParts[0].partName == "5334"
        assert testPocket.currParts[0].partName == "5334"

    def testPocket2():
        testPocket = Pocket.Pocket()
        testPocket.setLocation(10,20)
        testPocket.addNewPartData(5334, 5)
        testPocket.addNewPartData(3518, 4)
        testPocket.addNewPartData(9999, 8)
        assert testPocket.isPartInPocket("5334")
        assert not testPocket.isPartInPocket("69420")
        assert testPocket.currParts[0].num == 0
        assert testPocket.currParts[0].partName == "5334"
        assert testPocket.maxParts[0].num == 5
        assert testPocket.currParts[0].partName == "5334"
        assert testPocket.canAddPartToPocket("3518")
        testPocket.addPartToPocket("5334")
        assert testPocket.currParts[0].num == 1
        testPocket.currParts[0].num = 100
        assert not testPocket.canAddPartToPocket("5334")






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
        testPartDB1()
        testPartDB2()
        testPartDB3()
        testPocket1()
        testPocket2()
        print("Everything passed")

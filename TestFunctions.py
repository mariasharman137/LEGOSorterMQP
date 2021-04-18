from PhotoImporter import PhotoImporter as PhI
import ColorDB
from ColorChoice import ColorChoice as CC
from Greyscale import Greyscale
import numpy as np
import PartDatabase as PDb
import Tray
import Pocket
import TrayDB
import PartToPocket
import Cnn
import Motors


# noinspection PyMethodParameters
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

    def testPTP():
        testptp = PartToPocket.PartToPocket()
        assert testptp.getPocket("Light Grey Brick 1x2 with Round Hole") == 12
        assert testptp.getPocket("Black 3L Pin") == 6
        assert not testptp.getPocket("Black Knob Wheel") == 20

    def testTDb():
        testTDb = TrayDB.TrayDB(3)
        testTDb.setHeights(20,50)
        testTDb.placePart("Black", 3705)
        assert testTDb.trays[0].partsSum() == 1
        testTDb.placePart("Black", 3705)
        assert testTDb.trays[0].partsSum() == 2
        testTDb.placePart("Black", 3705)
        assert testTDb.trays[0].partsSum() == 3
        testTDb.placePart("Black", 3705)
        assert testTDb.trays[0].partsSum() == 4
        testTDb.placePart("Black", 3705)
        assert testTDb.trays[0].partsSum() == 5
        testTDb.placePart("Black", 3705)
        assert testTDb.trays[0].partsSum() == 6
        testTDb.placePart("Black", 3705)
        assert testTDb.trays[0].partsSum() == 6
        assert testTDb.trays[1].partsSum() == 1

    def testCnnDataArray():
        testCNN = Cnn.Cnn()
        #testDirectory = "C:/Users/phili/LEGOSorterMQP/ColorFiles"
        results = testCNN.makeDataArray(testDirectory)
        print("results")
        print(results)
        print("Each array")
        print(np.dsplit(results, 13))
    def testCnnLabelList():
        testCNN = Cnn.Cnn()
        # testDirectory = "C:\Users\phili\LEGOSorterMQP\ColorFiles"
        print(testCNN.makeLabelArray(testDirectory))

    def testPIimagesFromFolder():
        PI = PhI()
        # testDirectory = "C:\Users\phili\LEGOSorterMQP\ColorFiles"
        print(PI.imagesFromFolder(testDirectory))
    def testCNN():
        # testDirectory = "C:\Users\phili\LEGOSorterMQP\ColorFiles"
        testCnn = Cnn.Cnn()
        testCnn.Train(testDirectory)
    def testPartsList():
        testPDb = PDb.PartDatabase()
        print(testPDb.partsList)

    def testClawOpenWidth():
        testMotors = Motors.Motors()
        testMotors.openClawWidth(testMotors.CWL.getWidth(5))


    if __name__ == "__main__":
        # testphotoToArray()
        # testBlue()
        # testRed()
        # testLightGrey()
        # testDarkGrey()
        # testYellow()
        # testDarkGreyLego()
        # testBlankBlue()
        # testGreyscale()
        # testPrint()
        # testPartDB1()
        # testPartDB2()
        # testPartDB3()
        #testPTP()
        #testTDb()
        #testCnnLabelList()
        #testCnnDataArray()
        #testPIimagesFromFolder()
        #testCNN()
        #testPartsList()
        testClawOpenWidth()
        print("Everything passed")

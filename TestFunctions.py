from PhotoImporter import PhotoImporter as PhI
import ColorDB
from ColorChoice import ColorChoice as CC
from Greyscale import Greyscale
import numpy as np
import PartDatabase as PDb
import Tray
import Pocket
import TrayDB


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

    def testPocket1():
        testPocket = Pocket.Pocket()
        testPocket.setLocation(10, 20)
        testPocket.addNewPartData(5334, 5)
        assert testPocket.currParts[0].num == 0
        assert testPocket.maxParts[0].num == 5
        assert testPocket.maxParts[0].partName == "5334"
        assert testPocket.currParts[0].partName == "5334"

    def testPocket2():
        testPocket = Pocket.Pocket()
        testPocket.setLocation(10, 20)
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
        testPocket.addPartToPocket("5334",50)
        assert testPocket.currParts[0].num == 1
        print(str(testPocket.currParts[0].num) + "is the amount of parts")
        testPocket.currParts[0].num = 100
        assert not testPocket.canAddPartToPocket("5334")

    def testTray():
        testPocket = Pocket.Pocket()
        testPocket.setLocation(10, 20)
        testPocket.addNewPartData(5334, 5)
        testPocket.addNewPartData(3518, 4)
        testPocket.addNewPartData(9999, 8)

        testPocket2 = Pocket.Pocket()
        testPocket2.setLocation(100, 200)
        testPocket2.addNewPartData(1111, 1)
        testPocket2.addNewPartData(3518, 4)
        testPocket2.addNewPartData(2222, 2)

        testtray = Tray.Tray()
        testtray.addHeight(200)
        testtray.addPocket(testPocket)
        testtray.addPocket(testPocket2)

        testtray.addPartToTray(2222)
        print("One 2222 has been added")
        print("Number of 2222 in pocket is: " + str(testtray.pockets[1].currParts[2].num))
        assert testtray.pockets[1].currParts[2].num == 1

        testtray.addPartToTray(2222)
        print("Number of 2222 in pocket is: " + str(testtray.pockets[1].currParts[2].num))
        assert testtray.pockets[1].currParts[2].num == 2
        testtray.addPartToTray(2222)
        print("Number of 2222 in pocket is: " + str(testtray.pockets[1].currParts[2].num))
        assert testtray.pockets[1].currParts[2].num == 2

    def testTrayDB():
        testPocket = Pocket.Pocket()
        testPocket.setLocation(10, 20)
        testPocket.addNewPartData(5334, 5)
        testPocket.addNewPartData(3518, 4)
        testPocket.addNewPartData(9999, 8)

        testPocket2 = Pocket.Pocket()
        testPocket2.setLocation(100, 200)
        testPocket2.addNewPartData(1111, 1)
        testPocket2.addNewPartData(3518, 4)
        testPocket2.addNewPartData(2222, 2)

        testPocket3 = Pocket.Pocket()
        testPocket3.setLocation(10, 20)
        testPocket3.addNewPartData(5334, 5)
        testPocket3.addNewPartData(3518, 4)
        testPocket3.addNewPartData("Black Technic Axle 4", 8)

        testPocket4 = Pocket.Pocket()
        testPocket4.setLocation(100, 200)
        testPocket4.addNewPartData(1111, 1)
        testPocket4.addNewPartData(3518, 4)
        testPocket4.addNewPartData(2222, 2)

        testtray = Tray.Tray()
        testtray.addHeight(200)
        testtray.addPocket(testPocket)
        testtray.addPocket(testPocket2)

        testtray2 = Tray.Tray()
        testtray2.addHeight(200)
        testtray2.addPocket(testPocket3)
        testtray2.addPocket(testPocket4)

        testTrayDB = TrayDB.TrayDB()
        testTrayDB.addTray(testtray)
        testTrayDB.addTray((testtray2))

        testTrayDB.setHeights(50,100)
        print(testTrayDB.trays[1].pockets[0].currParts[2].partName)
        testTrayDB.placePart("Black",3705)

        assert testTrayDB.trays[1].pockets[0].currParts[2].num == 1
        assert testtray.height == 50
        assert testtray2.height == 150
        assert testTrayDB.partsSum() == 1


    if __name__ == "__main__":
        #testphotoToArray()
        #testBlue()
        #testRed()
        #testLightGrey()
        #testDarkGrey()
        #testYellow()
        #testDarkGreyLego()
        #testBlankBlue()
        #testGreyscale()
        #testPrint()
        #testPartDB1()
        #testPartDB2()
        #testPartDB3()
        #testPocket1()
        #testPocket2()
        #testTray()
        testTrayDB()
        print("Everything passed")

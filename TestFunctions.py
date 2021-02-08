from PhotoImporter import PhotoImporter as PhI
import ColorDB
from ColorChoice import ColorChoice as CC


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

    if __name__ == "__main__":
        testphotoToArray()
        testBlue()
        testRed()
        testLightGrey()
        testDarkGrey()
        testYellow()
        testDarkGreyLego()
        testBlankBlue()
        print("Everything passed")

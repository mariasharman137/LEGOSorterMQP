from PhotoImporter import PhotoImporter as PhI


class TestFunctions:

    # PhotoImporter.py
    def testphotoToArray():
        testimg= PhI.photoToArray("testImage.jpg")
        print("Image tested")
        for r in testimg:
            for c in r:
                print(c, end=" ")
            print()
        return True

    if __name__ == "__main__":
        testphotoToArray()
        print("Everything passed")

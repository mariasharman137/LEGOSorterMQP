import Jetson.GPIO as GPIO

class Motors:
    def __init__(self):

        #setting channel names
        DirectionX = 19
        StepX = 22

        #Assuming X is direction in which trays open/close

        #These are the ports for the motors which move things in the x,y,or z axis.
        self.PORTX = 1
        self.PORTY = 2
        self.PORTZ = 3

        #These are locations for the robot when they trays are closed
        self.CLOSETRAYX = 100
        self.CLOSETRAYY = 100

        #these are locations for when the part is being dropped
        self.DEFAULTX = 0
        self.DEFAULTY = 0

        #Code to set up GPIO stuff
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(DirectionX, GPIO.OUT) #directionX
        GPIO.setup(StepX, GPIO.OUT) #stepX

        #Set state: GPIO.output(channel,state)
        #set state: GPIO.output(channel,state, intital = GPIO.HIGH  OR GPIO.LOW)
        #Read value (high or low): GPIO.input(channel)



    def goTo(self,locationList):
        goalx = int(locationList[0])
        goaly = int(locationList[1])
        goalz = int(locationList[2])

        self.MagnetOn()
        self.MotorGoTo(self.PORTY, self.DEFAULTY)
        self.MagnetOff()
        self.MotorGoTo(self.PORTX,self.DEFAULTX)
        self.dropPart()
        self.MotorGoTo(self.PORTZ, goalz)
        self.MagnetOn()
        self.MotorGoTo(self.PORTY, goaly)
        self.MotorGoTo(self.PORTX, goalx)
        self.openClaw()
        self.closeClaw()
        self.MagnetOff()

        #Robot will return to default position next time code is run

    def MotorGoTo(self,port,goal):
        #TODO Add low level motor stuff
        print("Motor in port " + str(port) + " is moving to " + str(goal))

    def MagnetOn(self):
        print("Magnet turning on")

    def MagnetOff(self):
        print("Magnet turning off")

    def dropPart(self):
        print("Dropping part")

    def openClaw(self):
        print("Opening claw")

    def closeClaw(self):
        print("Closing claw")
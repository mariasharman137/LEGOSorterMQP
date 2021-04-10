import Jetson.GPIO as GPIO
import time

class Motors:
    def __init__(self):

        #setting channel names
        self.DirectionX = 22
        self.StepX = 19
        self.ResetX = 21

        #Assuming X is direction in which trays open/close

        #These are the ports for the motors which move things in the x,y,or z axis.
        self.PORTX = "X"
        self.PORTY = "Y"
        self.PORTZ = "Z"

        #These are locations for the robot when they trays are closed
        self.CLOSETRAYX = 100
        self.CLOSETRAYY = 100

        #these are locations for when the part is being dropped
        self.DEFAULTX = 0
        self.DEFAULTY = 0

        #Variable becomes false if it is reset

        #Code to set up GPIO stuff
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.DirectionX, GPIO.OUT,initial=GPIO.LOW) #directionX
        GPIO.setup(self.StepX, GPIO.OUT,initial=GPIO.LOW) #stepX
        GPIO.setup(self.ResetX, GPIO.IN)

        self.xpos = 0.0
        self.ypos = 0.0
        self.zpos = 0.0

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

    def MotorGoTo(self,name,goal):
        #TODO Add low level motor stuff

        print("Motor " + str(name) + " is moving to " + str(goal))
        if name == "X":
            #assuming at 0
            #step angle = 1.2 deg
            #OD = 15 mm
            #Circ = 47.23 mm
            #300 steps per circumference
            #.157 mm / step
            if self.xpos < goal:
                GPIO.output(self.DirectionX,GPIO.HIGH)
                while self.xpos < goal and self.move == True:
                    GPIO.output(self.StepX,GPIO.HIGH)
                    time.sleep(0.01)
                    GPIO.output(self.StepX,GPIO.LOW)
                    time.sleep(0.005)
                    self.xpos = self.xpos + .157
                    if GPIO.input(self.ResetX) == GPIO.HIGH:
                        self.xpos = 0
                        self.move = False
                    print(self.xpos)
                self.move = True

            elif self.xpos > goal :
                GPIO.output(self.DirectionX,GPIO.LOW)
                while self.xpos > goal and self.move == True:
                    GPIO.output(self.StepX,GPIO.HIGH)
                    time.sleep(0.01)
                    GPIO.output(self.StepX,GPIO.LOW)
                    time.sleep(0.005)
                    self.xpos = self.xpos - .157
                    if GPIO.input(self.ResetX) == GPIO.HIGH:
                        self.xpos = 0
                        self.move = False
                    print(self.xpos)
                self.move = true

            else:
                pass

        elif name == "Y":
        #assuming at 0
        #step angle = 1.2 deg
        #OD = 15 mm
        #Circ = 47.23 mm
        #300 steps per circumference
        #.157 mm / step
            if self.ypos < goal:
                GPIO.output(self.DirectionY,GPIO.HIGH)
                while self.ypos < goal:
                    GPIO.output(self.StepY,GPIO.HIGH)
                    time.sleep(0.01)
                    GPIO.output(self.StepY,GPIO.LOW)
                    time.sleep(0.005)
                    self.ypos = self.ypos + .157
                    print(self.ypos)

            elif self.ypos > goal:
                GPIO.output(self.DirectionY,GPIO.LOW)
                while self.ypos > goal:
                    GPIO.output(self.StepY,GPIO.HIGH)
                    time.sleep(0.01)
                    GPIO.output(self.StepY,GPIO.LOW)
                    time.sleep(0.005)
                    self.ypos = self.ypos - .157
                    print(self.ypos)

            else:
                pass
        elif name == "Z":
            print("Z Motor not enabled yet")


            

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
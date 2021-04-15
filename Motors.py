import sys
sys.path.append('/opt/nvidia/jetson-gpio/lib/python')
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/Jetson/GPIO')
sys.path.append('/home/nvidia/repositories/nano_gpio/gpio_env/lib/python2.7/site-packages/periphery/')
import Jetson.GPIO as GPIO
import time
#from periphery import PWM
from pca9685_driver import Device


class Motors:
    def __init__(self):

        #setting channel names
        self.StepY = 22
        self.DirectionY = 19
        self.ResetY = 21
        self.clockZ = 5
        self.dataZ = 3
        self.clawChannel = 0
        self.emChannel = 1
        self.StepX = 38
        self.DirectionX = 40
        self.ResetX = 36

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

        GPIO.setup(self.DirectionY, GPIO.OUT,initial=GPIO.LOW) #directionX
        GPIO.setup(self.StepY, GPIO.OUT,initial=GPIO.LOW) #stepX
        GPIO.setup(self.ResetY, GPIO.IN)

        self.xpos = 0.0
        self.ypos = 0.0
        self.zpos = 0.0

        #Set state: GPIO.output(channel,state)
        #set state: GPIO.output(channel,state, intital = GPIO.HIGH  OR GPIO.LOW)
        #Read value (high or low): GPIO.input(channel)

        self.move = True

       
        #working_devs = [1,2,3,4,5]
        self.pca9685 = Device(0x40,1)
        #self.pca9685.set_pwm_frequency(60)
        # Set duty cycle
        self.pca9685.set_pwm(0, 2047)

        # set pwm freq
        self.pca9685.set_pwm_frequency(50)





    def set_duty_cycle(self, pwmdev, channel, dt):
        """
        @pwmdev a Device class object already configured
        @channel Channel or PIN number in PCA9685 to configure 0-15
        @dt desired duty cycle
        """
        val = (dt*4095)//100
        pwmdev.set_pwm(channel,val)

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
        self.move = True

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
                while self.xpos < goal: #and self.move == True:
                    GPIO.output(self.StepX,GPIO.HIGH)
                    time.sleep(0.01)
                    GPIO.output(self.StepX,GPIO.LOW)
                    time.sleep(0.005)
                    self.xpos = self.xpos + .157
                    if GPIO.input(self.ResetX) == GPIO.LOW:
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
                    if GPIO.input(self.ResetX) == GPIO.LOW:
                        self.xpos = 0
                        self.move = False
                    print(self.xpos)
                self.move = True

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
                while self.ypos < goal: #and self.move == True:
                    GPIO.output(self.StepY,GPIO.HIGH)
                    time.sleep(0.01)
                    GPIO.output(self.StepY,GPIO.LOW)
                    time.sleep(0.005)
                    self.ypos = self.ypos + .157
                    if GPIO.input(self.ResetY) == GPIO.LOW:
                        self.ypos = 0
                        self.move = False
                    print(self.ypos)
                self.move = True

            elif self.ypos > goal :
                GPIO.output(self.DirectionY,GPIO.LOW)
                while self.ypos > goal and self.move == True:
                    GPIO.output(self.StepY,GPIO.HIGH)
                    time.sleep(0.01)
                    GPIO.output(self.StepY,GPIO.LOW)
                    time.sleep(0.005)
                    self.ypos = self.ypos - .157
                    if GPIO.input(self.ResetY) == GPIO.LOW:
                        self.ypos = 0
                        self.move = False
                    print(self.ypos)
                self.move = True

            else:
                pass
        elif name == "Z":
            print("Z Motor not enabled yet")


            

    def MagnetOn(self):
        print("Magnet turning on")
        self.set_duty_cycle(self.pca9685,self.emChannel,100)

    def MagnetOff(self):
        print("Magnet turning off")
        self.set_duty_cycle(self.pca9685,self.emChannel,0)

    def dropPart(self):
        print("Dropping part")

    def openClaw(self):
        print("Opening claw")
        self.set_duty_cycle(self.pca9685,self.clawChannel,2)

    def neutralClaw(self):
        print("Opening claw")
        self.set_duty_cycle(self.pca9685,self.clawChannel,6)


    def closeClaw(self):
        print("Closing claw")
        self.set_duty_cycle(self.pca9685,self.clawChannel,10)


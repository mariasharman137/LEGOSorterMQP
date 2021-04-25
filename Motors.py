import sys

sys.path.append('/opt/nvidia/jetson-gpio/lib/python')
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/Jetson/GPIO')
sys.path.append('/home/nvidia/repositories/nano_gpio/gpio_env/lib/python2.7/site-packages/periphery/')
import Jetson.GPIO as GPIO
import time
import math
import clawWidthList
import UsSensor
#import board
# from periphery import PWM
from pca9685_driver import Device


class Motors:
    def __init__(self):

        #importing needed data
        self.CWL = clawWidthList.clawWidthList()
        self.UsSensor = UsSensor.UsSensor()

        # setting channel names
        self.StepY = 22
        self.DirectionY = 19
        self.ResetY =21
        self.clockZ = 5
        self.dataZ = 3
        self.clawChannel = 0 #unchanged
        self.emChannel = 1 #unchanged
        self.StepX = 38
        self.DirectionX =40
        self.ResetX =36
        self.PWMZ = 14 #,dutycycle is speed
        self.DirectionZ =15
        self.ResetZ = 11

        self.dutycyclevalue = 0
        self.deltaerror=1
        self.error0 = 1
        self.error1 = 1
        self.kp = .34
        self.kd = .01
        self.ki = 20
        self.readings = 50

        # Assuming X is direction in which trays open/close

        # These are the ports for the motors which move things in the x,y,or z axis.
        self.PORTX = "X"
        self.PORTY = "Y"
        self.PORTZ = "Z"

        # These are locations for the robot when they trays are closed
        self.CLOSETRAYY = 0

        # these are locations for when the part is being dropped from serializer
        self.DEFAULTX = 100
        self.DEFAULTY = 1000

        # Variable becomes false if it is reset

        # Code to set up GPIO stuff
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.DirectionX, GPIO.OUT, initial=GPIO.LOW)  # directionX
        GPIO.setup(self.StepX, GPIO.OUT, initial=GPIO.LOW)  # stepX
        GPIO.setup(self.ResetX, GPIO.IN)

        GPIO.setup(self.DirectionY, GPIO.OUT, initial=GPIO.LOW)  # directionX
        GPIO.setup(self.StepY, GPIO.OUT, initial=GPIO.LOW)  # stepX
        GPIO.setup(self.ResetY, GPIO.IN)

        GPIO.setup(self.ResetZ,GPIO.IN)

        self.xpos = 0.0
        self.ypos = 0.0
        self.zpos = 0.0

        # Set state: GPIO.output(channel,state)
        # set state: GPIO.output(channel,state, intital = GPIO.HIGH  OR GPIO.LOW)
        # Read value (high or low): GPIO.input(channel)

        self.move = True

        # working_devs = [1,2,3,4,5]
        self.pca9685 = Device(0x40, 1)
        # Set duty cycle
        self.pca9685.set_pwm(0, 2047)

        # set pwm freq
        self.pca9685.set_pwm_frequency(50)

        self.stepFrac = 1

        self.set_duty_cycle(self.pca9685, self.PWMZ, 0)

        self.zerror = 1



    def set_duty_cycle(self, pwmdev, channel, dt):
        """
        @pwmdev a Device class object already configured
        @channel Channel or PIN number in PCA9685 to configure 0-15
        @dt desired duty cycle
        """
        val = (int((dt * 4095) // 100))
        pwmdev.set_pwm(channel, val)

    def goTo(self, locationList,pocketNumber):
        goalx = int(locationList[0])
        goaly = int(locationList[1])
        goalz = float(locationList[2])

        #First turn everything on
        #make sure the claw is closed
        #Move to pos to get part
            #first y plus to get out of the way of the trays
            #next x since it can now move properly
            #z does not need to move
        #next move to the position to place the part
            #first move z since it is out of the way
            #Next move x since it is away from the trays
            #Next move y to 0 to grab the tray
            #Now move y to the part position
            #Place part (open claw and then sleep to let it be open for a little while)
        #close tray
            #Close claw
            #Move y to 0
            #turn off magnet
            #Move y 100

        #First turn everything on
        #make sure the claw is closed
        self.closeClaw()
        time.sleep(.25)
        self.MagnetOff()
        #Move to pos to get part
        #first y plus to get out of the way of the trays
        self.MotorGoTo("Y", self.DEFAULTY)
        #next x since it can now move properly
        self.MotorGoTo("X", self.DEFAULTX)
        #z does not need to move
        #next move to the position to place the part
        #first move z since it is out of the way
        self.MotorGoTo("Z", goalz)
        #Next move x since it is away from the trays
        self.MotorGoTo("X", goalx)
        #Next move y to 0 to grab the tray
        self.MotorGoTo("Y", self.CLOSETRAYY)
        time.sleep(.1)
        self.MagnetOn()
        time.sleep(.1)
        #Now move y to the part position
        self.MotorGoTo("Y", goaly)
        #Place part (open claw and then sleep to let it be open for a little while)
        self.MagnetOff()
        time.sleep(.1)
        self.openClaw()
        time.sleep(.25)
        #close tray
        #Close claw
        self.closeClaw()
        #Move y to 0 (close tray)
        self.MotorGoTo("Y", -1000)
        self.MotorGoTo("X", -1000)
        #turn off magnet
        self.MagnetOff()
        #Move y 100
        self.MotorGoTo("Y", 100)

    def MotorGoTo(self, name, goal):
        # TODO Add low level motor stuff
        self.move = True

        print("Motor " + str(name) + " is moving to " + str(goal))
        if name == "X":
            # assuming at 0
            # step angle = 1.2 deg
            # OD = 15 mm
            # Circ = 47.23 mm
            # 300 steps per circumference
            # .157 mm / step
            if self.xpos < goal and goal < 201:
                GPIO.output(self.DirectionX, GPIO.HIGH)
                while self.xpos < goal and self.move == True:
                    GPIO.output(self.StepX, GPIO.HIGH)
                    time.sleep(0.002/self.stepFrac)
                    GPIO.output(self.StepX, GPIO.LOW)
                    time.sleep(0.002/self.stepFrac)
                    self.xpos = self.xpos + .192/self.stepFrac
                    #if GPIO.input(self.ResetX) == GPIO.LOW:
                        #self.xpos = 0
                        #self.move = False
                    print(self.xpos)
                self.move = True

            elif self.xpos > goal:
                GPIO.output(self.DirectionX, GPIO.LOW)
                while self.xpos > goal and self.move == True:
                    GPIO.output(self.StepX, GPIO.HIGH)
                    time.sleep(0.002/self.stepFrac)
                    GPIO.output(self.StepX, GPIO.LOW)
                    time.sleep(0.002/self.stepFrac)
                    self.xpos = self.xpos - .192/self.stepFrac
                    if GPIO.input(self.ResetX) == GPIO.LOW:
                        self.xpos = 0
                        self.move = False
                    print(self.xpos)
                self.move = True

            else:
                pass

        elif name == "Y":
            # assuming at 0
            # step angle = 1.2 deg
            # OD = 15 mm
            # Circ = 47.23 mm
            # 300 steps per circumference
            # .157 mm / step
            if self.ypos < goal and goal < 400:
                GPIO.output(self.DirectionY, GPIO.HIGH)
                while self.ypos < goal and self.move == True:
                    GPIO.output(self.StepY, GPIO.HIGH)
                    time.sleep(0.001/self.stepFrac)
                    GPIO.output(self.StepY, GPIO.LOW)
                    time.sleep(0.001/self.stepFrac)
                    self.ypos = self.ypos + .195/self.stepFrac
                    #if GPIO.input(self.ResetY) == GPIO.LOW:
                        #self.ypos = 0
                        #self.move = False
                    print(self.ypos)
                self.move = True

            elif self.ypos > goal:
                GPIO.output(self.DirectionY, GPIO.LOW)
                while self.ypos > goal and self.move == True:
                    GPIO.output(self.StepY, GPIO.HIGH)
                    time.sleep(0.001/self.stepFrac)
                    GPIO.output(self.StepY, GPIO.LOW)
                    time.sleep(0.001/self.stepFrac)
                    self.ypos = self.ypos - .195/self.stepFrac
                    if GPIO.input(self.ResetY) == GPIO.LOW:
                        self.ypos = 0
                        self.move = False
                    print(self.ypos)
                self.move = True

            else:
                pass
        elif name == "Z":
            self.error0=0
            # iterator = 0
            # self.zpos = self.UsSensor.USMeasure()
            # if self.zpos < goal and goal < 100:
            #     # ztime = 0.0
            #     # while iterator<100 and self.move == True:
            #     #     self.set_duty_cycle(self.pca9685, self.DirectionZ, 100)
            #     #     self.set_duty_cycle(self.pca9685, self.PWMZ, 20)
            #     #     time.sleep(abs(goal)/100)
            #     #     #if GPIO.input(self.ResetZ) == GPIO.LOW:
            #     #         #self.ypos = 0
            #     #         #self.move = False
            #     #     print(self.zpos)
            #     #     iterator += 1
            #     # self.mov+e = True
            #     # self.set_duty_cycle(self.pca9685, self.PWMZ, 0)
            #     self.zerror = goal - self.zpos
            #     self.error0 = 0
            #     self.error1 = 0
            self.zerror = 20
            while not (self.zerror < 5 and self.zerror > -5):
                reading = 0
                for n in range(self.readings):
                    reading += self.UsSensor.USMeasure()
                    time.sleep(.0001)

                self.zpos = reading/self.readings
                self.zerror = goal - self.zpos
                self.error0 = self.error1 + self.error0
                self.error1 = self.zerror
                self.deltaerror = self.error0 - self.error1
                self.dutycyclevalue = int(self.kp * self.zerror + self.kd * self.deltaerror)
                if self.dutycyclevalue > 0:
                    if self.dutycyclevalue > 100:
                        self.dutycyclevalue = 100
                        self.set_duty_cycle(self.pca9685,self.DirectionZ,100)
                        self.set_duty_cycle(self.pca9685, self.PWMZ, self.dutycyclevalue)
                    else:
                        self.set_duty_cycle(self.pca9685,self.DirectionZ,100)
                        self.set_duty_cycle(self.pca9685, self.PWMZ, self.dutycyclevalue)

                elif self.dutycyclevalue < 0:
                    if self.dutycyclevalue < -100:
                        self.dutycyclevalue = -100
                        self.set_duty_cycle(self.pca9685, self.DirectionZ, 0)
                        self.set_duty_cycle(self.pca9685, self.PWMZ, -1*self.dutycyclevalue)
                    else:
                        self.set_duty_cycle(self.pca9685, self.DirectionZ, 0)
                        self.set_duty_cycle(self.pca9685, self.PWMZ, -1*self.dutycyclevalue)
                time.sleep(.1)
                print(str(self.zpos) + " z pos")
                print(str(goal) + " goal")
                print(str(self.zerror) + " z error")
                print(str(self.dutycyclevalue) + "DCV")
            # elif self.zpos > goal and abs(float(goal)) < 100:
            #     ztime = 0.0
            #     while iterator < 100 and self.move == True:
            #         self.set_duty_cycle(self.pca9685, self.DirectionZ, 0)
            #         self.set_duty_cycle(self.pca9685, self.PWMZ, 40)
            #         time.sleep(abs(goal)/100)
            #         if GPIO.input(self.ResetZ) == GPIO.LOW:
            #             self.ypos = 0
            #             self.move = False
            #         print(self.zpos)
            #         iterator += 1
            #     self.move = True
            #     self.set_duty_cycle(self.pca9685, self.PWMZ, 0)

            # else:
            #     pass
            self.set_duty_cycle(self.pca9685, self.PWMZ, 0)

    def MagnetOn(self):
        print("Magnet turning on")
        self.set_duty_cycle(self.pca9685, self.emChannel, 100)

    def MagnetOff(self):
        print("Magnet turning off")
        self.set_duty_cycle(self.pca9685, self.emChannel, 0)
 
    def dropPart(self):
        print("Dropping part")

    # Flaps are 2 inches wide
    def openClaw(self):
        print("Opening claw")
        self.set_duty_cycle(self.pca9685, self.clawChannel, 4)
        time.sleep(1)

    def neutralClaw(self):
        print("Opening claw neutral")
        self.set_duty_cycle(self.pca9685, self.clawChannel, 6.85)

    def closeClaw(self):
        print("Closing claw")
        self.set_duty_cycle(self.pca9685, self.clawChannel, 8.5)

    def openClawPercent(self, percent):
        print("opening claw " + percent + " %")
        DCValue = percent * 5 + 5
        self.set_duty_cycle(self.pca9685, self.clawChannel, DCValue)

    def openClawWidth(self,width):
        print("opening claw to a width of " + str(width) + " mm")
        widthPow = (((8.6/math.pi)*(math.acos((-1*width/89) + (45/44.5))+3.7)))-7
        print("duty cycle is " + str(widthPow))
        self.set_duty_cycle(self.pca9685, self.clawChannel, widthPow)

    def MotorGoToXZ(self,goalx,goalz):
        done = False
        xdir = 2
        zdir = 2
        error0 = 0
        error1 = 0
        if self.xpos > goalx:
            xdir = -1
            GPIO.output(self.DirectionX, GPIO.LOW)
        elif self.xpos < goalx:
            xdir = 1
            GPIO.output(self.DirectionX, GPIO.HIGH)
        else:
            xdir = 0

        if self.zpos > goalz:
            zdir = -1
        elif self.zpos < goalz:
            zdir = 1
        else:
            zdir = 0

        while done == False:
            if (self.xpos + .1 < goalx or self.xpos - .1 > goalx) and (self.xpos + 1 < goalx or self.xpos - 1 > goalx):
                done == True
            if  not (self.xpos + .1 < goalx or self.xpos - .1 > goalx):
                self.xpos = self.xpos + xdir * .157/self.stepFrac
                GPIO.output(self.StepX, GPIO.HIGH)
                time.sleep(0.002 / self.stepFrac)
                GPIO.output(self.StepX, GPIO.LOW)
                time.sleep(0.002 / self.stepFrac)
            if (not (self.zpos + .1 < goalz or self.zpos - .1 > goalz)) :
                #zpos = USReading
                #set direction pin to the correct direction
                if self.zpos - 1 > goalz:
                    self.set_duty_cycle(self.pca9685, self.DirectionZ, 100)
                else:
                    self.set_duty_cycle(self.pca9685, self.DirectionZ, 0)
                self.set_duty_cycle(self.pca9685, self.DirectionZ, 0)
                #Set dutycycle to value deterined by controller
                error0 = error1
                error1 = goalx - self.zpos
                deltaerror = error1 - error0
                DCContVal = kp * error1 + kd * (deltaerror)
                self.set_duty_cycle(self.pca9685, self.PWMZ, DCContVal)
                




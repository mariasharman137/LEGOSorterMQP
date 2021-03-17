class Motors:
    def __init__(self):
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

    def goTo(self,locationList):
        goalx = locationList[0]
        goaly = locationList[1]
        goalz = locationList[2]
        #resets tray position
        self.MotorGoTo(self.PORTX,self.DEFAULTX)
        self.MotorGoTo(self.PORTY, self.DEFAULTY)
        #TODO: Drop Part

        #Move to destination
        self.MotorGoTo(self.PORTZ, goalz)
        #TODO turn on magnet
        self.MotorGoTo(self.PORTY, goaly)
        self.MotorGoTo(self.PORTX, goalx)
        #TODO open end-effector

        #Robot will return to default position next time code is run

    def MotorGoTo(self,port,goal):
        #TODO Add low level motor stuff
        print("Motor in port " + str(port) + " is moving to " + str(goal))
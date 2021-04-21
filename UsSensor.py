import Jetson.GPIO as GPIO
import time
from Piya.Sonar.Echo import Echo



class UsSensor:
    def __init__(self):
        self.USTrig = 7
        self.USEcho = 12 #Moved from 8 to 12
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.USTrig, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.USEcho, GPIO.IN)
        self.USReading = 0

    def USMeasure(self):
        echo = Echo(self.USTrig,self.USEcho,343, 3,10,True,echo_callback)
        # print("Measuring Distance")
        # #start timer
        # time0 = time.perf_counter()
        # #send trigger input
        # GPIO.output(self.USTrig,GPIO.HIGH)
        # time.sleep(.00001)
        # GPIO.output(self.USTrig,GPIO.LOW)
       
        # GPIO.wait_for_edge(self.USEcho,GPIO.RISING)
        # time1 = time.perf_counter()
        # #end timer
        # print("Echo recieved")
        # print("start time:" + str(time0))
        # print("end time:" + str(time1))
        # ttime = time1-time0
        # uttime = ttime *1000000
        # deltatime = uttime/5.8
        # print(str(deltatime) + " mm")
        # return deltatime
        
        #deltatime(us) / 58 = dist in cm
        #deltatime(us) / 5.8 = dist in mm

    def echo_callback(values):
        self.USReading = float(values[0])
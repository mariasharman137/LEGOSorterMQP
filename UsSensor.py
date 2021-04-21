import Jetson.GPIO as GPIO
import time


class UsSensor:
    def __init__(self):
        self.USTrig = 7
        self.USEcho = 12 #Moved from 8 to 12
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.USTrig, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.USEcho, GPIO.IN)

    def USMeasure(self):
        print("Measuring Distance")
        #start timer
        time0 = time.perf_counter()
        #send trigger input
        GPIO.output(self.USTrig,GPIO.HIGH)
        time.sleep(.00001)
        GPIO.output(self.USTrig,GPIO.LOW)
       
        GPIO.wait_for_edge(self.USEcho,GPIO.RISING)
        time1 = time.perf_counter()
        #end timer
        print("Echo recieved")
        print("start time:" + str(time0))
        print("end time:" + str(time1))
        ttime = time1-time0
        uttime = ttime *1000000
        deltatime = uttime/5.8
        print(str(deltatime) + " mm")
        return deltatime
        
        #deltatime(us) / 58 = dist in cm
        #deltatime(us) / 5.8 = dist in mm
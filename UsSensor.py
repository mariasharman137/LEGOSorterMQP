import Jetson.GPIO as GPIO
import time


class UsSensor:
    def __init__(self):
        self.USTrig = 38
        self.USEcho = 40
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.USTrig, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.USEcho, GPIO.IN)

    def USMeasure(self):
        print("Measuring Distance")
        #start timer
        GPIO.LOW
        time0 = time.perf_counter()
        #send trigger input
        GPIO.output(self.USTrig,GPIO.HIGH)
        time.sleep(.00001)
        GPIO.output(self.USTrig,GPIO.LOW)
        #wait for return signal
        while GPIO.input(self.USEcho) == GPIO.LOW:
            time1 = time.perf_counter
            print("Waiting for response")
        #end timer
        ttime = time1-time0
        uttime = ttime *1000000
        deltatime = uttime/5.8
        return deltatime
        
        #deltatime(us) / 58 = dist in cm
        #deltatime(us) / 5.8 = dist in mm
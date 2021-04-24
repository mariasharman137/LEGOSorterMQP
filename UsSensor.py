import Jetson.GPIO as GPIO
import time
import busio
import board
from smbus2 import SMBus
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn




class UsSensor:
    def __init__(self):
        self.adc = Adafruit_ADS1x15.ADS1115(address=0x48, bus = 0)


    def USMeasure(self):
        for i in range(10):
            #values[i] = adc.read_adc(i,gain=1)
            print(adc.read_adc(i,gain=1))
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
            
            # deltatime(us) / 58 = dist in cm
            #deltatime(us) / 5.8 = dist in mm

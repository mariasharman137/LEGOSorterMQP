import Jetson.GPIO as GPIO
import time

from smbus2 import SMBus





class UsSensor:
    def __init__(self):
        self.bus = SMBus(0)
        self.address = 0x48
        data = [0b10000100,0x83]
        self.bus.write_i2c_block_data(0x48, 0x01, data)
        time.sleep(0.5)



    def USMeasure(self):
        # self.bus.write_byte_data(self.address, 0, 0b10010000)
        # self.bus.write_byte_data(self.address, 1, 0b10000001)
        # self.bus.write_byte_data(self.address, 2, 0b10000100)
        # self.bus.write_byte_data(self.address, 3, 0b10000011)
        # self.bus.write_byte_data(self.address, 0, 0b10010000)
        # firsthalf = self.bus.read_byte_data(self.address, 1, 0b00000000)
        # secondhalf = self.bus.read_byte_data(self.address, 2, 0b10010001)
        # tempstr = str(firsthalf) + str(secondhalf)
        # integerObtained = int(tempstr)
        # return integerObtained
        # data = [0b10000010,0x83]
        # self.bus.write_i2c_block_data(0x48, 0x01, data)
        # time.sleep(0.5)
        data = self.bus.read_i2c_block_data(0x48, 0x00, 2)
        raw_adc = data[0] * 256 + data[1]
        if raw_adc > 32767:
	        raw_adc -= 65535
        return raw_adc

        # b = self.bus.read_byte_data(0x48,1)
        # return (b)
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

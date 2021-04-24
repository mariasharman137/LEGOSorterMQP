import Jetson.GPIO as GPIO
import time
import busio
import board
from smbus2 import SMBus


bus = SMBus(0)
b = bus.read_byte_data(0x48,0)
print(b)
b = bus.read_byte_data(0x48,1)
print(b)
b = bus.read_byte_data(0x48,2)
print(b)
b = bus.read_byte_data(0x48,3)
print(b)



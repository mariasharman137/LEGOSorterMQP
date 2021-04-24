import board 
import digitalio
import busio
import Jetson.GPIO as GPIO
print("Hello Blinka")

pin = digitalio.DigitalInOut(board.D4)
print("digital io ok")
i2c = busio.I2C(board.SCL,board.SDA)
print("SCL1 ok")
print(GPIO.getMode())
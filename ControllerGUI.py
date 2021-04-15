import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from PhotoImporter import PhotoImporter as PhI
from ColorChoice import ColorChoice as CC
from Greyscale import Greyscale
from tkinter import font
import TrayDB
import PartDatabase
import Motors
import UsSensor
import Jetson.GPIO
import time

window = tk.Tk()
filename = "ColorFiles/Default.png"
resulting_color = "light grey"
load = Image.open(filename)
render = ImageTk.PhotoImage(load)
gRender = ""
myFont = font.Font(family='Helvetica', size=20)
CGPDb = PartDatabase.PartDatabase()
CGMotors = Motors.Motors()
CGUsSensor = UsSensor.UsSensor()

# going with 5 trays as default since that is the max the robot can hold
CGTDb = TrayDB.TrayDB(5)


# Gives part name if it exists, and if not, returns "Part not valid"
def getLabelPartname():
    partColor = str(entry_color.get())
    partShape = str(entry_shape.get())
    if CGPDb.checkIfPart(partColor, partShape):
        label_partname.configure(text="The part name is:  " + str(CGPDb.returnPart(partColor, partShape)),
                                 bg="light green")
        window.mainloop()
    else:
        label_partname.configure(text="Part not valid", bg="red")
        window.mainloop()


def goToPosXYZ():
    x = entry_pos_x.get()
    y = entry_pos_y.get()
    z = entry_pos_z.get()
    Location = [x, y, z]
    CGMotors.goTo(Location)


def goToPosX():
    CGMotors.MotorGoTo(CGMotors.PORTX, int(entry_pos_x.get()))


def goToPosY():
    CGMotors.MotorGoTo(CGMotors.PORTY, int(entry_pos_y.get()))


def goToPosZ():
    CGMotors.MotorGoTo(CGMotors.PORTZ, int(entry_pos_z.get()))


def turnOnMagnet():
    button_magnet_on.configure(bg="light green")
    button_magnet_off.configure(bg="red")
    CGMotors.MagnetOn()


def turnOffMagnet():
    button_magnet_off.configure(bg="light green")
    button_magnet_on.configure(bg="red")
    CGMotors.MagnetOff()


def dropPart():
    CGMotors.dropPart()
    button_part_drop.configure(bg="light green")


def openClaw():
    CGMotors.openClaw()
    button_open_claw.configure(bg="light green")
    button_close_claw.configure(bg="red")
    button_neutral_claw.configure(bg="red")


def neutralClaw():
    CGMotors.neutralClaw()
    button_open_claw.configure(bg="red")
    button_close_claw.configure(bg="red")
    button_neutral_claw.configure(bg="light green")



def closeClaw():
    CGMotors.closeClaw()
    button_close_claw.configure(bg="light green")
    button_open_claw.configure(bg="red")
    button_neutral_claw.configure(bg="red")



def placePart():
    partColor = str(entry_color.get())
    partShape = str(entry_shape.get())
    CGTDb.placePart(partColor, partShape)


def resetColors():
    button_magnet_off.configure(bg="white")
    button_magnet_on.configure(bg="white")
    button_close_claw.configure(bg="white")
    button_open_claw.configure(bg="white")
    button_part_drop.configure(bg="white")

def getUsDistance():
    label_Us_Distance.configure(text = "The distance is " + str(CGUsSensor.USMeasure()) + " cm")
def callReset():
    CGMotors.move=False


window.title('Controller Gui')
window.geometry("950x540")
window.config(background="white")

button_exit = tk.Button(window, text="Exit", command=exit, width=30, height=1, bg="red", font=myFont)

# New TextEntry & Label for Color
entry_color = tk.Entry(window, justify="center")
label_color = tk.Label(window, text="Enter color here:")

# New TextEntry & Label for Shape
entry_shape = tk.Entry(window, justify="center")
label_shape = tk.Label(window, text="Enter shape here:")

# New Label/button to show name of part, or if it is not valid, and label to show answer
label_partname = tk.Label(window, text="The name of the part is:")
button_partname = tk.Button(window, command=getLabelPartname, text="Click to view part name")
label_partname_answer = tk.Label(window, text="The answer will appear here")

# Button and entry for move to position: X,Y,Z
button_pos_xyz = tk.Button(window, command=goToPosXYZ, text="Click to go to the x,y, and z position position")
entry_pos_xyz = tk.Entry(window, justify="center")

# Button and entry for move to position: X
button_pos_x = tk.Button(window, command=goToPosX, text="Click to go to only x position")
entry_pos_x = tk.Entry(window, justify="center")

# Button and entry for move to position: Y
button_pos_y = tk.Button(window, command=goToPosY, text="Click to go to only y position")
entry_pos_y = tk.Entry(window, justify="center")

# Button and entry for move to position: Z
button_pos_z = tk.Button(window, command=goToPosZ, text="Click to go to only z position")
entry_pos_z = tk.Entry(window, justify="center")

# Title
imageColor = tk.Label(text="Welcome to Controller GUI", width=30, height=1, font=myFont)

# Button to turn magnet on
button_magnet_on = tk.Button(window, text="Turn Magnet On", command=turnOnMagnet)

# Button to turn magnet off
button_magnet_off = tk.Button(window, text="Turn Magnet Off", command=turnOffMagnet)

# Button to drop part
button_part_drop = tk.Button(window, text="Drop Part", command=dropPart)

# Button to open claw
button_open_claw = tk.Button(window, text="Open Claw", command=openClaw)

# button to close claw
button_close_claw = tk.Button(window, text="Close Claw", command=closeClaw)

#button to neutral claw
button_neutral_claw = tk.Button(window, text = "Middle Pos Claw", command = neutralClaw)

# Reset Button Colors
button_reset_colors = tk.Button(window, text="Reset CGui Colors", command=resetColors)

# Place Part
button_place_part = tk.Button(window, text="Press to place part with above color and shape", command=placePart)

# Get Distance
button_Us_Sensor = tk.Button(window, command = getUsDistance)
label_Us_Distance = tk.Label(window, text = "Press to get distance obtained by Ultrasonic Sensor")

#Stop Button
button_stop = tk.Button(window, command = callReset, text = "reset to 0")

# Locations of elements in grid:
imageColor.grid(column=1, row=1)
button_exit.grid(column=2, row=1)

entry_color.grid(column=2, row=2)
label_color.grid(column=1, row=2)

label_shape.grid(column=1, row=3)
entry_shape.grid(column=2, row=3)

button_pos_xyz.grid(column=1, row=7)
entry_pos_xyz.grid(column=2, row=7)

button_pos_x.grid(column=1, row=4)
entry_pos_x.grid(column=2, row=4)

button_pos_y.grid(column=1, row=5)
entry_pos_y.grid(column=2, row=5)

button_pos_z.grid(column=1, row=6)
entry_pos_z.grid(column=2, row=6)

label_partname.grid(column=2, row=8)
button_partname.grid(column=1, row=8)

# Button to turn magnet on
button_magnet_on.grid(column=1, row=9)
button_magnet_off.grid(column=2, row=9)

button_open_claw.grid(column=1, row=10)
button_close_claw.grid(column=2, row=10)
button_neutral_claw.grid(column = 3, row = 10)

button_part_drop.grid(column=1, row=11)
button_reset_colors.grid(column=2, row=11)

button_place_part.grid(column=1, row=12)

button_Us_Sensor.grid(column=2, row = 13)
label_Us_Distance.grid(column=1, row = 13)

button_stop.grid(column = 1, row = 14)

# to show the window
window.mainloop()

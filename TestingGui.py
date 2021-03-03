import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from PhotoImporter import PhotoImporter as PhI
from ColorChoice import ColorChoice as CC
from Greyscale import Greyscale

window = tk.Tk()
filename = "ColorFiles/Default.png"
resulting_color = "light grey"
load = Image.open(filename)
render = ImageTk.PhotoImage(load)
gRender = ""


def browseFiles():
    global filename
    global window
    global render
    clearCImg()
    clearGImg()
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=[("all files", "*.*")])
    label_file_explorer.configure(text="File Opened: " + filename)
    load = Image.open(filename)
    render = ImageTk.PhotoImage(load)
    img.configure(image=render)


def getColor():
    global resulting_color
    testimg = PhI.photoToArray(filename)
    resulting_color = (str(CC.chooseColor(testimg)))
    imageColor.configure(text=resulting_color)
    print(resulting_color)
    label_file_explorer.config(bg=resulting_color)
    window.mainloop()


def showGreyscale():
    global gRender
    # localArray = PhI.photoToArray(filename)
    # localGArray = Greyscale().ArrayToGreyscale(localArray)
    # gImage = Image.fromarray(localGArray,'L')
    # gRender = ImageTk.PhotoImage(gImage)
    # img.configure(image=gRender)

    # gets image file, makes it into an array
    testimg = PhI.photoToArray(filename)

    # changes Array from a 3d RGB array into a 2d Greyscale one
    tgs = Greyscale.ArraytoGreyscale(testimg)

    # makes an image from the array
    gImage = Image.fromarray(tgs)
    gRender = ImageTk.PhotoImage(gImage)
    gimg.configure(image=gRender)
    #uncomment below to get pixel values in terminal
    #for r in tgs:
        #for c in r:
            #print(c, end=" ")
        #print()


def clearCImg():
    global render
    render = ''
    #img.configure(image=render)


def clearGImg():
    global gRender
    gRender = ''
    #img.configure(image=gRender)


window.title('Testing Gui')
window.geometry("1900x1080")
window.config(background="white")

label_file_explorer = tk.Label(window, text="The color will appear here once calculated", width=135, height=4,)

button_explore = tk.Button(window, text="Browse Files", command=browseFiles,width=135, height=4)

button_exit = tk.Button(window, text="Exit", command=exit,width=135, height=4, bg = "red")

button_color = tk.Button(window, text="Obtain Color", command=getColor, width=135, height=4)

button_show_greyscale = tk.Button(window, text="Press to show greyscale image", command=showGreyscale, width=135, height=4)

button_clear_img = tk.Button(window, text="clear color img", command=clearCImg, width=135, height=4, bg = 'orange')

button_clear_g_img = tk.Button(window, text="clear greyscale img", command=clearGImg, width=135, height=4, bg = "orange")

imageColor = tk.Label(text="Welcome to Testing GUI", width = 135, height = 4)

imageColor.grid(column=1, row=1)

label_file_explorer.grid(column=1, row=2)

button_explore.grid(column=1, row=3)

button_exit.grid(column=2, row=1)

button_color.grid(column=1, row=4)

button_clear_img.grid(column = 2, row = 2)

button_clear_g_img.grid(column = 2, row = 3)

img = tk.Label(image=render)
img.image = render
img.grid(column=1, row=6)

button_show_greyscale.grid(column=2, row=4)

gimg = tk.Label(image=gRender)
gimg.image = gRender
gimg.grid(column=2, row=6)

# to show the window
window.mainloop()

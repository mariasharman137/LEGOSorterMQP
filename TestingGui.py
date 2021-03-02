import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from PhotoImporter import PhotoImporter as PhI
from ColorChoice import ColorChoice as CC

window = tk.Tk()
filename = "ColorFiles/Default.png"
resulting_color = ""


def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=[("all files", "*.*")])
    label_file_explorer.configure(text="File Opened: " + filename)
    load = Image.open(filename)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(image=render)
    img.image = render
    img.grid(column=1, row=5)


def getColor():
    global resulting_color
    testimg = PhI.photoToArray(filename)
    resulting_color = (str(CC.chooseColor(testimg)))
    imageColor.configure(text=resulting_color)
    print(resulting_color)
    window.mainloop()


window.title('Testing Gui')
window.geometry("800x800")
window.config(background="white")

label_file_explorer = tk.Label(window, text="File Explorer using Tkinter", width=100, height=4, fg="blue")

button_explore = tk.Button(window, text="Browse Files", command=browseFiles)

button_exit = tk.Button(window, text="Exit", command=exit)

button_color = tk.Button(window, text="Obtain Color", command=getColor)

imageColor = tk.Label(text="Hello, Tkinter")

imageColor.grid(column=1, row=1)

label_file_explorer.grid(column=1, row=2)

button_explore.grid(column=1, row=3)

button_exit.grid(column=1, row=4)

button_color.grid(column=1, row=6)



# to show the window
window.mainloop()

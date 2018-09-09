import serial

from tkinter import *
from tkinter import ttk

import time # for after()
import random

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# Windows: COM5
# OSX: 
port = 'COM5'
ser = serial.Serial(port, 9600)

class myGUI:
    def __init__(self, master):
        self.master = master
        master.title("seePR")

        self.frame = Frame(master)
        self.frame.pack()

        global label_var
        label_var = Label(self.frame, text="initial")
        label_var.pack()

    def update_value(self):
        val = str(ser.readline())
        val = val.split("=")[1] # clean the string
        val = val.split("\\")[0]
        global label_var
        label_var.destroy()
        label_var = Label(self.frame, text=val)
        label_var.pack()
        self.frame.after(1, self.update_value)

root = Tk() # main window
my_gui = myGUI(root)
root.after(1, my_gui.update_value())
root.mainloop()
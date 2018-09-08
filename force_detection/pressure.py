import serial
from tkinter import *
from tkinter import ttk
import time
import matplotlib.pyplot as plt

# Windows: COM5
# OSX: 
port = 'COM5'
ser = serial.Serial(port, 9600)

# GUI
root = Tk() # main window
frame = Frame(root, width=1000, height=800)
frame.pack()

val_list = []

def add_value():
    val = str(ser.readline())
    val = val.split("=")[1] # clean the string
    val = val.split("\\")[0]
    label_var = Label(frame, text=val)
    label_var.grid(row=0, column=0)
    root.after(1, add_value)

    val_list.append(val)
    plt.plot(val_list)
    plt.ylabel('pressure values')
    plt.show()

root.after(0, add_value)
root.mainloop()
import serial
from tkinter import *
from tkinter import ttk
import time
import random

# Windows: COM5
# OSX: 
port = 'COM5'
ser = serial.Serial(port, 9600)

# GUI
root = Tk() # main window
frame = Frame(root, width=300, height=300)
frame.pack()

def add_value():
    val = ser.readline()
    label_var = Label(frame, text=val)
    label_var.grid(row=0, column=0)
    root.after(1, add_value)

root.after(0, add_value)  # add_letter will run as soon as the mainloop starts.
root.mainloop()

'''
labelText = StringVar()
label_var = Label(root, text="sensor data")
label_var.grid(row=0, column=0)

def update_value():
    x = ser.readline()
    print(x)
    #global label_var
    #label_var.destroy()
    #label_var = Label(root, text=x)
    #label_var.grid(row=0, column=0)

root.after(0, update_value)
root.mainloop()
'''
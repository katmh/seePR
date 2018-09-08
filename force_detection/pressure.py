import serial
from tkinter import *
from tkinter import ttk

ser = serial.Serial('COM5', 9600)

root = Tk()
labelText = StringVar()
label_var = Label(root, text="sensor data")
label_var.grid(row=0, column=0)

x = ser.readline()
print(x)
label_var.destroy()
label_var = Label(root, text=x)
label_var.grid(row=0, column=0)

root.mainloop()
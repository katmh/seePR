import serial

import tkinter as tk
from tkinter import ttk

import time # for after()
import random

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

# plot settings
LARGE_FONT= ("Verdana", 12)
style.use("ggplot")



current_plot = None


x = [1,2,3,4,5,6,7,8]
y = [1,2,3,4,5,6,7,8]



# Windows: COM5
# OSX: 
port = 'COM5'
ser = serial.Serial(port, 9600)

class myGUI:
    def __init__(self, master):
        self.master = master
        master.title("seePR")

        self.frame = tk.Frame(master)
        self.frame.pack()

        global label_var
        label_var = tk.Label(self.frame, text="initial")
        label_var.pack()

        # plot


        self.plot_pressure()

    def update_value(self):
        val = str(ser.readline())
        
        val = val.split("= ")[1] # clean the string
        val = val.split("\\")[0]
        
        global label_var, x, y
        label_var.destroy()
        label_var = tk.Label(self.frame, text=val)
        label_var.pack()
        
        #x.append(val)
        #y.append(y[-1] + 1)
        self.frame.after(1, self.update_value)
        #self.frame.after(1, self.plot_pressure)

    def plot_pressure(self):
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot(x, y)

        #global x, y
        
        canvas = FigureCanvasTkAgg(f, self.frame)
        canvas.show()
        current_plot = canvas.get_tk_widget()
        current_plot.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        canvas.print_figure('pressure_vs_time.png')

root = tk.Tk() # main window
my_gui = myGUI(root)
root.after(1, my_gui.update_value())
root.mainloop()
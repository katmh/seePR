import serial

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
x = []
y = []

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

        # initial plot
        self.plot_pressure()

        global val_list, time_list
        val_list = []
        time_list = []

        # elapsed time
        global start_time
        start_time = time.time()

    def update_value(self):
        val = str(ser.readline())

        global start_time
        elapsed_time = time.time() - start_time
        #print(elapsed_time)
        
        val = val.split("=")[1] # clean the string
        val = val.split("\\")[0]
        val = float(val)
        
        global label_var, x, y
        label_var.destroy() # replace, not add
        label_var = tk.Label(self.frame, text=val)
        label_var.pack()

        global val_list, time_list
        val_list.append(val)
        time_list.append(elapsed_time)
        if val > 800:
            messagebox.showwarning("Warning","Too high, put lower pressure")
        if val < 600:
            messagebox.showwarning("Warning","Too low, put more pressure")
        #print(val_list[-5:])

        # call to refresh plot        
        #x.append(val)
        #y.append(y[:-1] + 1)
        #self.refresh_plot()
        self.refresh_plot()
        self.frame.after(1, self.update_value)
        #self.frame.after(1, self.plot_pressure)

    def plot_pressure(self): # initial plot only
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)

        global line1
        line1, = a.plot(x,y,'r-')

        #global x, y
        
        global canvas
        canvas = FigureCanvasTkAgg(f, self.frame)
        canvas.show()
        current_plot = canvas.get_tk_widget()
        current_plot.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def refresh_plot(self):
        # update x and y values
        global val_list, time_list
        x = time_list[-10:]
        print(x)
        y = val_list[-10:]
        print(y)

        # refresh the plot
        global line1, canvas
        line1.set_data(x,y)
        ax = canvas.figure.axes[0]
        #print(ax)
        #ax.set_xlim(x.min(), x.max())
        ax.set_xlim(min(x), max(x))
        #ax.set_ylim(y.min(), y.max())
        ax.set_ylim(min(y), max(y))
        canvas.draw()

root = tk.Tk() # main window
my_gui = myGUI(root)
root.after(1, my_gui.update_value())
root.mainloop()
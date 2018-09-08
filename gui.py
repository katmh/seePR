from tkinter import *
from tkinter import ttk

root = Tk() # main window

frame = Frame(root)

labelText = StringVar()

label_var = Label(frame, textariable=labelText)
button = Button(frame, text="Click Me")

labelText.set("I am a Label")

label.pack()
button.pack()
frame.pack()

root.mainloop()
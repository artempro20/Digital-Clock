from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Clock")

def present_time():
    display_time = time.strftime("%H:%M:%S")
    clock.config(text=display_time)
    clock.after(200,present_time)

clock = Label(root, font=("TkTextFont",150),bg="green",fg="black")
clock.pack()

present_time()

root.mainloop()
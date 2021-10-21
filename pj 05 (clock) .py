from tkinter import *
from tkinter.ttk import *
from time import strftime

x=Tk()
x.title("Clock")

def time():
    s=strftime('%H:%M:%S %p')
    label.config(text=s)
    label.after(1000,time)

label=Label(x,background="Black",foreground="green")
label.pack(anchor='center')
time()

mainloop()

print("----End----")
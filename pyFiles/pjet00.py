from tkinter import *
from tkinter.ttk import *
 
from time import strftime



root =Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
    now=datetime.datetime.now()
    label.config(text=now)

label=Label(root, font=("ds_digital",80),background="black",foreground="cyan")
label.pack(anchor='center')
time()

#import datetime
#now=datetime.datetime.now()
#print(now)


mainloop() 

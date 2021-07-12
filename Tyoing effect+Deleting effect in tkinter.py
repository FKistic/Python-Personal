from tkinter import *
import tkinter as tk 

root=Tk()
import sys
from time import sleep
words = "Typing effect in tkinter.py"
ab=StringVar()
a=Label(textvariable=ab)
a.pack()
l=[]
for i in words:
    l.append(i)
    sleep(0.2)
    b=str(l)
    b=b.replace("[","")
    b=b.replace("]","")
    b=b.replace(", ","")
    b=b.replace(",","")
    b=b.replace("'","")
    b=b.replace("  ","")
    c=len(b)
    ab.set(f"{b[0:c-1]}{i}")
    a.update()
for i in range(c):
    sleep(0.2)
    sample_str = b[0:c-1] + ""
    ab.set(sample_str)
    a.update()
    c-=1
root.mainloop()

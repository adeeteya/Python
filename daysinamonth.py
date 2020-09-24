#days in a month using gui
#By Aditya.R 19S0604
#1/11/19
from tkinter import *
def monthcheck():
    if(e1.get() in m):
      Label(master,text="No of days in "+e1.get()+" is "+str(d[m.index(e1.get())])).grid(row=2)
    else:
      Label(master,text="Invalid Input").grid(row=2)
d=[31,29,31,30,31,30,31,31,30,31,30,31]
m=['january','february','march','april','may','june','july','august','september','octomber','november','december']
master=Tk()
master.title("Days in a month")
Label(master, text='Enter the month in lowercase ').grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
w=Button(master,text='enter',command=monthcheck).grid(row=1)
mainloop()

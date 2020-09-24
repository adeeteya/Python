import pyperclip,webbrowser
from tkinter import *
def search():
    webbrowser.open('https://www.google.com/maps/place/'+address.get())
master=Tk()
master.title('Maps')
w=Label(master,text='Enter The Location')
w.pack()
address=Entry(master,width=100)
address.pack()
if (pyperclip.paste()!=0):
    address.insert(END,pyperclip.paste())
    search()
b1=Button(master,text='Submit',width=25,command=search)
b1.pack()
master.mainloop()

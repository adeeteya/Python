#to generate a random name
import tkinter as tk
import random
def namegen():
    f=open("names.txt",'r')
    r2=random.randrange(0,4945)
    countline=0;name=''
    for line in f:
        if(countline==r2):
            name=line
            break
        countline+=1
    f.close()
    message=tk.Message(r,text=name,bg='black',fg='white').grid(row=1,column=0)
    #message.pack()
r = tk.Tk()
name=''
r.title('Random Name Generator')
button = tk.Button(r, text='Generate', width=25,command=namegen).grid()
#button.pack()
print()
r.mainloop()

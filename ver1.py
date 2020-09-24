from tkinter import *
from tkinter import messagebox
#%,mem,version:0.1
import traceback
counter = 0
def display(x):
    global expression
    expression+=str(x)
    Label(master,text=expression,bg='black',fg='red',width=30,height=4).grid(row=0,columnspan=5)
def remove():
    global expression
    expression=expression[0:len(expression)-1]
    Label(master,text=expression,bg='black',fg='red',width=30,height=4).grid(row=0,columnspan=5)
def clear():
    global expression
    expression=''
    Label(master,text=expression,bg='black',fg='red',width=30,height=4).grid(row=0,columnspan=5)
def evaluate():
    try:
        result=eval(expression)
    except ZeroDivisionError:
        messagebox.showerror('Error','Division by Zero not possible')
    except Exception:
        messagebox.showerror('Error','Invalid Syntax')
    Label(master,text=str(result),bg='black',fg='red',width=30,height=4).grid(row=0,columnspan=5)
master=Tk()
expression=''
master.title('Calculator')
master.configure(bg='black')
Label(master,text='0',bg='black',fg='red',width=30,height=4).grid(row=0,columnspan=5)
Button(master,command=lambda:display(1),height='5',width='5',text="1",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=3,column=2)
Button(master,command=lambda:display(2),height='5',width='5',text="2",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=3,column=1)
Button(master,command=lambda:display(3),height='5',width='5',text="3",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=3,column=0)
Button(master,command=lambda:display(4),height='5',width='5',text="4",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=2,column=2)
Button(master,command=lambda:display(5),height='5',width='5',text="5",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=2,column=1)
Button(master,command=lambda:display(6),height='5',width='5',text="6",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=2,column=0)
Button(master,command=lambda:display(7),height='5',width='5',text="7",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=1,column=2)
Button(master,command=lambda:display(8),height='5',width='5',text="8",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=1,column=1)
Button(master,command=lambda:display(9),height='5',width='5',text="9",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=1,column=0)
Button(master,command=lambda:display(0),height='5',width='5',text="0",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=4,column=0)
Button(master,command=lambda:display('.'),height='5',width='5',text=".",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=4,column=1)
Button(master,command=lambda:display(3.14),height='5',width='5',text="π",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=4,column=2)
Button(master,command=lambda:display('/'),height='5',width='5',text="÷",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=4,column=3)
Button(master,command=lambda:display('*'),height='5',width='5',text="x",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=3,column=3)
Button(master,command=lambda:display('-'),height='5',width='5',text="-",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=2,column=3)
Button(master,command=lambda:display('+'),height='5',width='5',text="+",bg='black',fg='white',activebackground='yellow',activeforeground='red',relief='raised').grid(row=1,column=3)
Button(master,command=evaluate,text="=",height='5',width='5',bg='yellow',fg='black',activebackground='black',activeforeground='red',relief='raised').grid(row=4,column=4)
Button(master,command=master.destroy,height='5',width='5',text='off',bg='yellow',fg='black',activebackground='black',activeforeground='red',relief='raised').grid(row=3,column=4)
Button(master,command=clear,text='clear',height='5',width='5',bg='yellow',fg='black',activebackground='black',activeforeground='red',relief='raised').grid(row=2,column=4)
Button(master,command=remove,text='⌫',height='5',width='5',bg='yellow',fg='black',activebackground='black',activeforeground='red',relief='raised').grid(row=1,column=4)
master.mainloop()

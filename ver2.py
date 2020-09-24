from tkinter import *
from tkinter import messagebox
#%,mem,version:0.2
#added keyboard input in version 0.2
def keydisplay(event):
    global expression
    temp=str(event)
    if(len(temp)==74):expression+=temp[59]
    elif(len(temp)==73):expression+=temp[58]
    elif(len(temp)==78):expression+=temp[63]
    elif(len(temp)==81):expression+=temp[66]
    elif(len(temp)==68):expression+=temp[53]
    Label(master,text=expression,bg='black',fg='red',width=30,height=4).grid(row=0,columnspan=5)
def display(x):
    global expression
    expression+=str(x)
    Label(master,text=expression,bg='black',fg='red',width=30,height=4).grid(row=0,columnspan=5)
def remove(event):
    global expression
    expression=expression[0:len(expression)-1]
    Label(master,text=expression,bg='black',fg='red',width=30,height=4).grid(row=0,columnspan=5)
def clear():
    global expression
    expression=''
    Label(master,text=expression,bg='black',fg='red',width=30,height=4).grid(row=0,columnspan=5)
def evaluate(event):
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
master.bind('1',keydisplay)
master.bind('2',keydisplay)
master.bind('3',keydisplay)
master.bind('4',keydisplay)
master.bind('5',keydisplay)
master.bind('6',keydisplay)
master.bind('7',keydisplay)
master.bind('8',keydisplay)
master.bind('9',keydisplay)
master.bind('0',keydisplay)
master.bind('+',keydisplay)
master.bind('-',keydisplay)
master.bind('/',keydisplay)
master.bind('*',keydisplay)
master.bind('=',evaluate)
master.bind('.',keydisplay)
master.bind('<BackSpace>',remove)
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
b2=Button(master,command=evaluate,text="=",height='5',width='5',bg='yellow',fg='black',activebackground='black',activeforeground='red',relief='raised')
b2.grid(row=4,column=4)
b2.bind("<Button-1>",evaluate)
Button(master,command=master.destroy,height='5',width='5',text='off',bg='yellow',fg='black',activebackground='black',activeforeground='red',relief='raised').grid(row=3,column=4)
Button(master,command=clear,text='clear',height='5',width='5',bg='yellow',fg='black',activebackground='black',activeforeground='red',relief='raised').grid(row=2,column=4)
b1=Button(master,text='⌫',height='5',width='5',bg='yellow',fg='black',activebackground='black',activeforeground='red',relief='raised')
b1.grid(row=1,column=4)
b1.bind("<Button-1>",remove)
master.mainloop()

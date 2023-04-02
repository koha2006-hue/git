#create menu GUI with tkinter
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Menu:
    def __init__(self, root):
        self.root=root
        self.root.title("Menu")
        self.root.geometry("500x500")
        self.root.resizable(0,0)
        self.root.config(bg="white")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.bind("<Escape>", self.exit)
#Label
        self.lbl1=Label(self.root,text="Welcome to PGSIM",font=("arial",20,"bold"),bg="white")
        self.lbl1.pack(side=TOP,fill=X)
        self.lbl2=Label(self.root,text="Please choose the type of certificate you want to generate",font=("arial",10,"bold"),bg="white")
        self.lbl2.pack(side=TOP,fill=X)
#Button
        Buttonframe=Frame(self.root,bd=20,relief=FLAT,)
        Buttonframe.pack(side=TOP,fill=X)
        self.btn1=Button(Buttonframe,text="Citizen",width=20,font=("arial",15,"bold"),command=self.generate)
        self.btn1.grid(row=0,column=2)
        self.btn2=Button(Buttonframe,text="Marriage",width=20,font=("arial",15,"bold"),command=self.generate)
        self.btn2.grid(row=1,column=2)
        self.btn3=Button(Buttonframe,text="Divorce",width=20,font=("arial",15,"bold"),command=self.generate)
        self.btn3.grid(row=2,column=2)
        self.btn4=Button(Buttonframe,text="Death",width=20,font=("arial",15,"bold"),command=self.generate)
        self.btn4.grid(row=3,column=2)
        self.btn5=Button(Buttonframe,text="Exit",width=20,font=("arial",15,"bold"),command=self.exit)
        self.btn5.grid(row=4,column=2)
        Buttonframe.pack()(side=TOP,fill=X,anchor = 'center')
#Function
    def generate(self):
        messagebox.showinfo("Information","This function is not available yet")
    def exit(self,event=None):
        self.root.destroy()
        exit()  
if __name__ == "__main__":
    root = Tk()
    app = Menu(root)
    root.mainloop()

import tkinter
# Importing all the modules from the tkinter library.
from tkinter import *
# Importing the ttk module from the tkinter library.
from tkinter import ttk
# Importing the random module.
import random
# Importing the time module.
import time 
# Importing the datetime module.
import datetime
# Importing the messagebox module from the tkinter library.
from tkinter import messagebox
# Importing the mysql.connector module.
import mysql.connector
from subfunction.subfunct import *
class Government:
    def __init__(self,root):
        self.citizen_name = StringVar()
        self.citizen_id = StringVar()
        self.citizen_DoB = StringVar()
        self.nationality = StringVar()
        self.place_of_origin = StringVar()
        self.place_of_residence = StringVar()
        self.marriage = StringVar()
        self.sex=StringVar()
        """
        The above function is used to create a window with a title and a size
        
        :param root: The root window is the main window of your application. It is the window that
        contains all other widgets
        """
        # The above function is used to create a window with a title and a size
        self.root=root
        # Setting the title of the window.
        self.root.title("public govermental services information management system")
        # Setting the size of the window.
        self.root.geometry(# Setting the size of the window.
        "1540x800+0+0")
 # The above code is creating a label with the text "government Management System" and the font size is
 
 
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="[PUBLIC GOVERMENTAL SERVICES INFORMATION MANAGEMENT SYSTE]",fg="red",bg="white",font=("times new roman",30,"bold"))

        lbltitle.pack(side=TOP,fill=X)
        
        # Create the Dataframe
        Dataframe=Frame(self.root,bd=20,relief=RIDGE,padx=20)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,text="Citizen Information",font=("times new roman",12,"bold"),fg="red")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
        
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,text="ID Card",font=("times new roman",12,"bold"),fg="red")
        DataframeRight.place(x=990,y=5,width=460,height=350)
        
        ## Create buttons frame
        # Creating a frame for the buttons.
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE,)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        ## create detail frame
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE,)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        ##Create DataframeLeft
        lblName=Label(DataframeLeft,text="Enter date of birth",font=("times new roman",12,"bold"),)
    
        lblName.grid(row=0,column=0,padx=10,pady=10,# Aligning the text to the left.
        sticky=W)
        
        # Creating a combo box for the day
        day = ttk.Combobox(DataframeLeft, width=2)
        day.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        # Create a combo box for the month
        month = ttk.Combobox(DataframeLeft, width=10)
        month.grid(row=0,column=2,padx=10,pady=10,sticky=NW)

        # Create a combo box for the year
        year = ttk.Combobox(DataframeLeft, width=4)
        year.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        # Create a list of days
        days = [i for i in range(1,32)]
        # Create a list of months
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        # Create a list of years
        years = [i for i in range(1900,2023)]

        # Set the values of the combo boxes
        day['values'] = days
        month['values'] = months
        year['values'] = years

        # Create a label for the day

        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Citizen Name",)
        lblref.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.citizen_name,width=26)
        txtref.grid(row=1,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Date of birth",)
        lblref.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.citizen_DoB,width=26)
        txtref.grid(row=2,column=1,padx=10,pady=10)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="ID",)
        lblref.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.citizen_id,width=26)
        txtref.grid(row=3,column=1,padx=10,pady=10)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Sex",)
        lblref.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sex,width=26)
        txtref.grid(row=4,column=1,padx=10,pady=10)


        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="nationality",)
        lblref.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.nationality,width=26)
        txtref.grid(row=5,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="marriage",)
        lblref.grid(row=6,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.marriage,width=26)
        txtref.grid(row=6,column=1,padx=10,pady=10)
        
       
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Place of origin",)
        lblref.grid(row=7,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.place_of_origin,width=26)
        txtref.grid(row=7,column=1,padx=10,pady=10)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ## Create DataframeRight
        # The above code is creating a text box with the name txtID_card.
        self.txtID_card=Text(DataframeRight,font=("arial",12,"bold"),width=46,height=16,padx=2,pady=6)
        
        self.txtID_card.grid(row=0,column=0)
        
        
        ## Create Buttonframe
        # The above code is creating a button with the name btnAdd1 and the text on the
        # button is "Add".
        btnAdd1 = Button(Buttonframe,command= self.AddData, text="Add", bg="green", fg="white", font=("arial", 12, "bold"), width=12, height=2, padx=2, pady=2)
        btnAdd1.grid(row=0, column=0)

        btnAdd2 = Button(Buttonframe, text="Show",command=self.show_data, bg="green", fg="white", font=("arial", 12, "bold"), width=12, height=4, padx=2, pady=2)
        btnAdd2.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update",command=self.update, bg="green", fg="white", font=("arial", 12, "bold"), width=12, height=4, padx=2, pady=2)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete",command=self.delete, bg="green", fg="white", font=("arial", 12, "bold"), width=12, height=4, padx=2, pady=2)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear",command= self.reset, bg="green", fg="white", font=("arial", 12, "bold"), width=12, height=4, padx=2, pady=2)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit",command=self.Exit, bg="green", fg="white", font=("arial", 12, "bold"), width=12, height=4, padx=2, pady=2)
        btnExit.grid(row=0, column=5)

        ## Create tabler
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.government_table=ttk.Treeview(Detailsframe,column=("Citizen name","date of birth","ID","Sex","nationnality","Place of origin","Marriage"),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.government_table.xview)
        scroll_y=ttk.Scrollbar(command=self.government_table.yview)
        
        self.government_table.heading("Citizen name",text="Citizen name")
        self.government_table.heading("date of birth",text="date of birth")
        self.government_table.heading("ID",text="ID")
        self.government_table.heading("Sex",text="Sex")
        self.government_table.heading("nationnality",text="nationnality")
        self.government_table.heading("Place of origin",text="Place of origin")
        self.government_table.heading("Marriage",text="Marriage")

        
        
        
        self.government_table['show']='headings'
        
        self.government_table.pack(fill=BOTH,expand=1)
        self.government_table.column("Citizen name",width=100)
        self.government_table.column("date of birth",width=100)
        self.government_table.column("nationnality",width=100)
        self.government_table.column("ID",width=100)
        self.government_table.column("Sex",width=100)
        self.government_table.column("Place of origin",width=100)
        self.government_table.column("Marriage",width=100)
        self.fetch_data()
        self.government_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.government_table.pack(fill=BOTH,expand=1)

    def AddData(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="mydata")
        my_cursor=conn.cursor()
        try:    
            my_cursor.execute("insert into pgsim values(%s,%s,%s,%s,%s,%s)",(
                                                                                self.citizen_name.get(),         
                                                                                self.citizen_DoB.get(),
                                                                                self.citizen_id.get(),
                                                                                self.sex.get(),
                                                                                self.nationality.get(),
                                                                                self.place_of_origin.get(),
                                                                                self.marriage.get()
                                                                                ))
            conn.commit()        
            messagebox.showinfo("Success","Record has been inserted")
        except mysql.connector.Error as error:
            if error.errno == 1062:
                messagebox.showerror("Error","Duplicate entry")
            else:
                messagebox.showerror("Error",error)
        self.fetch_data()                                            
        conn.close()

    def show_data(self):
        self.txtID_card.insert(END,"Citizen name: "+self.citizen_name.get()+"\n")
        self.txtID_card.insert(END,"Citizen ID: "+self.citizen_id.get()+"\n")
        self.txtID_card.insert(END,"Citizen date of birth: "+self.citizen_DoB.get()+"\n")
        self.txtID_card.insert(END,"Sex: "+ self.sex.get()+"\n")
        self.txtID_card.insert(END,"nationality: "+ self.nationality.get()+"\n")
        self.txtID_card.insert(END,"Place of origin: "+self.place_of_origin.get()+"\n")
        self.txtID_card.insert(END,"Marriage: "+self.marriage.get()+"\n")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute ("update pgsim set Name=%s, date_of_birth=%s,ID=%s, nationality=%s, Place_of_birth=%s, Marriage=%s where ID=%s",(
                                                                                self.citizen_name.get(),         
                                                                                self.citizen_DoB.get(),
                                                                                self.citizen_id.get(),
                                                                                self.nationality.get(),
                                                                                self.place_of_origin.get(),
                                                                                self.marriage.get(),
                                                                                self.citizen_id.get()
                                                                                ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Record has been updated")

    def reset(self):
        self.citizen_name.set("")
        self.citizen_id.set("")
        self.citizen_DoB.set("")
        self.nationality.set("")
        self.place_of_origin.set("")
        self.marriage.set("")

    def delete(self):
        if self.citizen_id.get()=="":
            messagebox.showinfo("Error","Please select a record to delete")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="mydata")
            my_cursor=conn.cursor()
            query="delete from pgsim where ID=%s"
            value=(self.citizen_id.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            conn.close()
            self.fetch_data()
            self.reset()
            messagebox.showinfo("Success","Record has been deleted")


    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("Exit","Do you want to exit")
        if self.Exit>0:
            self.root.destroy()
            return


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pgsim")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.government_table.delete(*self.government_table.get_children())
            for row in rows:
                self.government_table.insert('',END,values=row)
            conn.commit()
        conn.close()
    def get_cursor(self,ev=""):
        cursor_row=self.government_table.focus()
        contents=self.government_table.item(cursor_row)
        row=contents['values']
        self.citizen_name.set(row[0])
        self.citizen_DoB.set(row[1])
        self.citizen_id.set(row[2])
        self.nationality.set(row[3])
        self.place_of_origin.set(row[4])
        self.marriage.set(row[5])

# Create the root window
root = Tk()

# Create an instance of the government class
government = Government(root)


# Start the mainloop
root.mainloop()

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


class Hospital:
    def __init__(self,root):
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
 # The above code is creating a label with the text "Hospital Management System" and the font size is
 
 
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="PUBLIC GOVERMENTAL SERVICES INFORMATION MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",30,"bold"),wraplength=1300)

        lbltitle.pack(side=TOP,fill=X)
        
        # Create the Dataframe
        Dataframe=Frame(self.root,bd=20,relief=RIDGE,padx=20)
        Dataframe.place(x=0,y=130,width=1540,height=400)
        
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,text="Citizen Information",font=("times new roman",12,"bold"),fg="red")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
        
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,text="Prescription",font=("times new roman",12,"bold"),fg="red")
        DataframeRight.place(x=990,y=5,width=460,height=350)
        
        ## Create buttons frame
        # Creating a frame for the buttons.
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE,)
        Buttonframe.place(x=0,y=530,width=1540,height=80)
        
        ## create detail frame
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE,)
        Detailsframe.place(x=0,y=600,width=1540,height=190)
        
        ##Create DataframeLeft
        lblName=Label(DataframeLeft,text="Enter date of birth",font=("times new roman",12,"bold"),)
    
        lblName.grid(row=0,column=0,padx=10,pady=10,# Aligning the text to the left.
        sticky=W)
        
        

        # Create a combo box for the month
        month = ttk.Combobox(DataframeLeft, width=10)
        month.grid(row=0,column=1,padx=10,pady=10,sticky=W )

        # Create a combo box for the year
        year = ttk.Combobox(DataframeLeft, width=4)
        year.grid(row=0,column=2,padx=10,pady=2,sticky=W)

        # Create a list of days
        days = [i for i in range(1,32)]
        # Create a list of months
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        # Create a list of years
        years = [i for i in range(1900,2023)]

        # Set the values of the combo boxes
        
        month['values'] = months
        year['values'] = years

        # Create a label for the day

        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Citizen Name",)
        lblref.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=1,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Date of birth",)
        lblref.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=2,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="nationality",)
        lblref.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=3,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Place of origin",)
        lblref.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=3,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="marriage",)
        lblref.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=4,column=1,padx=10,pady=10)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="ID",)
        lblref.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=26)
        txtref.grid(row=5,column=1,padx=10,pady=10)
        
        
        
        
        ## Create DataframeRight
        # The above code is creating a text box with the name txtPrescription.
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=46,height=16,padx=2,pady=6)
        
        self.txtPrescription.grid(row=0,column=0)
        
        
        ## Create Buttonframe
        # The above code is creating a button with the name btnPrescription1 and the text on the
        # button is "Prescription".
       ## Create DataframeRight
        # The above code is creating a text box with the name txtPrescription.
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=46,height=16,padx=2,pady=6)
        
        self.txtPrescription.grid(row=0,column=0)
        
        btnPrescription1 = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=25, height=4, padx=2, pady=2,anchor= "center" )
        btnPrescription1.grid(row=0, column=0)
        

        btnPrescription2 = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=27, height=4, padx=2, pady=2,anchor="center")
        btnPrescription2.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=26, height=4, padx=2, pady=2,anchor="center")
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=26, height=4, padx=2, pady=2,anchor="center")
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=26, height=4, padx=2, pady=2,anchor="center")
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=30, height=4, padx=2, pady=2,anchor="center")
        btnExit.grid(row=0, column=5)

        ## Create tabler
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("Citizen name","date of birth","nationnality","Place of origin","Marriage","ID"),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("Citizen name",text="Citizen name")
        self.hospital_table.heading("date of birth",text="date of birth")
        self.hospital_table.heading("nationnality",text="nationnality")
        self.hospital_table.heading("Place of origin",text="Place of origin")
        self.hospital_table.heading("Marriage",text="Marriage")
        self.hospital_table.heading("ID",text="ID")
        
        
        self.hospital_table['show']='headings'
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.column("Citizen name",width=100)
        self.hospital_table.column("date of birth",width=100)
        self.hospital_table.column("nationnality",width=100)
        self.hospital_table.column("Place of origin",width=100)
        self.hospital_table.column("Marriage",width=100)
        self.hospital_table.column("ID",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        
        
# Create the root window
root = Tk()

# Create an instance of the Hospital class
hospital = Hospital(root)


# Start the mainloop
root.mainloop()

from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
from subfunction.subfunct import province,century,random_6,last_two_digit
from datetime import date

class BirthDeclaration:
    def __init__(self, root):
        self.root = root
        self.root.title("Birth Declaration Form")
        self.root.geometry("1295x550+230+220")

        #variables
        self.entry_name_var=StringVar()
        self.entry_id_var=StringVar()
        self.entry_father_name_var=StringVar()
        self.entry_mother_name_var=StringVar()
        self.entry_date_var=StringVar()
        self.entry_place_var=StringVar()


        # Create form labels
        label_title = Label(self.root, text="Birth Declaration Form", font=("Arial", 20, "bold"))
        label_title.pack(side=TOP, pady=20)

        lableframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,font=("times new roman",12,"bold"),padx=2)
        lableframeleft.place(x=10,y=10,width=450,height=500)

        lableframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show",font=("times new roman",12,"bold"),padx=2)
        lableframeright.place(x=470,y=10,width=800,height=500)
#==================================================================
        self.birth_table=ttk.Treeview(lableframeright,columns=("name","id","father_name","mother_name","date","place"))
        self.birth_table.heading("name",text="Name")
        self.birth_table.heading("id",text="ID")
        self.birth_table.heading("father_name",text="Father's Name")
        self.birth_table.heading("mother_name",text="Mother's Name")
        self.birth_table.heading("date",text="Date of Birth")
        self.birth_table.heading("place",text="Place of Birth")
        self.birth_table["show"]="headings"
        self.birth_table.column("name",width=100)
        self.birth_table.column("id",width=100)
        self.birth_table.column("father_name",width=100)
        self.birth_table.column("mother_name",width=100)
        self.birth_table.column("date",width=100)
        self.birth_table.column("place",width=100)
        self.fetch_data()
        self.birth_table.pack(fill=BOTH,expand=1)
        self.birth_table.bind("<ButtonRelease-1>",self.get_cursor)
       
#==================================================================

        label_title=Label(lableframeleft,text="Birth Declaration Form",font=("times new roman",20,"bold"),bg="yellow",fg="red")
        label_title.pack(side=TOP,fill=X)

        #create name label and entry
        label_name=Label(lableframeleft,text="Name",font=("arial",12,"bold"))
        label_name.pack(side=TOP,anchor="w")
        entry_name=Entry(lableframeleft,textvariable=self.entry_name_var,font=("arial",12,"bold"),bd=5,relief=GROOVE)
        entry_name.pack(side=TOP,fill=X,padx=10,pady=5)

        #create id label and entry
        label_id=Label(lableframeleft,text="ID",font=("arial",12,"bold"))
        label_id.pack(side=TOP,anchor="w")
        entry_id=Entry(lableframeleft,textvariable=self.entry_id_var,font=("arial",12,"bold"),bd=5,relief=GROOVE)
        entry_id.pack(side=TOP,fill=X,padx=10,pady=5)

        #create father's name label and entry
        label_father_name=Label(lableframeleft,text="Father's Name",font=("arial",12,"bold"))
        label_father_name.pack(side=TOP,anchor="w")
        entry_father_name=Entry(lableframeleft,textvariable=self.entry_father_name_var,font=("arial",12,"bold"),bd=5,relief=GROOVE)
        entry_father_name.pack(side=TOP,fill=X,padx=10,pady=5)
        
        #create mother's name label and entry
        label_mother_name=Label(lableframeleft,text="Mother's Name",font=("arial",12,"bold"))
        label_mother_name.pack(side=TOP,anchor="w")
        entry_mother_name=Entry(lableframeleft,textvariable=self.entry_mother_name_var,font=("arial",12,"bold"),bd=5,relief=GROOVE)
        entry_mother_name.pack(side=TOP,fill=X,padx=10,pady=5)

        #create date of birth label and entry
        label_date=Label(lableframeleft,text="Date of Birth",font=("arial",12,"bold"))
        label_date.pack(side=TOP,anchor="w")
        entry_date=Entry(lableframeleft,textvariable=self.entry_date_var,font=("arial",12,"bold"),bd=5,relief=GROOVE)
        entry_date.pack(side=TOP,fill=X,padx=10,pady=5)

        #create place of birth label and entry
        label_place=Label(lableframeleft,text="Place of Birth",font=("arial",12,"bold"))
        label_place.pack(side=TOP,anchor="w")
        #Day combobox
        combo_day=ttk.Combobox(lableframeleft,font=("arial",12,"bold"),state="readonly")
        combo_day["value"]=tuple (range(1,32))
        combo_day.pack(side=RIGHT,fill=X,padx=5,pady=5)
        #Month combobox
        combo_month=ttk.Combobox(lableframeleft,font=("arial",12,"bold"),state="readonly")
        combo_month["value"]=('January','February','March','April','May','June','July','August','September','October','November','December')
        combo_month.pack(side=RIGHT,fill=X,padx=5,pady=5)
        


        


        #create place of birth by combobox (province only), others are text
        combo_province=ttk.Combobox(lableframeleft,font=("arial",12,"bold"),state="readonly")
        combo_province["value"]=('Ha Noi','Ha Giang','Cao Bang','Bac Kan','Tuyen Quang','Lao Cai','Dien Bien','Lai Chau','Son La','Yen Bai','Hoa Binh','Thai Nguyen','Lang Son','Quang Ninh','Bac Giang','Phu Tho','Vinh Phuc','Bac Ninh','Hai Duong','Hai Phong','Hung Yen','Thai Binh','Ha Nam','Nam Dinh','Ninh Binh','Thanh Hoa','Nghe An','Ha Tinh','Quang Binh','Quang Tri','Thua Thien Hue','Da Nang','Quang Nam','Quang Ngai','Binh Dinh','Phu Yen','Khanh Hoa','Ninh Thuan','Binh Thuan','Ninh Thuan','Kon Tum','Gia Lai','Dak Lak','Dak Nong','Binh Phuoc','Tay Ninh','Binh Duong','Dong Nai','Ba Ria-Vung Tau','Ho Chi Minh','Tien Giang','Ben Tre','Tra Vinh','Vinh Long','Dong Thap','An Giang','Kien Giang','Can Tho','Hau Giang','Soc Trang','Bac Lieu','Ca Mau')
        combo_province.current(0)
        self.province = combo_province.get()
        def update_province(event):
            self.province=combo_province.get()
        combo_province.bind("<<ComboboxSelected>>",update_province)

        
        

       

    def fetch_data(self):
        connect=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="mydata")
        my_cursor=connect.cursor()
        my_cursor.execute("SELECT * FROM birth")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.birth_table.delete(*self.birth_table.get_children())
            for row in rows:
                self.birth_table.insert('',END,values=row)
            connect.commit()
        connect.close()
    def get_cursor(self):
        cursor_row=self.birth_table.focus()
        content=self.birth_table.item(cursor_row)
        row=content["values"]
        self.entry_name_var.set(row[0])
        self.id=row[1]
        self.entry_father_name_var.set(row[2])
        self.entry_mother_name_var.set(row[3])
        self.date=row[4]
        self.entry_place_var.set(row[5])


    def add_data(self):
        connect=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="mydata")
        my_cursor=connect.cursor()
        my_cursor.execute("INSERT INTO birth VALUES(%s,%s,%s,%s,%s,%s)",(
            self.entry_name_var.get(),
            self.id,
            self.entry_father_name_var.get(),
            self.entry_mother_name_var.get(),
            self.entry_date_var.get(),
            self.entry_place_var.get()
        ))
        connect.commit()
        self.fetch_data()
        connect.close()

        # Clear form fields
        self.entry_date_var.set("")
        self.entry_father_name_var.set("")
        self.entry_mother_name_var.set("")
        self.entry_name_var.set("")
        self.entry_place_var.set("")
        self.id=""

root = Tk()
BirthDeclaration(root)
root.mainloop()


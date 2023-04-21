import sqlite3
from tkinter import *
from tkinter import ttk

from tkcalendar import DateEntry


class ManageUsers(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Manage Users')
        self.geometry("1100x500+5+5")
        self.resizable(False, False)
        # Add Some Style
        style = ttk.Style()
        # Pick A Theme
        style.theme_use('default')
        # Configure the Treeview Colors
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
        style.map('Treeview', background=[('selected', "#347083")])
        # now creating frames
        self.upframe = Frame(self)
        self.midframe = LabelFrame(self, text='Entries')
        self.lowframe = LabelFrame(self, text='Actions')
        # Configuring these Frames
        self.upframe.pack(pady=10)
        self.midframe.pack(fill="x", expand=1, padx=20)
        self.lowframe.pack(fill="x", expand=1, padx=20)
        # Adding Components to the first frame
        self.trscrol = Scrollbar(self.upframe)
        self.data = ttk.Treeview(self.upframe, yscrollcommand=self.trscrol.set, selectmode="extended")
        self.trscrol.pack(side=RIGHT, fill=Y)
        self.data.pack()
        self.trscrol.config(command=self.data.yview)
        self.data['columns'] = ("ID", "Name", "Password", "Phone No", "Job Level", "Joining Date", "DOB", "Address")
        # Properties of column for tree
        self.data.column("#0", width=0, stretch=NO)
        self.data.column("ID", anchor=W, width=60)
        self.data.column("Name", anchor=W, width=140)
        self.data.column("Password", anchor=W, width=140)
        self.data.column("Phone No", anchor=CENTER, width=120)
        self.data.column("Job Level", anchor=CENTER, width=110)
        self.data.column("Joining Date", anchor=CENTER, width=100)
        self.data.column("DOB", anchor=CENTER, width=100)
        self.data.column("Address", anchor=W, width=200)
        # Creating Headings for for columns
        self.data.heading("#0", text="", anchor=W)
        self.data.heading("ID", text="ID", anchor=W)
        self.data.heading("Name", text="Name", anchor=W)
        self.data.heading("Password", text="Password", anchor=W)
        self.data.heading("Phone No", text="Phone No", anchor=W)
        self.data.heading("Job Level", text="Job Level", anchor=CENTER)
        self.data.heading("Joining Date", text="Joining Date", anchor=CENTER)
        self.data.heading("DOB", text="DOB", anchor=CENTER)
        self.data.heading("Address", text="Address", anchor=CENTER)
        # For adding color in rows
        self.data.tag_configure('oddrow', background="white")
        self.data.tag_configure('evenrow', background="lightblue")
        # we will add components to the seconod Frame
        self.name_Label = Label(self.midframe, text="Name:")
        self.password_Label = Label(self.midframe, text="Password:")
        self.phone_Label = Label(self.midframe, text="Phone No:")
        self.jobl_Label = Label(self.midframe, text="Job Level:")
        self.dob_Label = Label(self.midframe, text="DOB:")
        self.address_Label = Label(self.midframe, text="Address:")
        # Creating the entries
        self.name_Entry = Entry(self.midframe)
        self.password_Entry = Entry(self.midframe)
        self.phone_Entry = Entry(self.midframe)
        self.jobl_Entry = ttk.Combobox(self.midframe, state='readonly', values=("Admin", "Salesmen"), width=21)
        self.dob_Entry = DateEntry(self.midframe)
        self.address_Entry = Entry(self.midframe)
        # Configuring the Gui
        self.name_Label.grid(row=0, column=0, padx=10, pady=10)
        self.name_Entry.grid(row=0, column=1, padx=10, pady=10)
        self.password_Label.grid(row=0, column=2, padx=10, pady=10)
        self.password_Entry.grid(row=0, column=3, padx=10, pady=10)
        self.phone_Label.grid(row=0, column=4, padx=10, pady=10)
        self.phone_Entry.grid(row=0, column=5, padx=10, pady=10)
        self.jobl_Label.grid(row=0, column=6, padx=10, pady=10)
        self.jobl_Entry.grid(row=0, column=7, padx=10, pady=10)
        self.dob_Label.grid(row=1, column=0, padx=10, pady=10)
        self.dob_Entry.grid(row=1, column=1, padx=10, pady=10)
        self.address_Label.grid(row=1, column=2, padx=10, pady=10)
        self.address_Entry.grid(row=1, column=3, padx=10, pady=10)
        # now the third frame
        self.add_Button = ttk.Button(self.lowframe, text='Add User', command=self.add_User)
        self.search_Button = ttk.Button(self.lowframe, text='Search User', command=self.search_User)
        self.delete_Button = ttk.Button(self.lowframe, text='Delete User', command=self.delete_User)
        self.select_Button = ttk.Button(self.lowframe, text='Select record', command=self.select_record)
        self.refresh_Button = ttk.Button(self.lowframe, text="Refresh", command=self.refresh_tree)
        self.clear_Button = ttk.Button(self.lowframe, text="Clear Entries", command=self.clear_Entries)
        self.progress_label = Label(self.lowframe, text="Press the required Button")
        self.close_Button = Button(self.lowframe, text='Close This Window', bg='red', command=self.close_Window)
        # configuring components
        self.add_Button.grid(row=0, column=1, padx=10, pady=10)
        self.search_Button.grid(row=0, column=2, padx=10, pady=10)
        self.delete_Button.grid(row=0, column=3, padx=10, pady=10)
        self.select_Button.grid(row=0, column=4, padx=10, pady=10)
        self.refresh_Button.grid(row=0, column=5, padx=10, pady=10)
        self.clear_Button.grid(row=0, column=6, padx=10, pady=10)
        self.progress_label.grid(row=0, column=7, padx=10, pady=10)
        self.close_Button.grid(row=0, column=8, padx=10, pady=10)
        # connecting to database
        conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Users")
        meddata = cur.fetchall()
        count = 0
        finedata = sorted(meddata, key=lambda x: x[1])
        for data in finedata:
            if count % 2 == 0:
                self.data.insert(parent='', index='end',
                                 values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]),
                                 tags='evenrow')
            else:
                self.data.insert(parent='', index='end',
                                 values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]),
                                 tags='oddrow')
            count += 1
        conn.commit()
        conn.close()
        self.data.tag_configure('oddrow', background='lightgrey')
        self.data.tag_configure('evenrow', background='lightblue')
        self.clear_Entries()
        # now we will bind the enter key
        self.name_Entry.focus()

    def add_User(self):
        name = self.name_Entry.get()
        phoneno = self.phone_Entry.get()
        password = self.password_Entry.get()
        jobl = self.jobl_Entry.get()
        dob = self.dob_Entry.get()
        address = self.address_Entry.get()
        SpecialSym = ['$', '@', '#', '%']
        conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
        cur = conn.cursor()
        if name and password and phoneno and jobl and dob and address != "":
            usercheckstat = f"SELECT *FROM Users WHERE Name ='{name}';"
            cur.execute(usercheckstat)
            if not cur.fetchone():
                if 20 > len(name) > 5:
                    if 20 > len(password) > 5:
                        if any(char in SpecialSym for char in password):
                            if phoneno.isdigit():
                                if len(phoneno) == 11:
                                    adduserstat = f"INSERT INTO Users(Name, Password, PhoneNo, Job_Level, DOB, Address) VALUES(?,?,?,?,?,?)"
                                    cur.execute(adduserstat, (name, password, phoneno, jobl, dob, address))
                                    conn.commit()
                                    self.refresh_tree()
                                    self.clear_Entries()
                                    self.progress_label.config(text="Person Added Successfully", bg='Green')
                                else:
                                    self.progress_label.config(text="Phone number must be of length 11", bg='red')
                            else:
                                self.progress_label.config(text="Phone number must be digit", bg='red')
                        else:
                            self.progress_label.config(text="Password must have special characters ", bg='red')
                    else:
                        self.progress_label.config(text="Password must be between 6-20", bg='red')
                else:
                    self.progress_label.config(text="Name must be between 6 to 20", bg='red')
            else:
                self.progress_label.config(text="Name Already Exist", bg='red')
        else:
            self.progress_label.config(text="Incomplete Form", bg='red')

    def search_User(self):
        for i in self.data.get_children():
            self.data.delete(i)
        name = self.name_Entry.get()
        if name != '':
            conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
            cur = conn.cursor()
            search_statement = f"SELECT *FROM Users WHERE Name LIKE '{name}';"
            cur.execute(search_statement)
            conn.commit()
            meddata = cur.fetchall()
            count = 0
            finedata = sorted(meddata, key=lambda x: x[1])
            for data in finedata:
                if count % 2 == 0:
                    self.data.insert(parent='', index='end',
                                     values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]),
                                     tags='evenrow')
                else:
                    self.data.insert(parent='', index='end',
                                     values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]),
                                     tags='oddrow')
                count += 1
            conn.commit()
            conn.close()
            self.progress_label.config(text="Successfull")
        else:
            self.progress_label.config(text="Not Exist", )

    def delete_User(self):

        selectedrecord = self.data.focus()
        if selectedrecord != "":
            values = self.data.item(selectedrecord, 'values')
            self.name_Entry.insert(0, values[1])
        name = self.name_Entry.get()
        if name != "":
            conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
            statment1 = f"DELETE FROM Users WHERE NAME = '{name}';"
            cur = conn.cursor()
            cur.execute(statment1)
            conn.commit()
            if not cur.fetchone():
                self.progress_label.config(text='Not found', bg='red')
            else:
                self.progress_label.config(text='Successfull', bg='green')
                self.clear_Entries()
        else:
            self.progress_label.config(text='Enter the Name')
        self.refresh_tree()
        self.clear_Entries()

    def select_record(self):
        self.clear_Entries()
        selectedrecord = self.data.focus()
        if selectedrecord != "":
            values = self.data.item(selectedrecord, 'values')
            self.name_Entry.insert(0, values[1])
            self.password_Entry.insert(0, values[2])
            self.phone_Entry.insert(0, values[3])
            self.jobl_Entry.set(value=(values[4]))
            self.dob_Entry.insert(0, values[6])
            self.address_Entry.insert(0, values[7])
        else:
            self.progress_label.config(text="Select a Record", bg='red')

    def refresh_tree(self):
        # to clear the previous data of tree view
        for i in self.data.get_children():
            self.data.delete(i)
        conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Users")
        meddata = cur.fetchall()
        count = 0
        # embeding updated data to tree view
        finedata = sorted(meddata, key=lambda x: x[1])
        for data in finedata:
            if count % 2 == 0:
                self.data.insert(parent='', index='end',
                                 values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]),
                                 tags='evenrow')
            else:
                self.data.insert(parent='', index='end',
                                 values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]),
                                 tags='oddrow')
            count += 1
        conn.commit()
        conn.close()
        self.progress_label.config(bg="green", text="Successful")

    def clear_Entries(self):
        self.name_Entry.delete(0, END)
        self.password_Entry.delete(0, END)
        self.phone_Entry.delete(0, END)
        self.jobl_Entry.delete(0, END)
        self.dob_Entry.delete(0, END)
        self.address_Entry.delete(0, END)
        self.progress_label.config(text='')

    def close_Window(self):
        self.destroy()

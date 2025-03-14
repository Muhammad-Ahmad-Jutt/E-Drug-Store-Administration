import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
class Stock(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Manage Stock')
        self.geometry("1200x500+5+5")
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
        self.midframe.pack(fill="x", expand=3, padx=20)
        self.lowframe.pack(fill="x", expand=3, padx=20)
        # Adding Components to the first frame
        self.trscrol = Scrollbar(self.upframe)
        self.data = ttk.Treeview(self.upframe, yscrollcommand=self.trscrol.set, selectmode="extended")
        self.trscrol.pack(side=RIGHT, fill=Y)
        self.data.pack()
        self.trscrol.config(command=self.data.yview)
        self.data['columns'] = ("ID", "Name", "Type", "Quantity", "Purchase Price", "Sell Price", "Salt", "Company")
        # Properties of columns for tree
        self.data.column("#0", width=0, stretch=NO)
        self.data.column("ID", anchor=W, width=80)
        self.data.column("Name", anchor=W, width=180)
        self.data.column("Type", anchor=CENTER, width=100)
        self.data.column("Quantity", anchor=CENTER, width=100)
        self.data.column("Purchase Price", anchor=CENTER, width=100)
        self.data.column("Sell Price", anchor=CENTER, width=100)
        self.data.column("Salt", anchor=CENTER, width=140)
        self.data.column("Company", anchor=CENTER, width=220)
        # Creating Headings for tree
        self.data.heading("#0", text="", anchor=W)
        self.data.heading("ID", text="ID", anchor=W)
        self.data.heading("Name", text="Name", anchor=W)
        self.data.heading("Type", text="Type", anchor=CENTER)
        self.data.heading("Quantity", text="Quantity", anchor=CENTER)
        self.data.heading("Purchase Price", text="Purchase Price", anchor=CENTER)
        self.data.heading("Sell Price", text="Sell Price", anchor=CENTER)
        self.data.heading("Salt", text="Salt", anchor=CENTER)
        self.data.heading("Company", text="Company", anchor=CENTER)
        # For adding color in rows
        self.data.tag_configure('oddrow', background="white")
        self.data.tag_configure('evenrow', background="lightblue")
        # we will add components to the seconod Frame
        # creating labels
        self.id_Label = Label(self.midframe, text="ID :")
        self.name_Label = Label(self.midframe, text="Name :")
        self.type_Label = Label(self.midframe, text="Type")
        self.quantity_Label = Label(self.midframe, text="Quantity")
        self.pprice_Label = Label(self.midframe, text="Purchase Price")
        self.sprice_Label = Label(self.midframe, text='Sale Price')
        self.salt_Label = Label(self.midframe, text="Salt")
        self.company_Label = Label(self.midframe, text="Company")
        # creating entries
        self.id_Entry = Entry(self.midframe, state='disabled')
        self.name_Entry = Entry(self.midframe)
        self.type_Entry = Entry(self.midframe)
        self.quantity_Entry = Entry(self.midframe)
        self.pprice_Entry = Entry(self.midframe)
        self.sprice_Entry = Entry(self.midframe)
        self.salt_Entry = Entry(self.midframe)
        self.company_Entry = Entry(self.midframe)
        # Configuring the Gui
        self.id_Label.grid(row=0, column=0, padx=10, pady=10)
        self.id_Entry.grid(row=0, column=1, padx=10, pady=10)
        self.name_Label.grid(row=0, column=2, padx=10, pady=10)
        self.name_Entry.grid(row=0, column=3, padx=10, pady=10)
        self.type_Label.grid(row=0, column=4, padx=10, pady=10)
        self.type_Entry.grid(row=0, column=5, padx=10, pady=10)
        self.quantity_Label.grid(row=0, column=6, padx=10, pady=10)
        self.quantity_Entry.grid(row=0, column=7, padx=10, pady=10)
        self.pprice_Label.grid(row=1, column=0, padx=10, pady=10)
        self.pprice_Entry.grid(row=1, column=1, padx=10, pady=10)
        self.sprice_Label.grid(row=1, column=2, padx=10, pady=10)
        self.sprice_Entry.grid(row=1, column=3, padx=10, pady=10)
        self.salt_Label.grid(row=1, column=4, padx=10, pady=10)
        self.salt_Entry.grid(row=1, column=5, padx=10, pady=10)
        self.company_Label.grid(row=1, column=6, padx=10, pady=10)
        self.company_Entry.grid(row=1, column=7, padx=10, pady=10)
        # now adding components to our last Frame
        self.add_Button = ttk.Button(self.lowframe, text='Add Item', command=self.add_Item)
        self.update_Button = ttk.Button(self.lowframe, text='Update Item', command=self.update_Item)
        self.search_Button = ttk.Button(self.lowframe, text='Search Item', command=self.search_Med)
        self.delete_Button = ttk.Button(self.lowframe, text='Delete Item', command=self.delete_record)
        self.select_Button = ttk.Button(self.lowframe, text='Select record', command=self.selected_record)
        self.refresh_Button = ttk.Button(self.lowframe, text="Refresh", command=self.refreshtree)
        self.clear_Button = ttk.Button(self.lowframe, text="Clear Entries", command=self.empty_Entries)
        self.purch_Button = ttk.Button(self.lowframe, text="Add Purchase", command=self.addPurchase)
        self.progress_label = Label(self.lowframe, text="Press the required Button")
        self.close_Button = Button(self.lowframe, text='Close', bg='red', command=self.exit_window)
        # configuring components
        self.add_Button.grid(row=0, column=1, padx=10, pady=10)
        self.update_Button.grid(row=0, column=2, padx=10, pady=10)
        self.search_Button.grid(row=0, column=3, padx=10, pady=10)
        self.delete_Button.grid(row=0, column=4, padx=10, pady=10)
        self.select_Button.grid(row=0, column=5, padx=10, pady=10)
        self.refresh_Button.grid(row=0, column=6, padx=10, pady=10)
        self.clear_Button.grid(row=0, column=7, padx=10, pady=10)
        self.purch_Button.grid(row=0, column=8, padx=10, pady=10)
        self.progress_label.grid(row=0, column=9, padx=10, pady=10)
        self.close_Button.grid(row=0, column=10, padx=10, pady=10)
        # now we will work on the retrieval of data, but firstly we have to make a
        conn = sqlite3.connect(f'{BASE_DIR}/Database/pharma.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM medicine")
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

    def refreshtree(self):
        # to clear the previous data of tree view
        for i in self.data.get_children():
            self.data.delete(i)
        conn = sqlite3.connect(f'{BASE_DIR}/Database/pharma.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM medicine")
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

    def add_Item(self):
        it_Name = self.name_Entry.get()
        it_Type = self.type_Entry.get()
        it_Quantity = self.quantity_Entry.get()
        it_PPrice = self.pprice_Entry.get()
        it_SPrice = self.sprice_Entry.get()
        it_Salt = self.salt_Entry.get()
        it_Company = self.company_Entry.get()
        if it_Name and it_Type and it_Quantity and it_PPrice and it_SPrice and it_Salt and it_Company != "":
            conn = sqlite3.connect(f'{BASE_DIR}/Database/pharma.db')
            cur = conn.cursor()
            check_statement = f"SELECT *FROM medicine WHERE Name='{it_Name}';"
            cur.execute(check_statement)
            if not cur.fetchone():
                if it_Quantity.isdigit():
                    if self.isfloat(it_PPrice):
                        if self.isfloat(it_SPrice):
                            insert_statement = f"INSERT INTO medicine(Name,Type,Quantity,purchase_Price,sell_Price,Salt,Company) VALUES(?,?,?,?,?,?,?)"
                            cur.execute(insert_statement, (
                                 it_Name, it_Type, it_Quantity, it_PPrice, it_SPrice, it_Salt, it_Company))
                            inserttopurchase = f"INSERT INTO Purchase(Name, Type, Quantity, purchase_Price, sell_Price) VALUES(?,?,?,?,?)"
                            cur.execute(inserttopurchase, (it_Name, it_Type, it_Quantity, it_PPrice, it_SPrice))
                            conn.commit()
                            self.refreshtree()
                            self.empty_Entries()
                            if not cur.fetchone():
                                self.progress_label.config(bg='green', text="Added Successfully")
                            else:
                                messagebox.showerror("Unsuccessful", "Error while adding to database", parent=self)
                        else:
                            messagebox.showerror("Wrong Input", "Sale must be an Integer", parent=self)
                    else:
                        messagebox.showerror("Wrong Input", "Purchase must be an Integer", parent=self)
                else:
                    messagebox.showerror("Wrong Input", "Quantity must be an Integer", parent=self)
            else:
                messagebox.showinfo("Already exist", "This Name is already occupied Try different", parent=self)
        else:
            messagebox.showwarning("Incomplete", "Please fill all the fields", parent=self)

    def update_Item(self):
        it_Name = self.name_Entry.get()
        it_Type = self.type_Entry.get()
        it_PPrice = self.pprice_Entry.get()
        it_SPrice = self.sprice_Entry.get()
        it_Salt = self.salt_Entry.get()
        it_Company = self.company_Entry.get()
        if it_Name and it_Type and it_PPrice and it_SPrice and it_Salt and it_Company != "":
            conn = sqlite3.connect(f'{BASE_DIR}/Database/pharma.db')
            cur = conn.cursor()
            check_statement = f"SELECT *FROM medicine WHERE Name Like '{it_Name}';"
            cur.execute(check_statement)
            if cur.fetchone():
                check_statement = f"SELECT ID FROM medicine WHERE Name Like '{it_Name}';"
                it_id = cur.execute(check_statement).fetchone()
                quantity_st = f"SELECT Quantity FROM medicine WHERE ID Like '{it_id[0]}';"
                quan = cur.execute(quantity_st).fetchone()
                quanint = int(quan[0])
                if self.isfloat(it_PPrice):
                    if self.isfloat(it_SPrice):
                        insert_statement = f"UPDATE medicine SET Name=?, Type = ?, Quantity=?, purchase_Price=?, sell_Price=?, Salt=?, Company=? WHERE ID='{it_id[0]}';"
                        cur.execute(insert_statement,
                                    (it_Name, it_Type, quanint, it_PPrice, it_SPrice, it_Salt, it_Company))
                        self.refresh_record()
                        self.empty_Entries()
                        conn.commit()
                        conn.close()
                    else:
                        messagebox.showerror("Wrong Input", "Sale must be an Integer", parent=self)
                else:
                    messagebox.showerror("Wrong Input", "Purchase must be an Integer", parent=self)
            else:
                messagebox.showinfo("Not exist", "Can't find the Item to update", parent=self)
        else:
            messagebox.showwarning("Incomplete", "Please fill all the fields", parent=self)
    def addPurchase(self):
        it_Name = self.name_Entry.get()
        it_Type = self.type_Entry.get()
        it_Quantity = self.quantity_Entry.get()
        it_PPrice = self.pprice_Entry.get()
        it_SPrice = self.sprice_Entry.get()
        it_Salt = self.salt_Entry.get()
        it_Company = self.company_Entry.get()
        if it_Name and it_Type and it_Quantity and it_PPrice and it_SPrice and it_Salt and it_Company != "":
            conn = sqlite3.connect(f'{BASE_DIR}/Database/pharma.db')
            cur = conn.cursor()
            check_statement = f"SELECT *FROM medicine WHERE Name Like '{it_Name}';"
            cur.execute(check_statement)
            if cur.fetchone():
                check_statement = f"SELECT ID FROM medicine WHERE Name Like '{it_Name}';"
                it_id = cur.execute(check_statement).fetchone()
                if it_Quantity.isdigit():
                    if self.isfloat(it_PPrice):
                        if self.isfloat(it_SPrice):
                            insert_statement = f"UPDATE medicine SET Name=?, Type = ?, Quantity=Quantity + ?, purchase_Price=?, sell_Price=?, Salt=?, Company=? WHERE ID='{it_id[0]}';"
                            cur.execute(insert_statement,
                                        (it_Name, it_Type, it_Quantity, it_PPrice, it_SPrice, it_Salt, it_Company))
                            inserttopurchase = f"INSERT INTO Purchase(Name, Type, Quantity, purchase_Price, sell_Price) VALUES(?,?,?,?,?)"
                            cur.execute(inserttopurchase, (it_Name, it_Type, it_Quantity, it_PPrice, it_SPrice))
                            conn.commit()
                            self.refresh_record()
                            self.empty_Entries()
                            conn.close()
                        else:
                            messagebox.showerror("Wrong Input", "Sale must be an Integer", parent=self)
                    else:
                        messagebox.showerror("Wrong Input", "Purchase must be an Integer", parent=self)
                else:
                    messagebox.showerror("Wrong Input", "Quantity must be an Integer", parent=self)
            else:
                messagebox.showinfo("Not exist", "Can't find the Item to update", parent=self)
        else:
            messagebox.showwarning("Incomplete", "Please fill all the fields", parent=self)

    def selected_record(self):
        self.empty_Entries()
        selectedrow = self.data.focus()
        self.id_Entry.config(state='normal')
        if selectedrow != "":
            values = self.data.item(selectedrow, 'values')
            self.id_Entry.insert(0, values[0])
            self.name_Entry.insert(0, values[1])
            self.type_Entry.insert(0, values[2])
            self.quantity_Entry.insert(0, values[3])
            self.pprice_Entry.insert(0, values[4])
            self.sprice_Entry.insert(0, values[5])
            self.salt_Entry.insert(0, values[6])
            self.company_Entry.insert(0, values[7])
        else:
            messagebox.showerror("Empty Selection", "You Have Not Selected Any Record", parent=self)
        self.id_Entry.config(state='disabled')

    def refresh_record(self):
        selected = self.data.focus()
        self.data.item(selected, text="", values=(
            self.id_Entry.get(), self.name_Entry.get(), self.type_Entry.get(), self.quantity_Entry.get(),
            self.pprice_Entry.get(), self.sprice_Entry.get(), self.salt_Entry.get(), self.company_Entry.get()))
        self.progress_label.config(bg='green', text="Updated Successfully")

    def exit_window(self):
        self.destroy()

    def delete_record(self):
        selectedrow = self.data.focus()
        self.id_Entry.config(state='normal')
        if selectedrow != "":
            values = self.data.item(selectedrow, 'values')
            self.id_Entry.insert(0, values[0])
            self.name_Entry.insert(0, values[1])
        id = self.id_Entry.get()
        name = self.name_Entry.get()
        conn = sqlite3.connect(f'{BASE_DIR}/Database/pharma.db')
        cur = conn.cursor()
        if id != '':
            int_ID = int(id)
            istatement = f"DELETE FROM medicine WHERE ID = '{int_ID}';"
            cur.execute(istatement)
            conn.commit()
            self.refreshtree()
            self.progress_label.config(text="Item Deleted Successfully")
        elif name != '':
            nstatement = f"DELETE FROM medicine WHERE Name = '{name}';"
            cur.execute(nstatement)
            conn.commit()
            self.refreshtree()
            self.progress_label.config(text="Item Deleted Successfully")
        else:
            self.progress_label.config(text="ID or Name is Required")

        self.refreshtree()
        self.empty_Entries()
        conn.commit()
        conn.close()
        self.id_Entry.config(state='disabled')

    def empty_Entries(self):
        self.id_Entry.config(state='normal')
        self.id_Entry.delete(0, END)
        self.name_Entry.delete(0, END)
        self.type_Entry.delete(0, END)
        self.quantity_Entry.delete(0, END)
        self.pprice_Entry.delete(0, END)
        self.sprice_Entry.delete(0, END)
        self.salt_Entry.delete(0, END)
        self.company_Entry.delete(0, END)
        self.id_Entry.config(state='disabled')

    def search_Med(self):
        for i in self.data.get_children():
            self.data.delete(i)
        self.id_Entry.config(state='normal')
        name = self.name_Entry.get()
        conn = sqlite3.connect(f'{BASE_DIR}/Database/pharma.db')
        cur = conn.cursor()
        if name != '':
            nstatement = f"SELECT *FROM medicine WHERE Name LIKE '{name}';"
            cur.execute(nstatement)
            conn.commit()
            self.progress_label.config(text="Item Found Successfully")
        else:
            self.progress_label.config(text="Name is Required")

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
        self.id_Entry.config(state='disabled')

    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False

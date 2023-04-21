import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import askyesno
from ttkwidgets.autocomplete import AutocompleteCombobox


class Sale(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Sale')
        self.geometry("1350x700+5+5")
        # Add Some Style
        style = ttk.Style()
        # Pick A Theme
        style.theme_use('default')
        # Configure the Treeview Colors
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
        style.map('Treeview', background=[('selected', "#347083")])
        # now creating frames
        self.upframe = LabelFrame(self, text='Search Menu', labelanchor='nw', height=150)
        self.up1frame = LabelFrame(self.upframe, text='Enter ID Number')
        self.up2frame = LabelFrame(self.upframe, text='Enter Name ')
        self.up3frame = LabelFrame(self.upframe, text='Enter the Salt')
        self.midframe = Frame(self)
        self.cart_Frame = LabelFrame(self.midframe, text='Cart')
        self.details_Frame = LabelFrame(self.midframe, text="Details")
        self.item_Frame = LabelFrame(self.details_Frame, text="Item Details")
        self.billFrame = LabelFrame(self.details_Frame, text='Billing Information')
        # # configuring the frames
        self.upframe.pack(pady=10, fill=X)
        self.up1frame.place(x=10, y=10)
        self.up2frame.place(x=300, y=10)
        self.up3frame.place(x=1070, y=10)
        self.midframe.pack(pady=10)
        self.cart_Frame.pack(pady=10, side=LEFT, padx=10)
        self.cart_Frame.pack(pady=10, side=LEFT, padx=10)
        self.details_Frame.pack(pady=10, side=RIGHT, padx=10)
        self.item_Frame.grid(row=0, column=0, pady=10, padx=10)
        self.billFrame.grid(row=0, column=1, pady=10, padx=10)
        #
        # # Adding data to the first frame
        # list for combobox
        conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
        cur = conn.cursor()
        namestatemnt = f'SELECT Name FROM medicine'
        cur.execute(namestatemnt)
        mednames = []
        for i in cur.fetchall():
            mednames.append(i[0])
        conn.commit()
        conn.close()
        self.id_Entry = ttk.Entry(self.up1frame, width=40)
        self.id_search = ttk.Button(self.up1frame, text='Search', command=self.searchbyid)
        self.fname_Entry = AutocompleteCombobox(self.up2frame, width=116, completevalues=mednames)
        self.name_search = ttk.Button(self.up2frame, text='Search', command=self.searchbyname)
        self.salt_Entry = ttk.Entry(self.up3frame, width=40)
        self.salt_search = ttk.Button(self.up3frame, text='Search', command=self.searchbysalt)
        # Now configuring first frame
        self.id_Entry.grid(row=0, column=0, padx=10, pady=10)
        self.id_search.grid(row=1, column=0)
        self.fname_Entry.grid(row=0, column=1, padx=10, pady=10)
        self.name_search.grid(row=1, column=1)
        self.salt_Entry.grid(row=0, column=2, padx=10, pady=10)
        self.salt_search.grid(row=1, column=2)
        # Adding data to the second frame
        self.trscrol = Scrollbar(self.cart_Frame)
        self.data = ttk.Treeview(self.cart_Frame, yscrollcommand=self.trscrol.set, selectmode="extended", height=100)
        self.trscrol.pack(side=RIGHT, fill=Y)
        self.data.pack()
        self.trscrol.config(command=self.data.yview)
        self.data['columns'] = ("ID", "Name", "Type", "Quantity", "1/Price", "Total Price")
        # Properties of columns for tree
        self.data.column("#0", width=0, stretch=NO)
        self.data.column("ID", anchor=W, width=80)
        self.data.column("Name", anchor=W, width=120)
        self.data.column("Type", anchor=CENTER, width=120)
        self.data.column("Quantity", anchor=CENTER, width=80)
        self.data.column("1/Price", anchor=CENTER, width=80)
        self.data.column("Total Price", anchor=CENTER, width=80)
        # Creating Headings for tree
        self.data.heading("#0", text="", anchor=W)
        self.data.heading("ID", text="ID", anchor=W)
        self.data.heading("Name", text="Name", anchor=W)
        self.data.heading("Type", text="Type", anchor=CENTER)
        self.data.heading("Quantity", text="Quantity", anchor=CENTER)
        self.data.heading("1/Price", text="1/Price", anchor=CENTER)
        self.data.heading("Total Price", text="Total Price", anchor=CENTER)
        # now we will add detail to the item frame
        self.des_Name_Label = Label(self.item_Frame, text="Name :")
        self.des_Name_Entry = Entry(self.item_Frame, state='disabled')
        self.des_Lstock_Label = Label(self.item_Frame, text='Stock Left')
        self.des_Lstock_Entry = Entry(self.item_Frame, state='disabled')
        self.des_Price_Label = Label(self.item_Frame, text="Price Per Piece")
        self.des_Price_Entry = Entry(self.item_Frame, state='disabled')
        self.des_salt_Label = Label(self.item_Frame, text="Salt :")
        self.des_salt_Entry = Entry(self.item_Frame, state='disabled')
        self.des_Quantity_Label = Label(self.item_Frame, text="Quantity :")
        self.des_Quantity_Entry = Entry(self.item_Frame)
        self.cartbutton = ttk.Button(self.item_Frame, text='Add To Cart', command=self.addtocart)
        self.morebutton = ttk.Button(self.item_Frame, text='More Details', command=self.moredetail)
        self.clearCart_Button = ttk.Button(self.item_Frame, text='Clear Cart', width=10, command=self.clearcart)
        self.delete_Button = ttk.Button(self.item_Frame, text='Delete Selected', command=self.deleteentry)
        # configuring these widgets
        self.des_Name_Label.grid(row=0, column=0, padx=10, pady=10)
        self.des_Name_Entry.grid(row=0, column=1, padx=10, pady=10)
        self.des_Lstock_Label.grid(row=1, column=0, padx=10, pady=10)
        self.des_Lstock_Entry.grid(row=1, column=1, padx=10, pady=10)
        self.des_Price_Label.grid(row=2, column=0, padx=10, pady=10)
        self.des_Price_Entry.grid(row=2, column=1, padx=10, pady=10)
        self.des_salt_Label.grid(row=3, column=0, padx=10, pady=10)
        self.des_salt_Entry.grid(row=3, column=1, padx=10, pady=10)
        self.des_Quantity_Label.grid(row=4, column=0, padx=10, pady=10)
        self.des_Quantity_Entry.grid(row=4, column=1, padx=10, pady=10)
        self.cartbutton.grid(row=5, column=1, padx=10, pady=10)
        self.morebutton.grid(row=5, column=0, padx=10, pady=10)
        self.clearCart_Button.grid(row=6, column=1, padx=10, pady=10)
        self.delete_Button.grid(row=6, column=0, pady=5, padx=5)
        # now we will add details to the billing frame
        self.cus_Name_Label = Label(self.billFrame, text="Enter Customer Name: ")
        self.cus_Name_Entry = ttk.Entry(self.billFrame, width=20)
        self.total_Bill_Label = Label(self.billFrame, text='Total Bill =')
        self.total_Bill = Label(self.billFrame, text="$$$", fg='red')
        self.sell_Button = ttk.Button(self.billFrame, text='Sell', width=10, command=self.makechanges)
        self.quit_Button = Button(self.details_Frame, text='Quit', width=10, bg='red', command=self.destroy)
        self.status_Label = Label(self.details_Frame, text='Do some operations')
        # now we will configure those widgets
        self.cus_Name_Label.grid(row=0, column=0, padx=5, pady=20)
        self.cus_Name_Entry.grid(row=0, column=1, padx=5, pady=20)
        self.total_Bill_Label.grid(row=1, column=0, padx=10, pady=10)
        self.total_Bill.grid(row=1, column=1, padx=10, pady=10)
        self.sell_Button.grid(row=2, column=1, pady=10, padx=10)
        self.quit_Button.grid(row=2, column=1, pady=10, padx=10, sticky=E)
        self.status_Label.grid(row=1, column=1, pady=5, padx=5)
        # now lets start our binding function

        self.id_Entry.bind("<Return>", self.searchbyid)
        self.fname_Entry.bind("<Return>", self.searchbyname)
        self.salt_Entry.bind("<Return>", self.searchbysalt)
        self.des_Quantity_Entry.bind("<Return>", self.addtocart)
        self.cus_Name_Entry.bind("<Return>", self.makechanges)
        self.fname_Entry.bind("<Control-p>", self.gotocus)
        self.fname_Entry.focus()
        global selprice, totalcost
        totalcost = []

    # now lets start the backend programing

    def searchbyid(self, *args):
        iid = self.id_Entry.get()
        if iid.isnumeric():
            self.search(iid)
            self.id_Entry.delete(0, END)
            self.des_Quantity_Entry.focus()
        else:
            self.status_Label.config(text="Id must be integer", bg='red')

    def searchbyname(self, *args):
        name = self.fname_Entry.get()
        conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
        cur = conn.cursor()
        idstat = f"SELECT ID FROM medicine WHERE Name = '{name}'"
        cur.execute(idstat)
        if cur.fetchone():
            mid = cur.execute(idstat).fetchone()
            self.search(mid[0])
            self.fname_Entry.delete(0, END)
            self.des_Quantity_Entry.focus()
        else:
            self.status_Label.config(text='Not Found', bg='red')

    def searchbysalt(self, *args):
        self.clearfields()
        salt_window = tk.Tk()
        salt_window.geometry("580x500")  # Size of the window
        salt_window.title("Medicine having same sat")  # Adding a title
        # now creating new frames for our salt window
        salt = self.salt_Entry.get()
        # lets create a tree view for our salt
        trscrol1 = Scrollbar(salt_window)
        data1 = ttk.Treeview(salt_window, yscrollcommand=trscrol1.set, selectmode="extended", height=100)
        trscrol1.pack(side=RIGHT, fill=Y)
        data1.pack(side=LEFT, fill=Y)
        trscrol1.config(command=data1.yview)
        data1['columns'] = ("ID", "Name", "Type", "Quantity", "1/Price", "Salt")
        # Properties of columns for tree
        data1.column("#0", width=0, stretch=NO)
        data1.column("ID", anchor=W, width=80)
        data1.column("Name", anchor=W, width=120)
        data1.column("Type", anchor=CENTER, width=120)
        data1.column("Quantity", anchor=CENTER, width=80)
        data1.column("1/Price", anchor=CENTER, width=80)
        data1.column("Salt", anchor=CENTER, width=80)
        # Creating Headings for tree
        data1.heading("#0", text="", anchor=W)
        data1.heading("ID", text="ID", anchor=W)
        data1.heading("Name", text="Name", anchor=W)
        data1.heading("Type", text="Type", anchor=CENTER)
        data1.heading("Quantity", text="Quantity", anchor=CENTER)
        data1.heading("1/Price", text="1/Price", anchor=CENTER)
        data1.heading("Salt", text="Salt", anchor=CENTER)
        # For adding color in rows
        data1.tag_configure('oddrow', background="white")
        data1.tag_configure('evenrow', background="lightblue")
        conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM SALT WHERE Salt = '{salt}'")
        meddata1 = cur.fetchall()
        global count
        count = 0
        finedata1 = sorted(meddata1, key=lambda x: x[1])
        for data in finedata1:
            if count % 2 == 0:
                data1.insert(parent='', index='end', values=(data[0], data[1], data[2], data[3], data[4], data[5]),
                             tags='evenrow')
            else:
                data1.insert(parent='', index='end', values=(data[0], data[1], data[2], data[3], data[4], data[5]),
                             tags='oddrow')
            count += 1
        conn.commit()
        conn.close()

    def search(self, iid):
        conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
        cur = conn.cursor()
        checkstatment = f"SELECT Name FROM Search WHERE ID = '{iid}';"
        cur.execute(checkstatment)
        if cur.fetchone():
            fetchstatement = f"SELECT *FROM Search WHERE ID = '{iid}';"
            med = cur.execute(fetchstatement).fetchone()
            self.medid = med[0]
            self.mtype = med[3]
            self.pprice = med[6]
            self.enablefield()
            self.clearfields()
            self.des_Name_Entry.insert(0, med[1])
            self.des_Lstock_Entry.insert(0, med[5])
            self.des_Price_Entry.insert(0, med[4])
            self.des_salt_Entry.insert(0, med[2])
            self.disablefield()
            self.status_Label.config(text='Found', bg='green')

        else:
            self.status_Label.config(text='Not Found', bg='red')
        conn.commit()
        conn.close()

    def clearfields(self):
        self.des_Name_Entry.delete(0, END)
        self.des_Lstock_Entry.delete(0, END)
        self.des_Price_Entry.delete(0, END)
        self.des_salt_Entry.delete(0, END)
        self.des_Quantity_Entry.delete(0, END)

    def enablefield(self):
        self.des_Name_Entry.config(state='normal')
        self.des_Lstock_Entry.config(state='normal')
        self.des_Price_Entry.config(state='normal')
        self.des_salt_Entry.config(state='normal')

    def disablefield(self):
        self.des_Name_Entry.config(state='disabled')
        self.des_Lstock_Entry.config(state='disabled')
        self.des_Price_Entry.config(state='disabled')
        self.des_salt_Entry.config(state='disabled')

    def addtocart(self, *args):
        if self.des_Name_Entry.get() != '':
            mid = self.medid
            name1 = self.des_Name_Entry.get()
            metype = self.mtype
            newprice = self.pprice
            mquan = self.des_Quantity_Entry.get()
            stock = self.des_Lstock_Entry.get()
            price = self.des_Price_Entry.get()
            if mquan.isnumeric():
                mquan = float(mquan)
                stock = float(stock)
                price = float(price)
                totalprice = price * mquan
                totcost = newprice * mquan
                if stock >= mquan:
                    self.data.insert(parent='', index='end', values=(mid, name1, metype, mquan, price, totalprice))
                    self.totalprice()
                    self.totalcost(totcost)
                    self.enablefield()
                    self.clearfields()
                    self.disablefield()
                    self.fname_Entry.focus()
                else:
                    self.status_Label.config(text="Not Enough Stock", bg='red')
            else:
                self.status_Label.config(text='Enter Quantity must be integer', bg='red')
        else:
            self.status_Label.config(text='Search an item first', bg='red')

    def totalprice(self):
        tot = 0
        for row in self.data.get_children():
            our_p  = float(self.data.item(row)["values"][5])
#            tot = tot + self.data.item(row)['values'][5]
            tot = tot + our_p

        self.tbill = float(tot)
        self.total_Bill.config(text=self.tbill)

    def totalcost(self, newprice):
        newprice = float(newprice)
        totalcost.append(newprice)
        self.tcost = sum(totalcost)

    def makechanges(self, *args):
        cus = self.cus_Name_Entry.get()
        if cus != "":
            conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
            cur = conn.cursor()
            subtrst = f'UPDATE medicine SET Quantity = Quantity - ? WHERE ID = ?'
            additionsell = f"INSERT INTO Sell(Name, Type, Quantity, sell_Price) VALUES (?, ?, ?, ?) "
            for i in self.data.get_children():
                for i in self.data.get_children():
                    sid = self.data.item(i)['values'][0]
                    sname = self.data.item(i)['values'][1]
                    stype = self.data.item(i)['values'][2]
                    quan = self.data.item(i)['values'][3]
                    sprice = self.data.item(i)['values'][4]
                    tosprice = float(sprice)*float(quan)
                    cur.execute(subtrst, (quan, sid))
                    cur.execute(additionsell, (sname, stype, quan, tosprice))
                    conn.commit()
                break

                # This is the break statment for the loop checking is it is empty or not
            else:
                self.status_Label.config(text='Cart is Empty', bg='red')
        else:
            self.status_Label.config(text="Customer name can't be Empty")

        answer = askyesno(title='End Shopping',
                          message="Do Customer Wants to End his Shopping?\n Do you want to print the slip?",
                          parent=self)
        self.addtotrans(cus)
        if answer == 'yes':
            print("Yes")
        else:
            print('no')
        self.clearcart()
        self.fname_Entry.focus()
        self.cus_Name_Entry.delete(0, END)

    def moredetail(self):
        try:
            iid = self.medid
            conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
            cur = conn.cursor()
            stat = f"SELECT *FROM medicine WHERE ID = '{iid}'"
            med = cur.execute(stat).fetchone()
            detail_window = tk.Tk()
            detail_window.geometry("750x330")  # Size of the window
            detail_window.title("Medicine Details")  # Adding a title
            detail_window.configure(bg='White')
            # now creating new frames for our salt window
            label1 = ttk.Label(detail_window, text=' ID of the Medicine is ', font='Arial, 15')
            label2 = ttk.Label(detail_window, text=' Name of the Medicine is ', font='Arial, 15')
            label3 = ttk.Label(detail_window, text=' Type of the Medicine is ', font='Arial, 15')
            label4 = ttk.Label(detail_window, text=' Quantity of the Medicine is ', font='Arial, 15')
            label5 = ttk.Label(detail_window, text=' Purchase Price of the Medicine is ', font='Arial, 15')
            label6 = ttk.Label(detail_window, text=' Sell Price of the Medicine is ', font='Arial, 15')
            label7 = ttk.Label(detail_window, text=' Salt of the Medicine is  ', font='Arial, 15')
            label8 = ttk.Label(detail_window, text=' Company of the Medicine is ', font='Arial, 15')
            label21 = ttk.Label(detail_window, text=' : ', font='Arial, 15')
            label22 = ttk.Label(detail_window, text=' : ', font='Arial, 15')
            label23 = ttk.Label(detail_window, text=' : ', font='Arial, 15')
            label24 = ttk.Label(detail_window, text=' : ', font='Arial, 15')
            label25 = ttk.Label(detail_window, text=' : ', font='Arial, 15')
            label26 = ttk.Label(detail_window, text=' : ', font='Arial, 15')
            label27 = ttk.Label(detail_window, text=' : ', font='Arial, 15')
            label28 = ttk.Label(detail_window, text=' : ', font='Arial, 15')
            label11 = ttk.Label(detail_window, text=med[0], font='Arial, 15')
            label12 = ttk.Label(detail_window, text=med[1], font='Arial, 15')
            label33 = ttk.Label(detail_window, text=med[2], font='Arial, 15')
            label44 = ttk.Label(detail_window, text=med[3], font='Arial, 15')
            label55 = ttk.Label(detail_window, text=med[4], font='Arial, 15')
            label66 = ttk.Label(detail_window, text=med[5], font='Arial, 15')
            label77 = ttk.Label(detail_window, text=med[6], font='Arial, 15')
            label88 = ttk.Label(detail_window, text=med[7], font='Arial, 15')
            close_button = Button(detail_window, text='Close', bg='red', command=detail_window.destroy)
            label1.grid(row=0, column=0, padx=5, pady=5)
            label2.grid(row=1, column=0, padx=5, pady=5)
            label3.grid(row=2, column=0, padx=5, pady=5)
            label4.grid(row=3, column=0, padx=5, pady=5)
            label5.grid(row=4, column=0, padx=5, pady=5)
            label6.grid(row=5, column=0, padx=5, pady=5)
            label7.grid(row=6, column=0, padx=5, pady=5)
            label8.grid(row=7, column=0, padx=5, pady=5)
            label21.grid(row=0, column=1, padx=5, pady=5)
            label22.grid(row=1, column=1, padx=5, pady=5)
            label23.grid(row=2, column=1, padx=5, pady=5)
            label24.grid(row=3, column=1, padx=5, pady=5)
            label25.grid(row=4, column=1, padx=5, pady=5)
            label26.grid(row=5, column=1, padx=5, pady=5)
            label27.grid(row=6, column=1, padx=5, pady=5)
            label28.grid(row=7, column=1, padx=5, pady=5)
            label11.grid(row=0, column=2, padx=5, pady=5)
            label12.grid(row=1, column=2, padx=5, pady=5)
            label33.grid(row=2, column=2, padx=5, pady=5)
            label44.grid(row=3, column=2, padx=5, pady=5)
            label55.grid(row=4, column=2, padx=5, pady=5)
            label66.grid(row=5, column=2, padx=5, pady=5)
            label77.grid(row=6, column=2, padx=5, pady=5)
            label88.grid(row=7, column=2, padx=5, pady=5)
            close_button.grid(row=8, column=2, pady=5, padx=5)
        except:
            self.status_Label.config(text="Select an Item First", bg='red')

    def clearcart(self):
        for i in self.data.get_children():
            self.data.delete(i)

        self.totalprice()

    def deleteentry(self):
        selectedrow = self.data.focus()
        if selectedrow != "":
            delen = self.data.selection()[0]
            self.data.delete(delen)

            self.totalprice()
        else:
            self.status_Label.config(text="Select an entry to delete", bg='Red')

    def addtotrans(self, cus):
        totbill = self.tbill
        totcost = self.tcost
        conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
        cur = conn.cursor()
        stat = f"INSERT INTO TRANSACTIONS(CusName, Cost, Received) VALUES (?, ?, ?)"
        cur.execute(stat, (cus, totcost, totbill))
        conn.commit()
        conn.close()

    def gotocus(self, *args):
        self.cus_Name_Entry.focus()

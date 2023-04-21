from tkinter import Label, Frame, PhotoImage, Button, Toplevel
from tkinter.constants import X
from reports import Reports
from updateuser import ManageUsers
from Stock import Stock
from sale import Sale


class AdminInterface(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("Admin Interface")
        self.geometry("500x350+350+200")
        self.resizable(False, False)
        # creating Frames for our program
        self.top = Frame(self, height=100, bg='gray')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg='white')
        self.bottom.pack(fill=X)
        # now creating the login label and buttons
        self.logimg = PhotoImage(file=r'/home/ahmad/Desktop/E_Drug Store/icons/admin.png')
        self.logimglbl = Label(self.top, image=self.logimg, bg='gray', borderwidth=0)
        self.logintext = Label(self.top, text="Admin Interface ", font='italic 20 bold', fg='black', bg='gray')
        self.logimglbl.place(x=10, y=10)
        self.logintext.place(x=100, y=40)
        self.upstockimg = PhotoImage(file=r"/home/ahmad/Desktop/E_Drug Store/icons/update stock.png")
        self.upuserimg = PhotoImage(file=r"/home/ahmad/Desktop/E_Drug Store/icons/update user.png")
        self.mkrepimg = PhotoImage(file=r"/home/ahmad/Desktop/E_Drug Store/icons/make reports.png")
        self.inventoryimg = PhotoImage(file=r"/home/ahmad/Desktop/E_Drug Store/icons/inventory.png")
        self.upuserbutton = Button(self.bottom, image=self.upuserimg, borderwidth=0, command=lambda: ManageUsers() )
        self.updatestock = Button(self.bottom, image=self.upstockimg, borderwidth=0, command=lambda: Stock() )
        self.makreports = Button(self.bottom, image=self.mkrepimg, borderwidth=0, command=lambda: Reports() )
        self.sale = Button(self.bottom, image=self.inventoryimg, borderwidth=0, command=lambda: Sale() )
        self.duml = Label(self.bottom, text="--------->", font='italic 20 bold', fg='white', bg='white')
        self.duml1 = Label(self.bottom, text="--------->", font='italic 20 bold', fg='white', bg='white')
        self.exitad = Button(self.bottom, text="Logout", font="italic 10 bold", fg="white", bg='red', width=10, command=self.exitadw)
        self.duml.grid(row=0, column=0, padx=10, pady=10)
        self.duml1.grid(row=1, column=0, padx=10, pady=10)
        self.sale.grid(row=0, column=2, padx=10, pady=10)
        self.updatestock.grid(row=0, column=1, pady=10, padx=10)
        self.upuserbutton.grid(row=1, column=2, padx=10, pady=10)
        self.makreports.grid(row=1, column=1, padx=10, pady=10)
        self.exitad.grid(row=4, column=3, pady=10, padx=10)
# the main gui function

    def exitadw(self):
        self.destroy()
        exit()

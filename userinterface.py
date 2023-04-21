from tkinter import *
from sale import Sale


class UserInterface(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("User Interface")
        self.geometry("500x350+350+200")
        self.resizable(False, False)
        # creating Frames for our program
        self.top = Frame(self, height=100, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg='white')
        self.bottom.pack(fill=X)
        # now creating the login label and buttons
        self.logimg = PhotoImage(file=r'/home/ahmad/Desktop/E_Drug Store/icons/sales.png')
        self.logimglbl = Label(self.top, image=self.logimg, bg='white')
        self.logintext = Label(self.top, text="User Interface ", font='italic 20 bold', fg='black', bg='white')
        self.logimglbl.place(x=10, y=10)
        self.logintext.place(x=100, y=40)
        self.inventoryimg = PhotoImage(file=r"/home/ahmad/Desktop/E_Drug Store/icons/inventory.png")
        self.sale = Button(self.bottom, image=self.inventoryimg, borderwidth=0, command= lambda :  Sale() )
        self.exit_button = Button(self.bottom, borderwidth=0, text='Logout', bg='red', font="italic 10 bold", width=10, command=self.exitfun)
        self.duml = Label(self.bottom, text="--------->", font='italic 20 bold', fg='white', bg='white')
        self.duml1 = Label(self.bottom, text="--------->", font='italic 20 bold', fg='white', bg='white')
        self.duml.grid(row=0, column=0, padx=10, pady=10)
        self.duml1.grid(row=1, column=0, padx=10, pady=10)
        self.sale.grid(row=0, column=2, padx=10, pady=10)
        self.exit_button.grid(row=5, column=4, padx=10, pady=10)

    def exitfun(self):
        self.destroy()
        exit()

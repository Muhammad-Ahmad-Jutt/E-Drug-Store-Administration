import sqlite3
from tkinter import Label, Frame, PhotoImage, Button, messagebox, Tk
from tkinter.constants import X
from tkinter.ttk import Entry
from adminInterface import *
from userinterface import *


class FirstGui(object):
    def __init__(self, master):
        self.master = master

        # creating Frames for our program
        self.top = Frame(master, height=100, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=450, bg='gray')
        self.bottom.pack(fill=X)
        # now creating the login labels and buttons
        self.logimg = PhotoImage(file=r'/home/ahmad/Desktop/E_Drug Store/icons/loginimg.png')
        self.loginimg = PhotoImage(file=r'/home/ahmad/Desktop/E_Drug Store/icons/login.png')
        self.logimglbl = Label(self.top, image=self.logimg, bg='white')
        self.logintext = Label(self.top, text="Enter your login Credential ", font='italic 20 bold', fg='black', bg='white')
        self.label1 = Label(self.bottom, text='       Enter Your ID : ', font='arial 15 bold', fg='black', bg='gray')
        self.label2 = Label(self.bottom, text='Enter Your Password : ', font='arial 15 bold', fg='black', bg='gray')
        self.passentry = Entry(self.bottom, show='*', width=30)
        self.lbutton = Button(self.bottom, image=self.loginimg, borderwidth=0, command=self.authenticateuser, bg='gray')
        self.ebutton = Button(self.bottom, text='Exit', width=10, command=self.exitp, bg='red')
        self.passentry.place(x=250, y=105)
        self.logimglbl.place(x=10, y=10)
        self.logintext.place(x=100, y=40)
        self.label1.place(x=20, y=50)
        self.userentery = Entry(self.bottom, width=30)
        self.userentery.place(x=250, y=55)
        self.label2.place(x=20, y=100)
        self.lbutton.place(x=300, y=150)
        self.ebutton.place(x=400, y=200)
        self.userentery.bind("<Return>", self.movetopass)
        self.passentry.bind("<Return>", self.authenticateuser)
        self.userentery.focus()

    def movetopass(self, *args):
        self.passentry.focus()

    def exitp(self):
        quit()

    def authenticateuser(self, *args):
        un = self.userentery.get()
        password = self.passentry.get()
        con = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
        cur = con.cursor()
        statment = f"SELECT *FROM Users WHERE Name='{un}' AND Password = '{password}';"
        cur.execute(statment)
        if not cur.fetchone():
            messagebox.showerror("Error", "Enter correct username and password ")
        else:
            rolestatment = f"SELECT Job_Level FROM Users WHERE Name = '{un}'"
            role = cur.execute(rolestatment).fetchone()
            rol = role[0]
            if rol == 'Admin':
                AdminInterface()
                self.master.withdraw()  # To make the window disappear after the admin interface starts
            elif rol == 'Salesmen':
                UserInterface()
                self.master.withdraw()
            else:
                messagebox.showerror("error", "User not found")
        con.close()
        # the main gui function


def mainloginfunction():
    root = Tk()
    app = FirstGui(root)
    root.title("E-Drug Store Administration")
    root.geometry("500x350+350+200")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    mainloginfunction()

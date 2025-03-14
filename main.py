import sqlite3
from tkinter import Label, Frame, PhotoImage, Button, messagebox, Tk
from tkinter.constants import X
from tkinter.ttk import Entry
from adminInterface import *
from userinterface import *

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

import sqlite3
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
DB_FOLDER = BASE_DIR / "Database"
DB_PATH = DB_FOLDER / "pharma.db"
SQL_SCHEMA_FILE = BASE_DIR / "pharma.sql"  


def migrate_schema():
    """Creates the database if missing and applies the schema from the .sql file."""
    
    # Ensure the Database folder exists
    DB_FOLDER.mkdir(parents=True, exist_ok=True)

    # Check if the database already exists
    if not DB_PATH.exists():
        print("Database not found. Creating a new one and applying schema...")

        # Connect to the database (creates the file)
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Read and execute the SQL schema file
        with open(SQL_SCHEMA_FILE, 'r', encoding='utf-8') as f:
            schema_sql = f.read()
            cursor.executescript(schema_sql)  # Executes multiple SQL statements

        # Commit and close the connection
        conn.commit()
        conn.close()

        print("Database and schema created successfully!")
    else:
        print("Database already exists. Skipping migration.")
def setup_database():
    """Ensures the database and users are set up properly."""
    
    # Define base directory dynamically
    db_folder = BASE_DIR / "Database"
    db_path = db_folder / "pharma.db"

    # Create the Database folder if it does not exist
    db_folder.mkdir(parents=True, exist_ok=True)

    # Connect to SQLite (creates the file if it doesn't exist)
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Create users table if it doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Password TEXT NOT NULL,
            PhoneNo TEXT,
            Job_Level TEXT,
            Joining_Date TEXT,
            DOB TEXT,
            Address TEXT
        )
    ''')

    # Loop through all users defined in .env
    user_index = 1
    while True:
        name = os.getenv(f"USER_{user_index}_NAME")
        password = os.getenv(f"USER_{user_index}_PASSWORD")
        phone = os.getenv(f"USER_{user_index}_PHONE")
        job = os.getenv(f"USER_{user_index}_JOB")
        join_date = os.getenv(f"USER_{user_index}_JOIN_DATE")
        dob = os.getenv(f"USER_{user_index}_DOB")
        address = os.getenv(f"USER_{user_index}_ADDRESS")

        # If no user found, break the loop
        if not name:
            break

        # Check if user already exists
        cur.execute("SELECT COUNT(*) FROM Users WHERE Name = ?", (name,))
        user_exists = cur.fetchone()[0] > 0

        if not user_exists:
            # Insert user into the database
            cur.execute('''
                INSERT INTO Users (Name, Password, PhoneNo, Job_Level, Joining_Date, DOB, Address) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (name, password, phone, job, join_date, dob, address))
            print(f"User '{name}' added to database.")
        else:
            print(f"User '{name}' already exists in the database.")

        # Move to the next user
        user_index += 1

    # Commit changes and close connection
    con.commit()
    con.close()





class FirstGui(object):
    def __init__(self, master):
        self.master = master

        # creating Frames for our program
        self.top = Frame(master, height=100, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=450, bg='gray')
        self.bottom.pack(fill=X)
        # now creating the login labels and buttons
        self.logimg = PhotoImage(file=f'{BASE_DIR}/icons/loginimg.png')
        self.loginimg = PhotoImage(file=f'{BASE_DIR}/icons/login.png')
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
        con = sqlite3.connect(f'{BASE_DIR}/Database/pharma.db')
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
    migrate_schema()
    setup_database()
    mainloginfunction()

import csv
import datetime
import shutil
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from datetime import date
from datetime import timedelta
import pandas as pd


class Reports(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("Reports")
        self.geometry("850x350+350+200")
        self.resizable(False, False)
        # creating Frames for our program
        self.top = Frame(self, height=100, bg='gray')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg='white')
        self.bottom.pack(fill=X)
        # now creating the login label and buttons
        self.logimg = PhotoImage(file=r'/home/ahmad/Desktop/E_Drug Store/icons/admin.png')
        self.logimglbl = Label(self.top, image=self.logimg, bg='gray', borderwidth=0)
        self.logintext = Label(self.top, text="Reports ", font='italic 20 bold', fg='black', bg='gray')
        self.logimglbl.place(x=10, y=10)
        self.logintext.place(x=100, y=40)
        self.exitad = Button(self.bottom, text="Exit", font="italic 10 bold", fg="white", bg='red', width=10,
                             command=self.destroy)

        self.days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16",
                     "17", "18", "19", "10", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
        self.months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        self.years = ["1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001",
                      "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013",
                      "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
        # now the contents of the frame
        self.questionf_label = ttk.Label(self.bottom, text='Select the date from which you want report')
        self.questiont_label = Label(self.bottom, text='Select the date upto to which you want report')
        self.day_label = Label(self.bottom, text="DD")
        self.month_Label = Label(self.bottom, text="MM")
        self.year_label = Label(self.bottom, text="YYYY")
        self.tday_label = Label(self.bottom, text="DD")
        self.tmonth_Label = Label(self.bottom, text="MM")
        self.tyear_label = Label(self.bottom, text="YYYY")
        self.fday_entry = ttk.Combobox(self.bottom, values=self.days, width=3, state='readonly')
        self.fmonth_entry = ttk.Combobox(self.bottom, values=self.months, width=3, state='readonly')
        self.fyear_entry = ttk.Combobox(self.bottom, values=self.years, width=7, state='readonly')
        self.tday_entry = ttk.Combobox(self.bottom, values=self.days, width=3, state='readonly')
        self.tmonth_entry = ttk.Combobox(self.bottom, values=self.months, width=3, state='readonly')
        self.tyear_entry = ttk.Combobox(self.bottom, values=self.years, width=7, state='readonly')
        self.repobutton = ttk.Button(self.bottom, text="Generate Report", command=self.genreport)
        self.report = LabelFrame(self.bottom, text="Reports")
        self.todayrepo = ttk.Button(self.report, text="Yesterday Report", command= self.today_r)
        self.yesterdatrepo = ttk.Button(self.report, text="Last 3 Day Report", command= self.lastthree)
        self.lastsevendayrepo = ttk.Button(self.report, text="Last Seven Days Report", command= self.lastsevenday)
        self.lastthirtydayrepo = ttk.Button(self.report, text="Last 30 Day Report", command= self.lastthirtyday)
        self.lastyearreport = ttk.Button(self.report, text="Last 360 day Report", command= self.lastyear)
        self.questionf_label.place(x=5, y=20)
        self.questiont_label.place(x=5, y=80)
        self.day_label.place(x=300, y=10)
        self.fday_entry.place(x=300, y=30)
        self.month_Label.place(x=350, y=10)
        self.fmonth_entry.place(x=350, y=30)
        self.year_label.place(x=400, y=10)
        self.fyear_entry.place(x=400, y=30)
        self.tday_label.place(x=300, y=70)
        self.tday_entry.place(x=300, y=100)
        self.tmonth_Label.place(x=350, y=70)
        self.tmonth_entry.place(x=350, y=100)
        self.tyear_label.place(x=400, y=70)
        self.tyear_entry.place(x=400, y=100)
        self.repobutton.place(x=320, y=145)
        self.report.place(x=500, y=20)
        self.exitad.place(x=650, y=220)
        self.todayrepo.grid(row=0, column=0, pady=5, padx=5)
        self.yesterdatrepo.grid(row=0, column=1, pady=5, padx=5)
        self.lastsevendayrepo.grid(row=1, column=0, pady=5, padx=5)
        self.lastthirtydayrepo.grid(row=1, column=1, pady=5, padx=5)
        self.lastyearreport.grid(row=2, column=0, pady=5, padx=5)

    # the main gui function
    def today_r(self):
        today = date.today()
        desired_day = today - timedelta(days=1)
        self.exportreport(desired_day)

    def lastthree(self):
        today = date.today()
        desired_day = today - timedelta(days=2)
        self.exportreport(desired_day)

    def lastsevenday(self):
        today = date.today()
        desired_day = today - timedelta(days=6)
        self.exportreport(desired_day)

    def lastthirtyday(self):
        today = date.today()
        desired_day = today - timedelta(days=29)
        self.exportreport(desired_day)

    def lastyear(self):
        today = date.today()
        desired_day = today - timedelta(days=359)
        self.exportreport(desired_day)

    def exportreport(self, fdate):
        conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
        cur = conn.cursor()
        purchaseh = ["Purchase Report"]
        sellh = ["Sell Report"]
        transactionh = ["Transaction Report"]
        fsheader = ["Sell ID", "Item Name", "Type", "Quantity", "Sell Price", "Sell Date"]
        fpheader = ["Purchase ID", "Item Name", "Type", "Quantity", "Purchase Price", "Sell Price", "Purchase Date"]
        ftheader = ["Transaction ID", "Customer Name", "Transactions Cost", "Received", "Transaction Date"]
        fsstatement = f"SELECT *FROM Sell WHERE SDate >= '{fdate}';"
        fpstatment = f"SELECT *FROM Purchase WHERE PDate >='{fdate}';"
        ftstatement = f"SELECT *FROM TRANSACTIONS WHERE TDate >='{fdate}';"
        sdata = cur.execute(fsstatement).fetchall()
        pdata = cur.execute(fpstatment).fetchall()
        tdata = cur.execute(ftstatement).fetchall()
        with open(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", 'w', newline='') as fle:
            writer = csv.writer(fle)

        for col in sdata:
            with open(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(sellh)
            fs = pd.DataFrame(data=sdata)
            fs.to_csv(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", header=fsheader, index=False,
                      mode='a')
            break
        for col in pdata:
            with open(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(purchaseh)
            fs = pd.DataFrame(data=pdata)
            fs.to_csv(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", header=fpheader, index=False,
                      mode='a')
            break
        for col in tdata:
            with open(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(transactionh)
            ft = pd.DataFrame(data=tdata)
            ft.to_csv(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", header=ftheader, index=False,
                      mode='a')
            break
        self.makeprl()

    def genreport(self):
        fday = self.fday_entry.get()
        fmonth = self.fmonth_entry.get()
        fyear = self.fyear_entry.get()
        tday = self.tday_entry.get()
        tmonth = self.tmonth_entry.get()
        tyear = self.tyear_entry.get()
        if fday and fmonth and fyear and tday and tmonth and tyear != "":
            fd = datetime.datetime(int(fyear), int(fmonth), int(fday))
            td = datetime.datetime(int(tyear), int(tmonth), int(tday))
            if fd < td:
                frdate = fyear + "-" + fmonth + "-" + fday
                todate = tyear + "-" + tmonth + "-" + tday
                conn = sqlite3.connect(r'/home/ahmad/Desktop/E_Drug Store/Database/pharma.db')
                cur = conn.cursor()
                purchaseh = ["Purchase Report"]
                sellh = ["Sell Report"]
                transactionh = ["Transaction Report"]
                fsheader = ["Sell ID", "Item Name", "Type", "Quantity", "Sell Price", "Sell Date"]
                fpheader = ["Purchase ID", "Item Name", "Type", "Quantity", "Purchase Price", "Sell Price", "Purchase Date"]
                ftheader = ["Transaction ID", "Customer Name", "Transactions Cost", "Received", "Transaction Date"]
                sstatement = f"SELECT *FROM Sell WHERE SDate >='{frdate}' AND SDate <= '{todate}';"
                pstatement = f"SELECT *FROM Purchase WHERE PDate >='{frdate}' AND PDate <= '{todate}';"
                tstatement = f"SELECT *FROM TRANSACTIONS WHERE TDate >='{frdate}' AND TDate <= '{todate}';"
                sdata = cur.execute(sstatement).fetchall()
                pdata = cur.execute(pstatement).fetchall()
                tdata = cur.execute(tstatement).fetchall()
                with open(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", 'w', newline='') as fle:
                    writer = csv.writer(fle)
                for col in sdata:
                    with open(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(sellh)
                    fs = pd.DataFrame(data=sdata)
                    fs.to_csv(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", header=fsheader,
                              index=False, mode='a')
                    break
                for col in pdata:
                    with open(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(purchaseh)
                    fs = pd.DataFrame(data=pdata)
                    fs.to_csv(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", header=fpheader,
                              index=False, mode='a')
                    break
                for col in tdata:
                    with open(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(transactionh)
                    ft = pd.DataFrame(data=tdata)
                    ft.to_csv(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", header=ftheader,
                              index=False, mode='a')
                    break
                self.makeprl()
            else:
                messagebox.showerror("Invalid Date", "'From Date' Can't be greater or equal to 'To Date'\n Kindly correct your date", parent=self)
        else:
            messagebox.showerror("Incomplete form", "Please enter the complete date(DD-MM-YYYY)", parent=self)

    def makeprl(self):
        with open(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", 'r') as file:
            reader = csv.reader(file, delimiter=",")
            tansections_start = False
            transaction_headerlist = None
            cost_columns = None
            received_columns = None
            costsum = 0
            receivedsum = 0
            for row in reader:
                if tansections_start is False:
                    if len(row) > 0:
                        if row != "":
                            if row[0] == "Transaction Report":
                                transaction_headerlist = next(reader)
                                cost_columns = transaction_headerlist.index("Transactions Cost")
                                received_columns = transaction_headerlist.index("Received")
                                tansections_start = True

                else:
                    if len(row[0]) > 0:
                        costsum += float(row[cost_columns])
                        receivedsum += float(row[received_columns])
                    else:
                        break
        profit = float(receivedsum) - float(costsum)
        datalist = [["      "], ["Profit loss Report"], ["Total Cost of medicine", costsum],
                    ["Total Money Received", receivedsum],
                    ["Net Profit", profit]]
        with open(r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv", 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(datalist)
        self.cpfile()

    def cpfile(self):
        tdate = date.today()
        fileadd = r"/home/ahmad/Desktop/E_Drug Store/exports/gen.csv"
        filedestination = r"/home/ahmad/Desktop/E_Drug Store/exports/Report "+str(tdate)+".csv"
        shutil.copy(fileadd, filedestination)

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from tkinter import *



root=Tk()
root.geometry('600x500')
root.title("DB Operation")
root.resizable(0, 0)
x = StringVar()
y = StringVar()

def home():
    f1=Frame()
    f1.config(background="#9A7D0A")
    x.set("")
    y.set("")
    f1.place(x=0, y=0, width=600, height=500)
    btn = Button(f1, text="mySql", command=mysqldb, fg="blue", bg="red",height=3,width=10)
    btn1 = Button(f1, text="Oracle", command=oracle, fg="blue",height=3,width=10)
    btn.pack(pady=45)
    btn1.pack(pady=25)
    root.mainloop()




#================MySQL===================
def mysqldb():
    dbTop = Frame()
    dbTop.config(background="#F5B7B1")
    x.set("")
    y.set("")
    dbTop.place(x=0, y=0, width=600, height=500)
    ddlbtn=Button(dbTop,text="DDL",command=ddl,height=3,width=10)
    dmlbtn=Button(dbTop,text="DML",command=dml,height=3,width=10)
    backbtn=Button(dbTop,text="Back",command=home,height=2,width=8,fg="#FF3333")
    ddlbtn.pack(pady=45)
    dmlbtn.pack(pady=25)
    backbtn.pack(side=BOTTOM,pady=15)

def ddl():
    ddltop=Frame()
    ddltop.config(background="#FCF3CF")
    x.set("")
    y.set("")

    ddltop.place(x=0, y=0, width=600, height=500)
    btn1 = Button(ddltop, text="CREATE", command=create, height=3, width=10)
    btn2 = Button(ddltop, text="DROP", command=drop, height=3, width=10)
    btn3 = Button(ddltop, text="ALTER", command=alter, height=3, width=10)
    btn1.pack(pady=25)
    btn2.pack(pady=25)
    btn3.pack(pady=25)
    ddltop.place(x=0, y=0, width=600, height=500)
    backbtn = Button(ddltop, text="Back", command=mysqldb,height=2,width=8,fg="#FF3333")
    backbtn.pack(side=BOTTOM, pady=15)

def create():
    creTop = Frame()
    x.set("")
    y.set("")
    creTop.config(background="#F4D03F")

    creTop.place(x=0, y=0, width=600, height=500)
    lbl=Label(creTop,text="Create Operation",font="bold").pack()
    lbl1 = Label(creTop, text="Example:\n CREATE TABLE Persons (PersonID int,LastName varchar(255),\nFirstName varchar(255),Address varchar(255),\nCity varchar(255));" , font="bold").pack(pady=15)
    backbtn = Button(creTop, text="Back", command=ddl,height=2,width=8,fg="#FF3333")
    backbtn.pack(side=BOTTOM, pady=15)
def drop():
    drTop=Frame()
    x.set("")
    y.set("")
    drTop.config(background="#F4D03F")

    drTop.place(x=0, y=0, width=600, height=500)
    lbl = Label(drTop, text="Drop Operation", font="bold").pack()
    lbl1 = Label(drTop,text="Example:\n DROP TABLE Shippers;",font="bold").pack(pady=15)
    backbtn = Button(drTop, text="Back", command=ddl, height=2, width=8, fg="#FF3333")
    backbtn.pack(side=BOTTOM, pady=15)

def alter():
    aTop = Frame()
    x.set("")
    y.set("")
    aTop.config(background="#F4D03F")

    aTop.place(x=0, y=0, width=600, height=500)
    lbl = Label(aTop, text="Alter Operation", font="bold").pack()
    lbl1 = Label(aTop, text="Example:\n ALTER TABLE Customers DROP COLUMN Email;", font="bold").pack(pady=15)
    backbtn = Button(aTop, text="Back", command=ddl, height=2, width=8, fg="#FF3333")
    backbtn.pack(side=BOTTOM, pady=15)

def dml():
    dmltop=Frame()
    dmltop.config(background="#FCF3CF")
    x.set("")
    y.set("")

    dmltop.place(x=0, y=0, width=600, height=500)
    btn1 = Button(dmltop, text="INSERT", command=insert,height=3,width=10)
    btn2 = Button(dmltop, text="UPDATE", command=update,height=3,width=10)
    btn3 = Button(dmltop, text="DELETE", command=delete,height=3,width=10)
    btn1.pack(pady=25)
    btn2.pack(pady=25)
    btn3.pack(pady=25)
    backbtn = Button(dmltop, text="Back", command=mysqldb,height=2,width=8,fg="#FF3333")
    backbtn.pack(side=BOTTOM, pady=15)

def insert():
    insTop = Frame()
    x.set("")
    y.set("")
    insTop.config(background="#F4D03F")

    insTop.place(x=0, y=0, width=600, height=500)
    lbl=Label(insTop,text="Insert Operation",font="bold").pack()
    lbl1 = Label(insTop, text="Example:\n INSERT INTO Customers (CustomerName, City, Country) \n VALUES ('Cardinal', 'Stavanger', 'Norway');" , font="bold").pack(pady=15)
    backbtn = Button(insTop, text="Back", command=dml,height=2,width=8,fg="#FF3333")
    backbtn.pack(side=BOTTOM, pady=15)


def update():
    updTop = Frame()
    updTop.config(background="#F4D03F")
    x.set("")
    y.set("")

    updTop.place(x=0, y=0, width=600, height=500)
    lbl = Label(updTop, text="Updation Operation", font="bold").pack()
    lbl1 = Label(updTop,text="Example:\n UPDATE Customers SET ContactName='Juan'\nWHERE Country='Mexico';",font="bold").pack(pady=15)
    backbtn = Button(updTop, text="Back", command=dml,height=2,width=8,fg="#FF3333")
    backbtn.pack(side=BOTTOM, pady=15)


def delete():
    delTop = Frame()
    delTop.config(background="#F4D03F")
    x.set("")
    y.set("")

    delTop.place(x=0, y=0, width=600, height=500)
    lbl = Label(delTop, text="Deletion Operation", font="bold").pack()
    lbl1=Label(delTop,text="Example:\nDELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';").pack(pady=15)
    backbtn = Button(delTop, text="Back", command=dml,height=2,width=8,fg="#FF3333")
    backbtn.pack(side=BOTTOM, pady=15)

#===============oracle==============
def oracle(root):
    top=Frame()
    x.set("")
    y.set("")
    top.config(background="#F5B7B1")

    top.place(x=0, y=0, width=600, height=500)
    lbl=Label(top,text="Oracle not yet Configured!!!").pack(pady=45)
    backbtn = Button(top, text="Back",command=home,height=2,width=8,fg="#FF3333",font="Helvetica")
    backbtn.pack(side=BOTTOM,pady=15)



home()
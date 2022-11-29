from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from tkinter import font
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from datetime import date
from datetime import timedelta
import datetime

###main
##root = Tk()
##root.title("library")
##helv30 = font.Font(family='Helvetica', size=30)
##helv15 = font.Font(family='Helvetica', size=15)
##bookTable = "Book"
##allreservations = []
##
###FUNCTION
##def Loans():
##    textentry = Entry(root, width = 20)
##    textentry.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.8)
##
###photo
##canv = Canvas(root, width=1000, height=1000, bg='white')
##canv.grid(row=0, column=0)
##resized_image2=Image.open("book-borrow-clipart.png").resize((500,500), Image.ANTIALIAS)
##image2 = ImageTk.PhotoImage(resized_image2)
##canv.create_image(50, 170, anchor=NW, image=image2)
##
###heading
##
##
##canv.create_text(500, 100, text="Loans", fill="black", font=('Roman 70 bold'))
##canv.pack()
##
##canv.create_text(750, 300, text="Please select an option:", fill="black", font=('Helvetica 20 bold'))
##canv.pack()

#functions


def Borrow():

    try:
        connection = mysql.connector.connect(host="localhost",user="root",password="pw",database="library")
        cursor = connection.cursor()
        
        MemberID = newMem
        AccessionNumber = en1.get()
        
        String = "A"
        String += AccessionNumber[1:]

        sql_select_Query_2 = "SELECT * FROM StatusOfBook"
        cursor.execute(sql_select_Query_2)
        records2 = cursor.fetchall()
        

        sql_select_Query = "SELECT * FROM Book"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        sql_select_Query3 = "SELECT * FROM Fine"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query3)
        records3 = cursor.fetchall()

        noreserevedmember = False
        
        for row in records2:
            if row[1] == String:
                status = row[0]
            else:
                continue
        
        count = 0

        for row in records:
            if row[0] == String:
                if row[5] == None or row[5] == "" or row[5] == MemberID:
                    noreserevedmember = True
                
            if row[6] == MemberID:
                count += 1
            else:
                continue

        nofine = True
        for row in records3:
            if (row[0] == MemberID) and (row[1] != 0):
                nofine = False
            else:
                continue
##        print(nofine)
##        print(status)
##        print(noreserevedmember)
##        print(count)
        
        if status != "Loaned" and noreserevedmember and count < 2 and nofine:
            currentdate = date.today()
            borrowdate = currentdate.strftime("%Y-%d-%m")
            after14days = currentdate + timedelta(days=14)
            returndate = after14days.strftime("%Y-%d-%m")
            

            sql_update_query = """Update Book SET Borrowed_MemberID = %s, BorrowDate = %s, DueDate = %s WHERE AccessionNumber = %s"""
            val = (MemberID,currentdate,after14days,String)
            cursor.execute(sql_update_query,val)
            connection.commit()

            sql_update_query1 = """Update StatusOfBook set Status = "Loaned" WHERE AccessionNumber = %s"""
            val1 = (String,)
            cursor.execute(sql_update_query1,val1)
            connection.commit()

            sql_update_query2 = """Update Book set Reserved_MemberID = "" WHERE AccessionNumber = %s"""
            val2 = (String,)
            cursor.execute(sql_update_query2,val2)
            connection.commit()
            
            messagebox.showinfo("Success!", "Book successfully borrowed")

        else:
            if status == "Loaned":
                dateneeded = ""
                for row in records:
                    if row[0] == String:
                        dateneeded = row[10].strftime("%d/%m/%Y")
                    else:
                        continue
                
                sentence = "Book currently on Loan until: "
                sentence += dateneeded
                messagebox.showinfo("Error", sentence)
                
            elif noreserevedmember == False:
                messagebox.showinfo("Error", "Book reserved by another member")
                
            else:
                if count >= 2:
                    messagebox.showinfo("Error", "Member loan quota exceeded")
                else:
                    messagebox.showinfo("Error", "Member has outstanding fines")
    except Exception:
        messagebox.showinfo("Error", "Invalid input")
        root.destroy()
        

def BorrowBook():
    global labelFrame, en1, en2,root, Canvas1

    root=Tk()
    root.title("library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="LightBlue1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="LightBlue1", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.11)
    headingLabel = Label(headingFrame1, text="Borrow Book", bg="white", fg="black", font=('Courier',30))
    headingLabel.place(relx=0, rely=0.1, relwidth=1, relheight=1)

    #frame for form
    LabelFrame1 = Frame(root, bg="LightBlue1")
    LabelFrame1.place(relx=0.03, rely=0.2, relwidth=1, relheight=0.6)

    lb = Label(LabelFrame1, text="To borrow a book, please enter the required information below: ", bg="LightBlue1", fg="black")
    lb.place(relx=0, rely=0.25, relheight=0.08)
    lb.config(font=("Courier", 14))

    

    #frame for form
    LabelFrame = Frame(root, bg="LightBlue3")
    LabelFrame.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.25)

    #aCESSIONnUMBER
    lb1 = Label(LabelFrame, text="Accession Number: ", bg="LightBlue3", fg="black")
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    #entry label for book Id
    en1 = Entry(LabelFrame)
    en1.place(relx=0.35, rely=0.2, relwidth=0.62, relheight=0.15)

    #member
    lb2 = Label(LabelFrame, text="Membership ID: ", bg="LightBlue3", fg="black")
    lb2.place(relx=0.05, rely=0.5, relheight=0.1)
    #entry for title
    en2 = Entry(LabelFrame)
    en2.place(relx=0.35, rely=0.5, relwidth=0.62, relheight=0.15)


    #Issue Button
    issuebtn = Button(root, text="Borrow Book", bg="#d1ccc0", fg="black", command=clicker)
    issuebtn.place(relx=0.2, rely=0.8, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Return to Loans menu", bg="#aaa69d", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.8, relwidth=0.3, relheight=0.08)

    root.mainloop()


def clicker():
    global  root, cursor, connection, newMem
    root = Tk()
    root.title("library")
    root.minsize(width=400, height=400)
    root.geometry("250x200")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="LightBlue1")
    Canvas1.pack(expand=True, fill=BOTH)

    connection = mysql.connector.connect(host="localhost",user="root",password="pw",database="library")


    sql_select_Query = "select * FROM Book"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    sql_select_Query2 = "select * FROM Member"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query2)
    records2 = cursor.fetchall()
    
    
    AcessionNumber = en1.get()
    Memberid = en2.get()
    title = ""
    Membername = ""
    newAN = ""
    newMem= ""
    validAN = False
    validMID = False
    currentdate = date.today()
    borrowdate = currentdate.strftime("%d/%m/%Y")
    after14days = currentdate + timedelta(days=14)
    returndate = after14days.strftime("%d/%m/%Y")
            

    for row in records:
        string = AcessionNumber[1:]
        if row[0][1:]==string:
            newAN = "A" + string
            title= row[1]
            validAN = True
        else:
            continue
    for row in records2:
        string = Memberid[1:-1]
        lastnum = Memberid[-1]
        if (row[0][1:-1] == string) and (row[0][-1].lower() == lastnum.lower()):
            newMem = row[0]
            validMID = True
            Membername = row[1]
        else:
            continue
            
            
        
    
    

    AN ="Accession Number : "
    AN += newAN
    
    TT = "Book Title: "
    TT +=  title

    BD = "Borrow Date: "
    BD += borrowdate
    
    MID = "Membership ID: "
    MID += newMem
    
    MN = "Member Name: "
    MN += Membername
    
    DD = "Due date: "
    DD += returndate

    if validAN and validMID:
        headingFrame1 = Frame(root, bg="LightBlue1", bd=5)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

         #add a leabel to heading Frame
        headingLabel = Label(headingFrame1, text="Confirm details", bg="white", fg="black", font=('Courier',15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        #add a label frame to canvas to give a lebl insite it to delete book
        LabelFrame = Frame(root, bg="LightBlue3")
        LabelFrame.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.4)
        
        lb1 = Label(LabelFrame, text=AN, bg="LightBlue3", fg="black")
        lb1.place(relx=0.01, rely=0.05)
        lb1.config(font=("Courier", 11))

        lb2 = Label(LabelFrame, text=TT, bg="LightBlue3", fg="black")
        lb2.place(relx=0.01, rely=0.2)
        lb2.config(font=("Courier", 11))

        lb3 = Label(LabelFrame, text=BD, bg="LightBlue3", fg="black")
        lb3.place(relx=0.01, rely=0.35)
        lb3.config(font=("Courier", 11))

        lb4 = Label(LabelFrame, text=MID, bg="LightBlue3", fg="black")
        lb4.place(relx=0.01, rely=0.5)
        lb4.config(font=("Courier", 11))

        lb5 = Label(LabelFrame, text=MN, bg="LightBlue3", fg="black")
        lb5.place(relx=0.01, rely=0.65)
        lb5.config(font=("Courier", 11))

        lb5 = Label(LabelFrame, text=DD, bg="LightBlue3", fg="black")
        lb5.place(relx=0.01, rely=0.8)
        lb5.config(font=("Courier", 11))

        Confirm = Button(root, text="Confirm Loan", bg="plum3", fg="black", command=Borrow)
        Confirm.place(relx=0.04, rely=0.86, relwidth=0.35, relheight=0.08)

        Back = Button(root, text="Return to Borrow menu", bg="#f7f1e3", fg="black", command=root.destroy)
        Back.place(relx=0.52, rely=0.86, relwidth=0.45, relheight=0.08)


    else:
        messagebox.showinfo("Error","Invalid MemberID or Accession Number")
        root.withdraw()

    root.mainloop()
    
def Return():
#Fine,BorrowedMemberID, newAN
    AccessionNumber = bookInfo1.get()

    sql_select_Query = "SELECT * FROM Fine"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    noprevfine = True

    sqlBook = """Update Book SET Borrowed_MemberID = %s, Returned_MemberID = %s, BorrowDate = %s,ReturnDate = %s, DueDate = %s WHERE AccessionNumber = %s"""
    valBook = ("",BorrowedMemberID,None,returndate,None,newAN)
    cursor.execute(sqlBook,valBook)
    connection.commit()

    sqlSTATUS = """Update StatusOfBook SET Status = %s WHERE AccessionNumber = %s"""
    valSTATUS = ("Available",newAN)
    cursor.execute(sqlSTATUS,valSTATUS)
    connection.commit()

    if abs(Fineamount) > 0:
        for row in records:
            if BorrowedMemberID == row[0]:
                sql_update_query = """Update Fine SET Amount = %s WHERE MemberID = %s"""
                newFine = row[1] + abs(Fineamount)
                val = (newFine,BorrowedMemberID)
                cursor.execute(sql_update_query,val)
                connection.commit()
                noprevfine = False
            else:
                continue
        
        if noprevfine:
            sql1 = "INSERT INTO Fine (MemberId, Amount) VALUES (%s, %s)"
            val1 = (BorrowedMemberID,Fineamount)
            cursor.execute(sql1,val1)
            connection.commit()

        messagebox.showinfo("Warning!","WARNING! Book returned successfully but member has incurred fine")
    else:
        messagebox.showinfo("Success!","Book returned successfully")
            
                

def returnBook():
    global root, con, cur, labelFrame, submitBtn, quitBtn, Canvas1, bookInfo1, bookInfo2, lb1

    root = Tk()
    root.title("library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="LightSkyBlue1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="LightSkyBlue1", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="Return Book", bg="white", fg="black", font=('Courier',25))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="LightSkyBlue3")
    LabelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.4)

    #take a book AN to delete
    lb2 = Label(LabelFrame, text="Accession Number: ", bg="LightSkyBlue3", fg="black")
    lb2.place(relx=0.1, rely=0.15)
    lb2.config(font=("Courier", 15))

    bookInfo1 = Entry(LabelFrame)
    bookInfo1.place(relx=0.1, rely=0.3, relwidth=0.5)

    lb3 = Label(LabelFrame, text="Return date(dd/mm/yyyy): ", bg="LightSkyBlue3", fg="black")
    lb3.place(relx=0.1, rely=0.55)
    lb3.config(font=("Courier", 15))

    bookInfo2 = Entry(LabelFrame)
    bookInfo2.place(relx=0.1, rely=0.7, relwidth=0.5)

    #submit Button
    submitBtn = Button(root, text="Return Book", bg="lightblue", fg="black", command=clicker2)
    submitBtn.place(relx=0.19, rely=0.8, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Back to Loans menu", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.51, rely=0.8, relwidth=0.3, relheight=0.08)

    root.mainloop()


def clicker2():
    global  root, cursor, connection, Fineamount ,BorrowedMemberID, returndate, newAN
    root = Tk()
    root.title("library")
    root.minsize(width=400, height=400)
    root.geometry("250x200")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="LightSkyBlue1")
    Canvas1.pack(expand=True, fill=BOTH)

    connection = mysql.connector.connect(host="localhost",user="root",password="pw",database="library")


    sql_select_Query = "select * FROM Book"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    sql_select_Query2 = "select * FROM Member"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query2)
    records2 = cursor.fetchall()
    
    
    AcessionNumber = bookInfo1.get()
    title = ""
    BorrowedMemberID =""
    Membername = ""
    returndatestring = bookInfo2.get()

    try:
        datetime.datetime.strptime(bookInfo2.get(), "%d/%m/%Y").date()
    except ValueError:
        messagebox.showinfo("Error", "Wrong date format")
        root.destroy()
  
    returndate = datetime.datetime.strptime(bookInfo2.get(), "%d/%m/%Y").date()
    havevalidid = False
    duedate = ""

    try:

        for row in records:
            string = AcessionNumber[1:]
            if row[0][1:]==string:
                newAN = "A" + string
                title= row[1]
                BorrowedMemberID = row[6]
                print(row[6])
                print(row[7])
                print(row[8])
                print(row[9])
                print(row[10])
                duedate = row[10].strftime("%d/%m/%Y")
                havevalidid = True
            else:
                continue
        Fineamount = (datetime.datetime.strptime(duedate, "%d/%m/%Y").date() - returndate).days
        

        if Fineamount > 0:
            Fineamount = 0
        
            
        for row in records2:
            if BorrowedMemberID == row[0]:
                Membername = row[1]
            else:
                continue
                

        AN ="Accession Number : "
        AN += newAN
        
        TT = "Book Title: "
        TT +=  title

        MID = "Membership ID: "
        MID += BorrowedMemberID
        
        MN = "Member Name: "
        MN += Membername
        
        DD = "Return date: "
        DD += returndatestring

        Fine = "Fine: $"
        Fine+= str(abs(Fineamount))

        if havevalidid:
            headingFrame1 = Frame(root, bg="LightSkyBlue1", bd=5)
            headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

            #add a leabel to heading Frame
            headingLabel = Label(headingFrame1, text="Confirm details", bg="white", fg="black", font=('Courier',15))
            headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

            #add a label frame to canvas to give a lebl insite it to delete book
            LabelFrame = Frame(root, bg="LightSkyBlue3")
            LabelFrame.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.4)
                
            lb1 = Label(LabelFrame, text=AN, bg="LightSkyBlue3", fg="black")
            lb1.place(relx=0.01, rely=0.05)
            lb1.config(font=("Courier", 11))

            lb2 = Label(LabelFrame, text=TT, bg="LightSkyBlue3", fg="black")
            lb2.place(relx=0.01, rely=0.2)
            lb2.config(font=("Courier", 11))

            lb3 = Label(LabelFrame, text=MID, bg="LightSkyBlue3", fg="black")
            lb3.place(relx=0.01, rely=0.35)
            lb3.config(font=("Courier", 11))

            lb4 = Label(LabelFrame, text=MN, bg="LightSkyBlue3", fg="black")
            lb4.place(relx=0.01, rely=0.5)
            lb4.config(font=("Courier", 11))

            lb5 = Label(LabelFrame, text=DD, bg="LightSkyBlue3", fg="black")
            lb5.place(relx=0.01, rely=0.65)
            lb5.config(font=("Courier", 11))

            lb5 = Label(LabelFrame, text=Fine, bg="LightSkyBlue3", fg="black")
            lb5.place(relx=0.01, rely=0.8)
            lb5.config(font=("Courier", 11))

            Confirm = Button(root, text="Confirm Return", bg="plum3", fg="black", command=Return)
            Confirm.place(relx=0.04, rely=0.86, relwidth=0.35, relheight=0.08)

            Back = Button(root, text="Back to Return Function", bg="#f7f1e3", fg="black", command=root.destroy)
            Back.place(relx=0.52, rely=0.86, relwidth=0.45, relheight=0.08)

    except Exception:
        messagebox.showinfo("Error", "Invalid Borrowed Book Accession Number")
        root.destroy()


        
    root.mainloop()
    
    
###Buttons
##
##btnBorrowing = Button(root,text="1. Book Borrowing",bg='black', fg='black',command=BorrowBook)
##btnBorrowing.place(relx=0.6,rely=0.45, relwidth=0.3, relheight=0.1)
##btnBorrowing['font'] = helv30
##
##btnReturn = Button(root,text="2. Book Return",bg='black', fg='black',command=returnBook)
##btnReturn.place(relx=0.6,rely=0.65, relwidth=0.3, relheight=0.1)
##btnReturn['font'] = helv30
##
##btnBack = Button(root,text="Back to Main Menu",bg='black', fg='black',command=Loans)
##btnBack.place(relx=0.4,rely=0.9, relwidth=0.2, relheight=0.06)
##btnBack['font'] = helv15
##
##root.mainloop()









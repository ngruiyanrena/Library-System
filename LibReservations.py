from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from tkinter import font
import mysql.connector


#RESERVEBOOK
def reserveBook():
    global en1, en2, en3, Canvas1, connection, cursor, bookTable, root
    
    root = Tk()
    root.title("library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "pw"
    mydatabase = "library"

    connection = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cursor = connection.cursor()

    # Create the canvas for info
    Canvas1 = Canvas(root)
    Canvas1.config(bg="RosyBrown1")
    Canvas1.pack(expand=True, fill=BOTH)
    
    # Add a heading Frame
    headingFrame1 = Frame(root, bg="RosyBrown1", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Reserve Books", bg="white", fg="black", font=('Courier',30))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Frame for form
    LabelFrame1 = Frame(root, bg="RosyBrown1")
    LabelFrame1.place(relx=0.03, rely=0.3, relwidth=1, relheight=0.6)

    lb = Label(LabelFrame1, text="To reserve a book, please enter the required information below: ", bg="RosyBrown1", fg="black")
    lb.place(relx=0, rely=0, relheight=0.08)
    lb.config(font=("Courier", 14))

    # Frame for form
    LabelFrame = Frame(root, bg="RosyBrown3")
    LabelFrame.place(relx=0.1, rely=0.37, relwidth=0.8, relheight=0.4)

    # Accession Number 
    lb1 = Label(LabelFrame, text="Accession Number: ", bg="RosyBrown3", fg="black")
    lb1.place(relx=0.05, rely=0.2, relheight=0.15)
    # Entry label for Accession Number 
    en1 = Entry(LabelFrame)
    en1.place(relx=0.35, rely=0.2, relwidth=0.62, relheight=0.15)

    # Membership ID
    lb2 = Label(LabelFrame, text="Membership ID: ", bg="RosyBrown3", fg="black")
    lb2.place(relx=0.05, rely=0.4, relheight=0.15)
    # Entry label for Membership ID
    en2 = Entry(LabelFrame)
    en2.place(relx=0.35, rely=0.4, relwidth=0.62, relheight=0.15)

    # Reserve Date
    lb3 = Label(LabelFrame, text="Reserve Date \n (YYYY-MM-DD): ", bg="RosyBrown3", fg="black")
    lb3.place(relx=0.05, rely=0.6, relheight=0.15)
    # Entry label for Reserve Date
    en3 = Entry(LabelFrame)
    en3.place(relx=0.35, rely=0.6, relwidth=0.62, relheight=0.15)
    
    # Submit Button
    SubmitBtn = Button(root, text="Reserve Book", bg="#d1ccc0", fg="black", command=confirmReservationDetails)
    SubmitBtn.place(relx=0.17, rely=0.85, relwidth=0.25, relheight=0.09)

    # Quit Button
    QuitBtn = Button(root, text="Back to \n Reservations Menu", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.60, rely=0.85, relwidth=0.25, relheight=0.09)
    
    root.mainloop()

#CONFIRMRESERVATIONDETAILS
def confirmReservationDetails():
    global root
    root = Tk()
    root.title("library")
    root.minsize(width=400, height=400)
    root.geometry("250x200")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="RosyBrown1")
    Canvas1.pack(expand=True, fill=BOTH)

    AccessionNumber = en1.get()
    MemberID = en2.get()
    ReserveDate = en3.get()

    # check for valid accession number 
    try: 
        cursor.execute("SELECT * FROM Book WHERE AccessionNumber = '" + AccessionNumber + "'")
        records = cursor.fetchall()
        BookTitle = records[0][1]

        # check if book is already reserved
        bookReservedMemberID = records[0][5]
        if  bookReservedMemberID != None and bookReservedMemberID != "":
            messagebox.showinfo("Error", "Book is already reserved.")
            root.withdraw()
            
    except:
        messagebox.showinfo("Error", "Invalid Accession Number.")
        root.withdraw()

    cursor.execute("SELECT * FROM Book WHERE Reserved_MemberID = '" + MemberID + "'")
    records3 = cursor.fetchall()
    numOfBooksReserved = len(records3)

    # check for valid member ID
    try: 
        cursor.execute("SELECT * FROM Member WHERE memberID = '" + MemberID + "'")
        records2 = cursor.fetchall()
        MemberName = records2[0][1]
        
        cursor.execute("SELECT * FROM Fine WHERE MemberID ='" + MemberID + "'")
        fineAmount = cursor.fetchall()
        outstandingFine = fineAmount[0][1]
        outstandingFineStr = str(outstandingFine)

        if numOfBooksReserved == 2:
            messagebox.showinfo("Error!", "Member currently has 2 Books on Reservation")
            root.withdraw()
            
        elif outstandingFine > 0:
            messagebox.showinfo("Error!", "Member has Outstanding Fine of: $" + outstandingFineStr)
            root.withdraw()

        else: 
            headingFrame1 = Frame(root, bg="RosyBrown1", bd=5)
            headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

            # Add a leabel to heading Frame
            headingLabel = Label(headingFrame1, text="Confirm details", bg="white", fg="black", font=('Courier',15))
            headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

            # Add a label frame to canvas 
            LabelFrame = Frame(root, bg="RosyBrown3")
            LabelFrame.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.4)

            lb1 = Label(LabelFrame, text="Accession Number: " + AccessionNumber, bg="RosyBrown3", fg="black")
            lb1.place(relx=0.01, rely=0.05)
            lb1.config(font=("Courier", 11))

            lb2 = Label(LabelFrame, text="Book Title: " + BookTitle, bg="RosyBrown3", fg="black")
            lb2.place(relx=0.01, rely=0.2)
            lb2.config(font=("Courier", 11))

            lb3 = Label(LabelFrame, text="Membership ID: " + MemberID, bg="RosyBrown3", fg="black")
            lb3.place(relx=0.01, rely=0.35)
            lb3.config(font=("Courier", 11))

            lb4 = Label(LabelFrame, text="Member Name: " + MemberName, bg="RosyBrown3", fg="black")
            lb4.place(relx=0.01, rely=0.5)
            lb4.config(font=("Courier", 11))

            lb5 = Label(LabelFrame, text="Reserve Date: " + ReserveDate, bg="RosyBrown3", fg="black")
            lb5.place(relx=0.01, rely=0.65)
            lb5.config(font=("Courier", 11))
            

            Confirm = Button(root, text="Confirm Reservation", bg="RosyBrown3", fg="black", command=confirmReservation)
            Confirm.place(relx=0.04, rely=0.86, relwidth=0.35, relheight=0.10)

            Back = Button(root, text="Return to \n Reservations Function", bg="#f7f1e3", fg="black", command=root.destroy)
            Back.place(relx=0.52, rely=0.86, relwidth=0.45, relheight=0.10)
    except:
        messagebox.showinfo("Error", "Invalid Membership ID.")
        root.withdraw()
    

    root.mainloop()

#CONFIRMRESERVATION
def confirmReservation():
    AccessionNumber = en1.get()
    MemberID = en2.get()
    ReserveDate = en3.get()

    try: 
        # Update Book Reserved_MemberID and ReserveDate
        sql_update_query = """Update Book SET Reserved_MemberID = %s, ReserveDate = %s WHERE AccessionNumber = %s"""
        val = (MemberID, ReserveDate, AccessionNumber)
        cursor.execute(sql_update_query,val)
        connection.commit()

        messagebox.showinfo("Success!", "Book successfully reserved")
        
    except:
        messagebox.showinfo("Error", "Invalid Reserve Date. Please key in YYYY-MM-DD format.")
        root.withdraw()
    
    root.mainloop()


#CANCELRESERVATION
def cancelReservation():
    global en1, en2, en3, connection, cursor, Canvas1, bookTable, root
    
    root = Tk()
    root.title("library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    #add your own database name and password here to reflect in the code
    mypass = "pw"
    mydatabase = "library"

    connection = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cursor = connection.cursor()

    # Create the canvas for info
    Canvas1 = Canvas(root)
    Canvas1.config(bg="RosyBrown1") 
    Canvas1.pack(expand=True, fill=BOTH)
    
    # Add a heading Frame
    headingFrame1 = Frame(root, bg="RosyBrown1", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Cancel Reservation", bg="white", fg="black", font=('Courier',25))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Frame for form
    LabelFrame1 = Frame(root, bg="RosyBrown1")
    LabelFrame1.place(relx=0.03, rely=0.3, relwidth=1, relheight=0.6)

    lb = Label(LabelFrame1, text="To cancel a reservation, please enter the required information below: ", bg="RosyBrown1", fg="black")
    lb.place(relx=0, rely=0, relheight=0.08)
    lb.config(font=("Courier", 14))

    # Frame for form
    LabelFrame = Frame(root, bg="RosyBrown3")
    LabelFrame.place(relx=0.1, rely=0.37, relwidth=0.8, relheight=0.4)

    # Accession Number 
    lb1 = Label(LabelFrame, text="Accession Number: ", bg="RosyBrown3", fg="black")
    lb1.place(relx=0.05, rely=0.2, relheight=0.15)
    # Entry label for Accession Number 
    en1 = Entry(LabelFrame)
    en1.place(relx=0.35, rely=0.2, relwidth=0.62, relheight=0.15)

    # Membership ID
    lb2 = Label(LabelFrame, text="Membership ID: ", bg="RosyBrown3", fg="black")
    lb2.place(relx=0.05, rely=0.4, relheight=0.15)
    # Entry label for Membership ID
    en2 = Entry(LabelFrame)
    en2.place(relx=0.35, rely=0.4, relwidth=0.62, relheight=0.15)

    # Reserve Date
    lb3 = Label(LabelFrame, text="Cancellation Date \n (YYYY-MM-DD): ", bg="RosyBrown3", fg="black")
    lb3.place(relx=0.05, rely=0.6, relheight=0.15)
    # Entry label for Reserve Date
    en3 = Entry(LabelFrame)
    en3.place(relx=0.35, rely=0.6, relwidth=0.62, relheight=0.15)
    
    # Submit Button
    SubmitBtn = Button(root, text="Cancel Reservation", bg="#d1ccc0", fg="black", command=confirmCancellationDetails)
    SubmitBtn.place(relx=0.17, rely=0.85, relwidth=0.25, relheight=0.09)

    # Quit Button
    QuitBtn = Button(root, text="Back to \n Reservations Menu", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.60, rely=0.85, relwidth=0.25, relheight=0.09)
    
    root.mainloop()

#CONFIRMCANCELLATIONDETAILS
def confirmCancellationDetails():
    global root
    root = Tk()
    root.title("library")
    root.minsize(width=400, height=400)
    root.geometry("250x200")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="RosyBrown1")
    Canvas1.pack(expand=True, fill=BOTH)

    AccessionNumber = en1.get()
    MemberID = en2.get()
    CancellationDate = en3.get()

    try: 
        cursor.execute("SELECT * FROM Book WHERE AccessionNumber = '" + AccessionNumber + "'")
        records = cursor.fetchall()
        BookTitle = records[0][1]
    except:
        messagebox.showinfo("Error", "Invalid Accession Number.")
        root.withdraw()

    try:
        cursor.execute("select * FROM Member WHERE MemberID = '" + MemberID + "'")
        records2 = cursor.fetchall()
        MemberName = records2[0][1]
    except:
        messagebox.showinfo("Error", "Invalid Membership ID.")
        root.withdraw()

    try: 
        MemberWhoReservedBook = records[0][5]

        if MemberWhoReservedBook == MemberID: 
            headingFrame1 = Frame(root, bg="RosyBrown1", bd=5)
            headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

            # Add a leabel to heading Frame
            headingLabel = Label(headingFrame1, text="Confirm details", bg="white", fg="black", font=('Courier',15))
            headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

            # Add a label frame to canvas 
            LabelFrame = Frame(root, bg="RosyBrown3")
            LabelFrame.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.4)

            lb1 = Label(LabelFrame, text="Accession Number: " + AccessionNumber, bg="RosyBrown3", fg="black")
            lb1.place(relx=0.01, rely=0.05)
            lb1.config(font=("Courier", 11))

            lb2 = Label(LabelFrame, text="Book Title: " + BookTitle, bg="RosyBrown3", fg="black")
            lb2.place(relx=0.01, rely=0.2)
            lb2.config(font=("Courier", 11))

            lb3 = Label(LabelFrame, text="Membership ID: " + MemberID, bg="RosyBrown3", fg="black")
            lb3.place(relx=0.01, rely=0.35)
            lb3.config(font=("Courier", 11))

            lb4 = Label(LabelFrame, text="Member Name: " + MemberName, bg="RosyBrown3", fg="black")
            lb4.place(relx=0.01, rely=0.5)
            lb4.config(font=("Courier", 11))

            lb5 = Label(LabelFrame, text="Cancellation Date: " + CancellationDate, bg="RosyBrown3", fg="black")
            lb5.place(relx=0.01, rely=0.65)
            lb5.config(font=("Courier", 11))

            Confirm = Button(root, text="Confirm Cancellation", bg="RosyBrown3", fg="black", command=confirmCancellation)
            Confirm.place(relx=0.04, rely=0.86, relwidth=0.35, relheight=0.10)

            Back = Button(root, text="Return to \n Cancellation Function", bg="#f7f1e3", fg="black", command=root.destroy)
            Back.place(relx=0.52, rely=0.86, relwidth=0.45, relheight=0.10)

        else: 
            messagebox.showinfo("Error!", "Member has no such reservation.")
            root.withdraw()
        
    except:
        messagebox.showinfo("Error", "Member has no such reservation.")
        root.withdraw()
        
    
    root.mainloop()

#CONFIRMCANCELLATION
def confirmCancellation():
    AccessionNumber = en1.get()
    CancellationDate = en3.get()
    canRun = True
    
    # checking if cancellation date is in the correct YYYY-MM-DD format
    try:
        sql_update_query = """Update Book SET ReserveDate = %s WHERE AccessionNumber = %s"""
        val = (CancellationDate, AccessionNumber)
        cursor.execute(sql_update_query, val)
        connection.commit()
    except:
        messagebox.showinfo("Error", "Invalid Cancellation Date. Please key in YYYY-MM-DD format.")
        canRun = False

    if canRun: 
        # Update Book Reserved_MemberID and ReserveDate
        sql_update_query1 = """Update Book SET Reserved_MemberID = %s, ReserveDate = %s WHERE AccessionNumber = %s"""
        val1 = ("", None, AccessionNumber)
        cursor.execute(sql_update_query1, val1)
        connection.commit()

        messagebox.showinfo("Success!", "Book reservation successfully cancelled")
        
    root.mainloop() 

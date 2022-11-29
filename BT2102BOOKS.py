from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from tkinter import font
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

###main
##root = Tk()
##root.title("Library")
##helv30 = font.Font(family='Helvetica', size=30)
##helv15 = font.Font(family='Helvetica', size=15)
##
##
###FUNCTION
##def Books():
##    textentry = Entry(root, width = 20)
##    textentry.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.8)
##
###photo
##canv = Canvas(root, width=1000, height=1000, bg='white')
##canv.grid(row=0, column=0)
##resized_image2=Image.open("Stack-of-Books-Clipart.jpeg").resize((500,600), Image.ANTIALIAS)
##image2 = ImageTk.PhotoImage(resized_image2)
##canv.create_image(100, 175, anchor=NW, image=image2)
##
###heading
##
##
##canv.create_text(500, 150, text="Books", fill="black", font=('Roman 70 bold'))
##canv.pack()
##
##canv.create_text(750, 300, text="Please select an option:", fill="black", font=('Helvetica 20 bold'))
##canv.pack()


#REGISTERBOOK

def bookRegister():
    
    AcessionNumber = en1.get()
    title = en2.get()
    authors = en3.get()
    isbn = en4.get()
    Publisher = en5.get()
    PublicationYear = en6.get()

        

    String = "A"
    String += AcessionNumber[1:]
        
    
   
    sql = "INSERT INTO Book (AccessionNumber, Title,Isbn,Publisher,PublicationYear) VALUES (%s, %s, %s, %s, %s)"
    val = (String,title,isbn,Publisher,PublicationYear)

    sql2 = "INSERT INTO Authors VALUES (%s, %s)"

    sql3 = "INSERT INTO StatusOfBook VALUES (%s, %s)"
    val3 = ("Available",String)

    sql_select_Query_2 = "select * FROM Book"
    cur.execute(sql_select_Query_2)
    recordsBook = cur.fetchall()

    breaked = True

    for i in recordsBook:
        if i[0] == String:
            breaked = False
        else:
            continue
            
    if String!="" and title!="" and isbn!="" and Publisher!="" and PublicationYear!="" and breaked:
        try:
            cur.execute(sql,val)
            con.commit()
            cur.execute(sql3,val3)
            con.commit()
            messagebox.showinfo("Success!","New Book added in Library.")

            author_list = authors.split(",")
            for i in range(len(author_list)):
                if author_list[i][0] == " ":
                    new = author_list[i][1:]
                else:
                    new = author_list[i]
                val2 = (new,String)
                cur.execute(sql2,val2)
                con.commit()
        
                
        except:
            messagebox.showinfo("Error","Book already added; Duplicate, Missing or Incomplete fields")
    else:
        messagebox.showinfo("Error","Book already added; Duplicate, Missing or Incomplete fields")
    
    print(AcessionNumber)
    print(title)
    print(isbn)
    print(Publisher)
    print(PublicationYear)


    


#ADDBOOK
def addBooks():     
    global en1, en2, en3, en4, en5, en6, Canvas1, cur, con, bookTable, root
    
    root = Tk()
    root.title("library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "12345678"
    mydatabase="library"

    con = mysql.connector.connect(host="localhost",user="root",password="pw",database="library")
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "Book" # Book Table

     #create the canvas for info
    Canvas1 = Canvas(root)
    Canvas1.config(bg="RosyBrown1")
    Canvas1.pack(expand=True, fill=BOTH)


    #add a heading Frame
    headingFrame1 = Frame(root, bg="RosyBrown1", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Books", bg="white", fg="black", font=('Courier',30))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #frame for form
    LabelFrame1 = Frame(root, bg="RosyBrown1")
    LabelFrame1.place(relx=0.03, rely=0.3, relwidth=1, relheight=0.6)

    lb = Label(LabelFrame1, text="For new book acquisition, please enter the required information below: ", bg="RosyBrown1", fg="black")
    lb.place(relx=0, rely=0, relheight=0.08)
    lb.config(font=("Courier", 14))

    

    #frame for form
    LabelFrame = Frame(root, bg="RosyBrown3")
    LabelFrame.place(relx=0.1, rely=0.37, relwidth=0.8, relheight=0.4)

    #aCESSIONnUMBER
    lb1 = Label(LabelFrame, text="Accession Number : ", bg="RosyBrown3", fg="black")
    lb1.place(relx=0.05, rely=0.1, relheight=0.08)
    #entry label for book Id
    en1 = Entry(LabelFrame)
    en1.place(relx=0.35, rely=0.1, relwidth=0.62, relheight=0.08)

    #title
    lb2 = Label(LabelFrame, text="Title: ", bg="RosyBrown3", fg="black")
    lb2.place(relx=0.05, rely=0.25, relheight=0.08)
    #entry for title
    en2 = Entry(LabelFrame)
    en2.place(relx=0.35, rely=0.25, relwidth=0.62, relheight=0.08)

    #author
    lb3 = Label(LabelFrame, text="Authors: ", bg="RosyBrown3", fg="black")
    lb3.place(relx=0.05, rely=0.4, relheight=0.08)
    #entry for author
    en3 = Entry(LabelFrame)
    en3.place(relx=0.35, rely=0.4, relwidth=0.62, relheight=0.08)

    #ISBN
    lb4 = Label(LabelFrame, text="ISBN: ", bg="RosyBrown3", fg="black")
    lb4.place(relx=0.05, rely=0.55, relheight=0.08)
    #entry for isbn
    en4 = Entry(LabelFrame)
    en4.place(relx=0.35, rely=0.55, relwidth=0.62, relheight=0.08)

    #Publisher
    lb5 = Label(LabelFrame, text="Publisher: ", bg="RosyBrown3", fg="black")
    lb5.place(relx=0.05, rely=0.7, relheight=0.08)
    #entry for publisher
    en5 = Entry(LabelFrame)
    en5.place(relx=0.35, rely=0.7, relwidth=0.62, relheight=0.08)

    #Publication year
    lb6 = Label(LabelFrame, text="Publication year: ", bg="RosyBrown3", fg="black")
    lb6.place(relx=0.05, rely=0.85, relheight=0.08)
    #entry for publisher year
    en6 = Entry(LabelFrame)
    en6.place(relx=0.35, rely=0.85, relwidth=0.62, relheight=0.08)



    #submit Button
    SubmitBtn = Button(root, text="Add new book", bg="#d1ccc0", fg="black", command=bookRegister)
    SubmitBtn.place(relx=0.17, rely=0.85, relwidth=0.25, relheight=0.09)

    #Quit button
    QuitBtn = Button(root, text="Return to Books menu", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.60, rely=0.85, relwidth=0.25, relheight=0.09)

    root.mainloop()

#delete
issue_Table = "libInsertBook"

def deleteBook():
    root.destroy()
    AcessionNumber = en1.get()
    
    String = "A"
    String += AcessionNumber[1:]

    sql_select_Query_2 = "select * FROM Book"
    cursor.execute(sql_select_Query_2)
    records2 = cursor.fetchall()

    emptyborrowedid = False
    emptyreservedid = False

    status = ""
    for row in records2:
        if row[0] == String:
            if row[5] == None:
                emptyreservedid = True
            if row[6] == None:
                emptyborrowedid = True      
        else:
            continue
    if emptyborrowedid and emptyreservedid:
        try:
            cursor.execute("DELETE FROM Book WHERE AccessionNumber = '"+String+"'")
            connection.commit()
            messagebox.showinfo("Success", "Book Deleted Successfully")
        except:
            messagebox.showinfo("Error", "Please check Book Accession Number")
    else:
        if emptyreservedid:
            messagebox.showinfo("Error", "Book is currently on Loan")
        else:
            messagebox.showinfo("Error", "Book is currently Reserved")
            
    print(AcessionNumber)

    en1.delete(0, END)
    

def delete():
    global en1, Canvas1, bookTable

    root = Tk()
    root.title("library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="plum1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="plum1", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="Delete Book", bg="white", fg="black", font=('Courier',25))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(root, bg="plum3")
    LabelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.4)

    #take a book AN to delete
    lb2 = Label(LabelFrame, text="Accession Number : ", bg="plum3", fg="black")
    lb2.place(relx=0.1, rely=0.3)
    lb2.config(font=("Courier", 15))

    en1 = Entry(LabelFrame)
    en1.place(relx=0.1, rely=0.45, relwidth=0.62)

    #submit button    
    submitBtn = Button(root, text="Withdraw Book", bg="plum3", fg="black", command=clicker)
    submitBtn.place(relx=0.15, rely=0.8, relwidth=0.25, relheight=0.09)

    QuitBtn = Button(root, text="Return to Books menu", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.60, rely=0.8, relwidth=0.25, relheight=0.09)

    root.mainloop()
    
def clicker():
    global  root, cursor, connection
    root = Tk()
    root.title("library")
    root.minsize(width=400, height=400)
    root.geometry("250x200")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="plum1")
    Canvas1.pack(expand=True, fill=BOTH)

    connection = mysql.connector.connect(host="localhost",user="root",password="pw",database="library")


    sql_select_Query = "select * FROM Book"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    
    sql_select_Query_2 = "select * FROM Authors"
    cursor.execute(sql_select_Query_2)
    records2 = cursor.fetchall()
    
    AcessionNumber = en1.get()
    title = ""
    isbn = ""
    publisher = ""
    publicationyear = ""
    newAN=""
    Authors= ""
    breaked = False

    for i in range(len(records2)):
        string = AcessionNumber[1:]
        if records2[i][1][1:] == string:
            Authors += records2[i][0]
            Authors += ","
            
        else:
            continue
    Authors = Authors[:-1]
            

    for row in records:
        string = AcessionNumber[1:]
        if row[0][1:]==string:
            newAN = "A" + string
            title= row[1]
            isbn= row[2]
            publisher= row[3]
            publicationyear= str(row[4])
            breaked = True
        else:
            continue
    
    

    AN ="Accession Number : "
    AN += newAN
    
    TT = "Title: "
    TT +=  title

    AR = "Authors: "
    AR += Authors
    
    IN = "Isbn: "
    IN += isbn
    
    PR = "Publisher: "
    PR += publisher
    
    PY = "Publication Year: "
    PY += publicationyear

    if breaked:
        headingFrame1 = Frame(root, bg="plum1", bd=5)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

         #add a leabel to heading Frame
        headingLabel = Label(headingFrame1, text="Confirm details", bg="white", fg="black", font=('Courier',15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        #add a label frame to canvas to give a lebl insite it to delete book
        LabelFrame = Frame(root, bg="plum3")
        LabelFrame.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.4)
        
        lb1 = Label(LabelFrame, text=AN, bg="plum3", fg="black")
        lb1.place(relx=0.01, rely=0.05)
        lb1.config(font=("Courier", 11))

        lb2 = Label(LabelFrame, text=TT, bg="plum3", fg="black")
        lb2.place(relx=0.01, rely=0.2)
        lb2.config(font=("Courier", 11))

        lb3 = Label(LabelFrame, text=AR, bg="plum3", fg="black")
        lb3.place(relx=0.01, rely=0.35)
        lb3.config(font=("Courier", 11))

        lb4 = Label(LabelFrame, text=IN, bg="plum3", fg="black")
        lb4.place(relx=0.01, rely=0.5)
        lb4.config(font=("Courier", 11))

        lb5 = Label(LabelFrame, text=PR, bg="plum3", fg="black")
        lb5.place(relx=0.01, rely=0.65)
        lb5.config(font=("Courier", 11))

        lb5 = Label(LabelFrame, text=PY, bg="plum3", fg="black")
        lb5.place(relx=0.01, rely=0.8)
        lb5.config(font=("Courier", 11))

        Confirm = Button(root, text="Confirm Withdraw", bg="plum3", fg="black", command=deleteBook)
        Confirm.place(relx=0.04, rely=0.86, relwidth=0.35, relheight=0.08)

        Back = Button(root, text="Return to Withdrawal menu", bg="#f7f1e3", fg="black", command=root.destroy)
        Back.place(relx=0.52, rely=0.86, relwidth=0.45, relheight=0.08)


    else:
        messagebox.showinfo("Error","Invalid Accession Number")
        root.withdraw()

    root.mainloop()
    

    
    
    
###Buttons
##
##btnAcquisition = Button(root,text="1. Book Acquisition",bg='black', fg='black',command=addBooks)
##btnAcquisition.place(relx=0.6,rely=0.45, relwidth=0.3, relheight=0.1)
##btnAcquisition['font'] = helv30
##
##btnWithdraw = Button(root,text="2. Book Withdrawal",bg='black', fg='black',command=delete)
##btnWithdraw.place(relx=0.6,rely=0.65, relwidth=0.3, relheight=0.1)
##btnWithdraw['font'] = helv30
##
##btnBack = Button(root,text="Back to Main Menu",bg='black', fg='black',command=Books)
##btnBack.place(relx=0.4,rely=0.925, relwidth=0.2, relheight=0.05)
##btnBack['font'] = helv15
##
##
##root.mainloop()









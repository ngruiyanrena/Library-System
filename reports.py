from urllib.parse import quote
from sqlalchemy.engine import create_engine
import sqlalchemy as db
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from tkinter import font
from tkinter import *
from PIL import Image, ImageTk


################################################################################ PASSWORD HERE
passphrase = "pw"
helv10b, helv15b, helv20b = ('Helvetica 10 bold'), ('Helvetica 10 bold'), ('Helvetica 20 bold')

engine = db.create_engine("mysql+pymysql://root:%s@localhost/library" % quote(passphrase))
connection = engine.connect()
metadata = db.MetaData()

book = db.Table('book', metadata, autoload=True, autoload_with=engine)
bookquery = db.select([book])
bookResultProxy = connection.execute(bookquery)
bookResultSet = bookResultProxy.fetchall()

statusofbook = db.Table('statusofbook', metadata, autoload=True, autoload_with=engine)
statusofbookquery = db.select([statusofbook])
statusofbookResultProxy = connection.execute(statusofbookquery)
statusofbookResultSet = statusofbookResultProxy.fetchall()

authors = db.Table('authors', metadata, autoload=True, autoload_with=engine)
authorsquery = db.select([authors])
authorsResultProxy = connection.execute(authorsquery)
authorsResultSet = authorsResultProxy.fetchall()

member = db.Table('member', metadata, autoload=True, autoload_with=engine)
memberquery = db.select([member])
memberResultProxy = connection.execute(memberquery)
memberResultSet = memberResultProxy.fetchall()

fine = db.Table('fine', metadata, autoload=True, autoload_with=engine)
finequery = db.select([fine])
fineResultProxy = connection.execute(finequery)
fineResultSet = fineResultProxy.fetchall()

##root = Tk()
##root.title("Reports")
##root.minsize(width=400,height=400)
##root.geometry("600x500")
##
##Canvas1 = Canvas(root) 
##Canvas1.config(bg="#F5E1FD")
##Canvas1.pack(expand=True,fill=BOTH)

    
def ViewLoaned():
    
    root = Tk()
    root.title("Loaned")
    root.minsize(width=1200,height=800)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#F5E1FD")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#F5E1FD",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Books On Loan", bg='#966FD6', fg='white', font=helv20b)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)

    engine = db.create_engine("mysql+pymysql://root:%s@localhost/library" % quote(passphrase))
    connection = engine.connect()
    metadata = db.MetaData()

    book = db.Table('book', metadata, autoload=True, autoload_with=engine)
    bookquery = db.select([book])
    bookResultProxy = connection.execute(bookquery)
    bookResultSet = bookResultProxy.fetchall()

    statusofbook = db.Table('statusofbook', metadata, autoload=True, autoload_with=engine)
    statusofbookquery = db.select([statusofbook])
    statusofbookResultProxy = connection.execute(statusofbookquery)
    statusofbookResultSet = statusofbookResultProxy.fetchall()

    authors = db.Table('authors', metadata, autoload=True, autoload_with=engine)
    authorsquery = db.select([authors])
    authorsResultProxy = connection.execute(authorsquery)
    authorsResultSet = authorsResultProxy.fetchall()

    loanedbooklist = []
    for bookstatus in statusofbookResultSet:
        if bookstatus[0] == "Loaned":
            loanedbooklist.append(bookstatus[-1])

    finalList = []
    for book in bookResultSet:
        if book[0] in loanedbooklist:
            authorlist = ""
            for author in authorsResultSet:
                if author[-1] == book[0]:
                    authorlist = authorlist + author[0] + ", "
            authorlist = authorlist[:-2]
            holder = book[:]
            holder+=(authorlist,)
            finalList.append(holder)

    printorder = [0, 1, -1, 2, 3, 4]
    printspace = [0.07, 0.12, 0.4, 0.6, 0.7, 0.9]

    loanedheadings = ('No.','Title','Author','ISBN', 'Publisher','P. Yr.')
    counter = 0
    for i in loanedheadings:
        x = printspace[counter]
        counter += 1
        Label(labelFrame, text= i, bg = 'black', fg='white').place(relx=x,rely=0.1)
        
    
    for i in finalList:
        counter = 0
        for j in printorder:
            x = printspace[counter]
            counter += 1
            Label(labelFrame, text = i[j],bg = 'black', fg = 'white').place(relx = x, rely = y)
        y += 0.1
        
    
    quitBtn = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    
    root.mainloop()


def ViewReserved():
    
    root = Tk()
    root.title("Reserved")
    root.minsize(width=1200,height=800)
    root.geometry("600x500")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#F5E1FD")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#F5E1FD",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Books Reserved", bg='#966FD6', fg='white', font=helv20b)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    engine = db.create_engine("mysql+pymysql://root:%s@localhost/library" % quote(passphrase))
    connection = engine.connect()
    metadata = db.MetaData()

    book = db.Table('book', metadata, autoload=True, autoload_with=engine)
    bookquery = db.select([book])
    bookResultProxy = connection.execute(bookquery)
    bookResultSet = bookResultProxy.fetchall()

    statusofbook = db.Table('statusofbook', metadata, autoload=True, autoload_with=engine)
    statusofbookquery = db.select([statusofbook])
    statusofbookResultProxy = connection.execute(statusofbookquery)
    statusofbookResultSet = statusofbookResultProxy.fetchall()

    authors = db.Table('authors', metadata, autoload=True, autoload_with=engine)
    authorsquery = db.select([authors])
    authorsResultProxy = connection.execute(authorsquery)
    authorsResultSet = authorsResultProxy.fetchall()

    member = db.Table('member', metadata, autoload=True, autoload_with=engine)
    memberquery = db.select([member])
    memberResultProxy = connection.execute(memberquery)
    memberResultSet = memberResultProxy.fetchall()

    fine = db.Table('fine', metadata, autoload=True, autoload_with=engine)
    finequery = db.select([fine])
    fineResultProxy = connection.execute(finequery)
    fineResultSet = fineResultProxy.fetchall()
    
    Label(labelFrame, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)

    reservedbooklist = []
    for book in bookResultSet:
        if book[5]:
            reservedbooklist.append(book[0])

    finalList = []
    for book in bookResultSet:
        if book[0] in reservedbooklist:
            authorlist = ""
            for author in authorsResultSet:
                if author[1] == book[0]:
                    authorlist = authorlist + author[0] + ", "
            authorlist = authorlist[:-2]
            holder = book[:]
            holder+=(authorlist,)
            finalList.append(holder)

    printorder = [0, 1, -1, 2, 3, 4]
    printspace = [0.07, 0.12, 0.4, 0.6, 0.7, 0.9]

    loanedheadings = ('No.','Title','Author','ISBN', 'Publisher','P. Yr.')
    counter = 0
    
    for i in loanedheadings:
        x = printspace[counter]
        counter += 1
        Label(labelFrame, text= i, bg = 'black', fg='white').place(relx=x,rely=0.1)
        
    
    for i in finalList:
        counter = 0
        for j in printorder:
            x = printspace[counter]
            counter += 1
            Label(labelFrame, text = i[j],bg = 'black', fg = 'white').place(relx = x, rely = y)
        y += 0.1
    
    quitBtn = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    
    root.mainloop()


def ViewFined():
    
    root = Tk()
    root.title("Outstanding Fines")
    root.minsize(width=1200,height=800)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#F5E1FD")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#F5E1FD",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Outstanding Fines", bg='#966FD6', fg='white', font=helv20b)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    engine = db.create_engine("mysql+pymysql://root:%s@localhost/library" % quote(passphrase))
    connection = engine.connect()
    metadata = db.MetaData()

    book = db.Table('book', metadata, autoload=True, autoload_with=engine)
    bookquery = db.select([book])
    bookResultProxy = connection.execute(bookquery)
    bookResultSet = bookResultProxy.fetchall()

    statusofbook = db.Table('statusofbook', metadata, autoload=True, autoload_with=engine)
    statusofbookquery = db.select([statusofbook])
    statusofbookResultProxy = connection.execute(statusofbookquery)
    statusofbookResultSet = statusofbookResultProxy.fetchall()

    authors = db.Table('authors', metadata, autoload=True, autoload_with=engine)
    authorsquery = db.select([authors])
    authorsResultProxy = connection.execute(authorsquery)
    authorsResultSet = authorsResultProxy.fetchall()

    member = db.Table('member', metadata, autoload=True, autoload_with=engine)
    memberquery = db.select([member])
    memberResultProxy = connection.execute(memberquery)
    memberResultSet = memberResultProxy.fetchall()

    fine = db.Table('fine', metadata, autoload=True, autoload_with=engine)
    finequery = db.select([fine])
    fineResultProxy = connection.execute(finequery)
    fineResultSet = fineResultProxy.fetchall()

    
    Label(labelFrame, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)

    printorder = [0, 1, 2, 3, 4]
    printspace = [0.07, 0.20, 0.4, 0.6, 0.8]

    loanedheadings = ('Member ID','Name','Faculty','Phone Number', 'Email Address')
    counter = 0
    
    for i in loanedheadings:
        x = printspace[counter]
        counter += 1
        Label(labelFrame, text= i, bg = 'black', fg='white').place(relx=x,rely=0.1)

    if fineResultSet:
        finedpeople = []
        for person in fineResultSet:
            if person[1]:
                finedpeople.append(person[0])
        finalfinedList = []
        for member in memberResultSet:
            if member[0] in finedpeople:
                finalfinedList.append(member)   
            
        
        for i in finalfinedList:
            counter = 0
            for j in printorder:
                x = printspace[counter]
                counter += 1
                Label(labelFrame, text = i[j],bg = 'black', fg = 'white').place(relx = x, rely = y)
            y += 0.1

    quitBtn = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    
    root.mainloop()


def ViewLoanMember():
    global bookInfo1

    root = Tk()
    root.title("Loaned to Member")
    root.minsize(width=1200,height=800)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#F5E1FD")
    Canvas1.pack(expand=True,fill=BOTH)

    #add a heading Frame
    headingFrame1 = Frame(root, bg="#F5E1FD", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Books on loan to Member", bg="white", fg="black", font=('Courier',24))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #Membership ID
    LabelFrame = Frame(root, bg="#F5E1FD")
    LabelFrame.place(relx=0.1, rely=0.37, relwidth=0.8, relheight=0.4)
    lb1 = Label(LabelFrame, text="Membership ID: ", bg="#F5E1FD", fg="black")
    lb1.place(relx=0.1, rely=0.3)
    lb1.config(font=("Courier", 15))
    #Entry for Membership ID
    bookInfo1 = Entry(LabelFrame)
    bookInfo1.place(relx=0.1, rely=0.45, relwidth=0.62, relheight=0.15)
    
    #Submit Button
    SubmitBtn = Button(root, text="Search member", bg="#d1ccc0", fg="black", command=ViewLoaned2)
    SubmitBtn.place(relx=0.17, rely=0.85, relwidth=0.25, relheight=0.09)

    #Quit button
    QuitBtn = Button(root, text="Return to Reports menu", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.60, rely=0.85, relwidth=0.3, relheight=0.09)
    root.mainloop()

    
def ViewLoaned2():
    global bookInfo1
    engine = db.create_engine("mysql+pymysql://root:%s@localhost/library" % quote(passphrase))
    connection = engine.connect()
    metadata = db.MetaData()

    member = db.Table('member', metadata, autoload=True, autoload_with=engine)
    memberquery = db.select([member])
    memberResultProxy = connection.execute(memberquery)
    memberResultSet = memberResultProxy.fetchall()
    membList = [member[0] for member in memberResultSet]

    try:
        if bookInfo1.get() not in membList:
            messagebox.showinfo("Error!","Member ID does not exist")

        else: 
            
            root = Tk()
            root.title("Loaned to Member")
            root.minsize(width=1200,height=800)
            root.geometry("600x500")


            Canvas1 = Canvas(root) 
            Canvas1.config(bg="#F5E1FD")
            Canvas1.pack(expand=True,fill=BOTH)
                
                
            headingFrame1 = Frame(root,bg="#F5E1FD",bd=5)
            headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
                
            headingLabel = Label(headingFrame1, text="Books On Loan to: " + bookInfo1.get(), bg='#966FD6', fg='white', font=helv20b)
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            
            labelFrame = Frame(root,bg='black')
            labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
            y = 0.25

            engine = db.create_engine("mysql+pymysql://root:%s@localhost/library" % quote(passphrase))
            connection = engine.connect()
            metadata = db.MetaData()

            book = db.Table('book', metadata, autoload=True, autoload_with=engine)
            bookquery = db.select([book])
            bookResultProxy = connection.execute(bookquery)
            bookResultSet = bookResultProxy.fetchall()

            statusofbook = db.Table('statusofbook', metadata, autoload=True, autoload_with=engine)
            statusofbookquery = db.select([statusofbook])
            statusofbookResultProxy = connection.execute(statusofbookquery)
            statusofbookResultSet = statusofbookResultProxy.fetchall()

            authors = db.Table('authors', metadata, autoload=True, autoload_with=engine)
            authorsquery = db.select([authors])
            authorsResultProxy = connection.execute(authorsquery)
            authorsResultSet = authorsResultProxy.fetchall()

            member = db.Table('member', metadata, autoload=True, autoload_with=engine)
            memberquery = db.select([member])
            memberResultProxy = connection.execute(memberquery)
            memberResultSet = memberResultProxy.fetchall()

            fine = db.Table('fine', metadata, autoload=True, autoload_with=engine)
            finequery = db.select([fine])
            fineResultProxy = connection.execute(finequery)
            fineResultSet = fineResultProxy.fetchall()
            
            Label(labelFrame, text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
            
            loanedbooklist = []
            for bookstatus in statusofbookResultSet:
                if bookstatus[0] == "Loaned":
                    loanedbooklist.append(bookstatus[-1])

            finalList = []
            for book in bookResultSet:
                if book[0] in loanedbooklist and book[6] == bookInfo1.get():
                    authorlist = ""
                    for author in authorsResultSet:
                        if author[-1] == book[0]:
                            authorlist = authorlist + author[0] + ", "
                    authorlist = authorlist[:-2]
                    holder = book[:]
                    holder+=(authorlist,)
                    finalList.append(holder)

            printorder = [0, 1, -1, 2, 3, 4]
            printspace = [0.07, 0.12, 0.4, 0.6, 0.7, 0.9]

            loanedheadings = ('No.','Title','Author','ISBN', 'Publisher','P. Yr.')
            counter = 0
            for i in loanedheadings:
                x = printspace[counter]
                counter += 1
                Label(labelFrame, text= i, bg = 'black', fg='white').place(relx=x,rely=0.1)
                
            
            for i in finalList:
                counter = 0
                for j in printorder:
                    x = printspace[counter]
                    counter += 1
                    Label(labelFrame, text = i[j],bg = 'black', fg = 'white').place(relx = x, rely = y)
                y += 0.1

            bookInfo1.delete(0, END)
            
            quitBtn = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
            quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

            
            root.mainloop()
            
    except:
        messagebox.showinfo("Error!","No Member ID was inputted")

def Search():

    engine = db.create_engine("mysql+pymysql://root:%s@localhost/library" % quote(passphrase))
    connection = engine.connect()
    metadata = db.MetaData()
    book = db.Table('book', metadata, autoload=True, autoload_with=engine)
    bookquery = db.select([book])
    bookResultProxy = connection.execute(bookquery)
    bookResultSet = bookResultProxy.fetchall()
    authors = db.Table('authors', metadata, autoload=True, autoload_with=engine)
    authorsquery = db.select([authors])
    authorsResultProxy = connection.execute(authorsquery)
    authorsResultSet = authorsResultProxy.fetchall()

    root = Tk()
    root.title("Search")
    root.minsize(width=600,height=500)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#F5E1FD")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#966FD6",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.15)

    headingLabel = Label(headingFrame1, text="Book Search", bg='#966FD6', fg='white', font=helv20b)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    bookInfoTitle = Entry(root)
    bookInfoTitle.place(relx=0.4,rely=0.3,relwidth=0.4,relheight=0.05)
    TitleLabel = Label(root, text="Title",bg = '#966FD6', fg='white', font=helv10b)
    TitleLabel.place(relx=0.2,rely=0.3, relwidth=0.2, relheight=0.05)

    bookInfoAuthor = Entry(root)
    bookInfoAuthor.place(relx=0.4,rely=0.4,relwidth=0.4,relheight=0.05)
    AuthorLabel = Label(root, text="Author",bg = '#966FD6', fg='white', font=helv10b)
    AuthorLabel.place(relx=0.2,rely=0.4, relwidth=0.2, relheight=0.05)

    bookInfoISBN = Entry(root)
    bookInfoISBN.place(relx=0.4,rely=0.5,relwidth=0.4,relheight=0.05)
    ISBNLabel = Label(root, text="ISBN",bg = '#966FD6', fg='white', font=helv10b)
    ISBNLabel.place(relx=0.2,rely=0.5, relwidth=0.2, relheight=0.05)

    bookInfoPublisher = Entry(root)
    bookInfoPublisher.place(relx=0.4,rely=0.6,relwidth=0.4,relheight=0.05)
    PublisherLabel = Label(root, text="Publisher",bg = '#966FD6', fg='white', font=helv10b)
    PublisherLabel.place(relx=0.2,rely=0.6, relwidth=0.2, relheight=0.05)

    bookInfoYear = Entry(root)
    bookInfoYear.place(relx=0.4,rely=0.7,relwidth=0.4,relheight=0.05)
    YearLabel = Label(root, text="Pub. Year",bg = '#966FD6', fg='white', font=helv10b)
    YearLabel.place(relx=0.2,rely=0.7, relwidth=0.2, relheight=0.05)

    def SearchBook():

        engine = db.create_engine("mysql+pymysql://root:%s@localhost/library" % quote(passphrase))
        connection = engine.connect()
        metadata = db.MetaData()
        book = db.Table('book', metadata, autoload=True, autoload_with=engine)
        bookquery = db.select([book])
        bookResultProxy = connection.execute(bookquery)
        bookResultSet = bookResultProxy.fetchall()
        authors = db.Table('authors', metadata, autoload=True, autoload_with=engine)
        authorsquery = db.select([authors])
        authorsResultProxy = connection.execute(authorsquery)
        authorsResultSet = authorsResultProxy.fetchall()

        numberInputs = bool(bookInfoTitle.get()) + bool(bookInfoAuthor.get()) + bool(bookInfoISBN.get()) + bool(bookInfoPublisher.get()) + bool(bookInfoYear.get())
        
        if numberInputs == 0:
            messagebox.showinfo("Error!","Please input search term")
            
        elif numberInputs != 1:
            messagebox.showinfo("Error!","Please input only one search term")
            
            
        elif " " in bookInfoTitle.get() or " " in bookInfoAuthor.get() or " " in bookInfoISBN.get() or " " in bookInfoPublisher.get() or " " in bookInfoYear.get():
            messagebox.showinfo("Error!","Please input only one word, no spaces")
            

        else:

            if bookInfoISBN.get():
                
                searchTerm = bookInfoISBN.get()
                finalList = []
                for book in bookResultSet:
                    if book[2] == searchTerm:
                        authorlist = ""
                        for author in authorsResultSet:
                            if author[-1] == book[0]:
                                authorlist = authorlist + author[0] + ", "
                        authorlist = authorlist[:-2]
                        holder = book[:]
                        holder+=(authorlist,)
                        finalList.append(holder)

            elif bookInfoYear.get():
                
                searchTerm = bookInfoYear.get()
                finalList = []
                for book in bookResultSet:
                    if book[4] == int(searchTerm):
                        authorlist = ""
                        for author in authorsResultSet:
                            if author[-1] == book[0]:
                                authorlist = authorlist + author[0] + ", "
                        authorlist = authorlist[:-2]
                        holder = book[:]
                        holder+=(authorlist,)
                        finalList.append(holder)

            elif bookInfoTitle.get():
                
                searchTerm = bookInfoTitle.get()
                searchTerm = searchTerm.lower()
                
                finalList = []
                for book in bookResultSet:
                    testVal = book[1].lower()
                    if testVal == searchTerm or (" " +searchTerm+" ") in testVal or (searchTerm+" ") == testVal[:len(searchTerm)+1] or (" " + searchTerm) == testVal[-len(searchTerm)-1:]:
                        authorlist = ""
                        for author in authorsResultSet:
                            if author[-1] == book[0]:
                                authorlist = authorlist + author[0] + ", "
                        authorlist = authorlist[:-2]
                        holder = book[:]
                        
                        holder+=(authorlist,)
                        finalList.append(holder)

            elif bookInfoPublisher.get():
                
                searchTerm = bookInfoPublisher.get()
                searchTerm = searchTerm.lower()
                
                finalList = []
                for book in bookResultSet:
                    testVal = book[3].lower()
                    if testVal == searchTerm or (" " +searchTerm+" ") in testVal or (searchTerm+" ") == testVal[:len(searchTerm)+1] or (" " + searchTerm) == testVal[-len(searchTerm)-1:]:
                        authorlist = ""
                        for author in authorsResultSet:
                            if author[-1] == book[0]:
                                authorlist = authorlist + author[0] + ", "
                        authorlist = authorlist[:-2]
                        holder = book[:]
                        
                        holder+=(authorlist,)
                        finalList.append(holder)

            elif bookInfoAuthor.get():
                
                searchTerm = bookInfoAuthor.get()
                searchTerm = searchTerm.lower()

                accenNo = []
                for author in authorsResultSet:
                    authorname = author[0]
                    testVal = authorname.lower()
                    if testVal == searchTerm or (" " +searchTerm+" ") in testVal or (searchTerm+" ") == testVal[:len(searchTerm)+1] or (" " + searchTerm) == testVal[-len(searchTerm)-1:]:
                        accenNo.append(author[1])
                        
                finalList = []
                for book in bookResultSet:
                    if book[0] in accenNo:
                        authorlist = ""
                        for author in authorsResultSet:
                            if author[-1] == book[0]:
                                authorlist = authorlist + author[0] + ", "
                        authorlist = authorlist[:-2]
                        holder = book[:]
                        holder+=(authorlist,)
                        finalList.append(holder)
                

            root1 = Tk()
            root1.title("Search Results")
            root1.minsize(width=1200,height=800)
            root1.geometry("600x500")

            Canvas1 = Canvas(root1) 
            Canvas1.config(bg="#F5E1FD")
            Canvas1.pack(expand=True,fill=BOTH)
                
            headingFrame1 = Frame(root1,bg="#F5E1FD",bd=5)
            headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
                
            headingLabel = Label(headingFrame1, text="Search Results for " + searchTerm, bg='#966FD6', fg='white', font=helv20b)
            headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
            
            labelFrame = Frame(root1,bg='black')
            labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
            y = 0.25
            
            Label(labelFrame, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)

            printorder = [0, 1, -1, 2, 3, 4]
            printspace = [0.07, 0.12, 0.4, 0.6, 0.7, 0.9]

            searchheadings = ('No.','Title','Author','ISBN', 'Publisher','P. Yr.')
            counter = 0
            for i in searchheadings:
                x = printspace[counter]
                counter += 1
                Label(labelFrame, text= i, bg = 'black', fg='white').place(relx=x,rely=0.1)
                
            
            for i in finalList:
                counter = 0
                for j in printorder:
                    x = printspace[counter]
                    counter += 1
                    Label(labelFrame, text = i[j],bg = 'black', fg = 'white').place(relx = x, rely = y)
                y += 0.05

            quitBtn = Button(root1,text="Quit",bg='white', fg='black', command=root1.destroy)
            quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)


    searchBtn = Button(root,text="Search",bg='white', fg='black', command = SearchBook)
    searchBtn.place(relx=0.2,rely=0.8, relwidth=0.2,relheight=0.1)
    
    quitBtn = Button(root,text="Back to Reports",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.6,rely=0.8, relwidth=0.2,relheight=0.1)

    root.mainloop()



##headingFrame1 = Frame(root,bg="#966FD6",bd=5)
##headingFrame1.place(relx=0.15,rely=0.1,relwidth=0.7,relheight=0.16)
##headingLabel = Label(headingFrame1, text="Reports Generator", bg='#966FD6', fg='white', font=helv20b)
##headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
##
##btn3 = Button(root,text="Books On Loan",bg = 'white', fg='black', command=ViewLoaned)
##btn3.place(relx=0.15,rely=0.3, relwidth=0.3,relheight=0.15)
##btn3['font'] = helv10b
##
##btn4 = Button(root,text="Books Reserved",bg = 'white',fg='black', command=ViewReserved)
##btn4.place(relx=0.15,rely=0.50, relwidth=0.3,relheight=0.15)
##btn4['font'] = helv10b
##
##btn5 = Button(root,text="Outstanding Fines",bg = 'white', fg='black', command=ViewFined)
##btn5.place(relx=0.55,rely=0.3, relwidth=0.3,relheight=0.15)
##btn5['font'] = helv10b
##
##btn6 = Button(root,text="On Loan To Member",bg = 'white',fg='black', command=ViewLoaned2)
##btn6.place(relx=0.55,rely=0.55, relwidth=0.3,relheight=0.10)
##btn6['font'] = helv10b
##
##btn7 = Button(root,text="Book Search",bg = 'white',fg='black', command = Search)
##btn7.place(relx=0.15,rely=0.70, relwidth=0.7,relheight=0.08)
##btn7['font'] = helv15b
##
##bookInfo1 = Entry(root)
##bookInfo1.place(relx=0.7,rely=0.5,relwidth=0.15,relheight=0.05)
##
##membLabel = Label(root, text="Member ID",bg = '#F5E1FD', fg='black', font=('Helvetica',10))
##membLabel.place(relx=0.55,rely=0.5, relwidth=0.15, relheight=0.05)
##
##btnback = Button(root,text="Back to Main Menu",bg = 'white', highlightbackground='LightBlue3', command = MainPg)
##btnback.place(relx=0.15,rely=0.80, relwidth=0.7,relheight=0.08)
##btnback['font'] = helv15b
##        
##root.mainloop()

from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
from MemberFunctions import *
from BT2102BOOKS import *
from BT2102LOANS import *
from LibReservations import *
from LibFinePayment import *
from reports import *


#main
root = Tk()
root.title("Library")

#font
helv30 = font.Font(family='Helvetica', size=30)
helvbold = font.Font(family='Helvetica', size=16, weight='bold')
helv15 = font.Font(family='Helvetica', size=15)
helv23 = font.Font(family='Helvetica', size=23)


### MEMBERSHIP MAIN PAGE
def MembershipMain():
    #destroy
    global btn1,btn2,btn3,btn4,btn5,btn6,canv
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    canv.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    btn6.destroy()
    

    #photos
    canv = Canvas(root, width=1000, height=1000, bg='white')
    canv.grid(row=2, column=3)
    resized_image1=Image.open("People-clipart-9.png").resize((400,500), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(resized_image1)
    canv.create_image(50, 170, anchor=NW, image=image1)
    label1 = Label(image=image1)
    label1.image = image1

    #heading
    canv.create_text(500, 150, text="Membership", fill="black", font=('Roman 70 bold'))
    canv.pack()
    canv.create_text(750, 300, text="Please select an option:", fill="black", font=('Helvetica 20 bold'))
    canv.pack()
    
    #buttons
    btn1 = Button(root,text="1. Membership Creation",fg='black',command=MemberCreation)
    btn1.place(relx=0.50,rely=0.25, relwidth=0.4, relheight=0.15)
    btn1['font'] = helv30

    btn2 = Button(root,text="2. Membership Deletion", fg='black',command=MemberDeleteMenu)
    btn2.place(relx=0.50,rely=0.43, relwidth=0.4, relheight=0.15)
    btn2['font'] = helv30

    btn3 = Button(root,text="3. Membership Update", fg='black',command=MemberUpdateMenu)
    btn3.place(relx=0.50,rely=0.61, relwidth=0.4, relheight=0.15)
    btn3['font'] = helv30

    btn4 = Button(root,text="Back to Main Menu", highlightbackground='LightBlue3',command=MainPg)
    btn4.place(relx=0.10,rely=0.82, relwidth=0.8, relheight=0.08)
    btn4['font'] = helvbold

    

### BOOKS MAIN PAGE
def BooksMain():
    global btnAcquisition,btnWithdraw,canv

    # destroy
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    canv.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    btn6.destroy()

    #photo
    canv = Canvas(root, width=1000, height=1000, bg='white')
    canv.grid(row=0, column=0)
    resized_image2=Image.open("Stack-of-Books-Clipart.jpeg").resize((400,500), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized_image2)
    canv.create_image(100, 175, anchor=NW, image=image2)
    labelimg = Label(image=image2)
    labelimg.image = image2

    #heading
    canv.create_text(500, 150, text="Books", fill="black", font=('Roman 70 bold'))
    canv.pack()
    canv.create_text(750, 300, text="Please select an option:", fill="black", font=('Helvetica 20 bold'))
    canv.pack()

    #Buttons
    btnAcquisition = Button(root,text="1. Book Acquisition",bg='black', fg='black',command=addBooks)
    btnAcquisition.place(relx=0.6,rely=0.45, relwidth=0.3, relheight=0.1)
    btnAcquisition['font'] = helv30

    btnWithdraw = Button(root,text="2. Book Withdrawal",bg='black', fg='black',command=delete)
    btnWithdraw.place(relx=0.6,rely=0.65, relwidth=0.3, relheight=0.1)
    btnWithdraw['font'] = helv30

    btnback = Button(root,text="Back to Main Menu", highlightbackground='LightBlue3',command=MainPg)
    btnback.place(relx=0.10,rely=0.82, relwidth=0.8, relheight=0.08)
    btnback['font'] = helvbold
    

### LOANS MAIN PAGE
def LoansMain():
    global btnBorrowing,btnReturn,canv
    
    bookTable = "Book"
    allreservations = []

    # destroy
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    canv.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    btn6.destroy()
    
    #photo
    canv = Canvas(root, width=1000, height=1000, bg='white')
    canv.grid(row=0, column=0)
    resized_image2=Image.open("book-borrow-clipart.png").resize((450,450), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized_image2)
    canv.create_image(70, 170, anchor=NW, image=image2)
    labelimg = Label(image=image2)
    labelimg.image = image2

    #heading
    canv.create_text(500, 100, text="Loans", fill="black", font=('Roman 70 bold'))
    canv.pack()
    canv.create_text(750, 300, text="Please select an option:", fill="black", font=('Helvetica 20 bold'))
    canv.pack()

    #Buttons
    btnBorrowing = Button(root,text="1. Book Borrowing",bg='black', fg='black',command=BorrowBook)
    btnBorrowing.place(relx=0.6,rely=0.45, relwidth=0.3, relheight=0.1)
    btnBorrowing['font'] = helv30

    btnReturn = Button(root,text="2. Book Return",bg='black', fg='black',command=returnBook)
    btnReturn.place(relx=0.6,rely=0.65, relwidth=0.3, relheight=0.1)
    btnReturn['font'] = helv30

    btnback = Button(root,text="Back to Main Menu", highlightbackground='LightBlue3',command=MainPg)
    btnback.place(relx=0.10,rely=0.82, relwidth=0.8, relheight=0.08)
    btnback['font'] = helvbold
    
    


### RESERVATION MAIN
def ReservationMain():
    global btnReservation,btnCancellation,canv
    # destroy
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    canv.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    btn6.destroy()

    #photo
    canv = Canvas(root, width=1000, height=1000, bg='white')
    canv.grid(row=0, column=0)
    resized_image2=Image.open("calendar-clip-art.png").resize((400,430), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized_image2)
    canv.create_image(100, 175, anchor=NW, image=image2)
    labelimg = Label(image=image2)
    labelimg.image = image2

    #heading 
    canv.create_text(500, 100, text="Reservations", fill="black", font=('Roman 70 bold'))
    canv.pack()
    canv.create_text(750, 300, text="Please select an option:", fill="black", font=('Helvetica 20 bold'))
    canv.pack()

    #Buttons
    btnReservation = Button(root,text="1. Book Reservation",bg='black', fg='black',command=reserveBook)
    btnReservation.place(relx=0.6,rely=0.45, relwidth=0.3, relheight=0.1)
    btnReservation['font'] = helv23

    btnCancellation = Button(root,text="2. Reservation Cancellation",bg='black', fg='black',command=cancelReservation)
    btnCancellation.place(relx=0.6,rely=0.65, relwidth=0.3, relheight=0.1)
    btnCancellation['font'] = helv23

    btnback = Button(root,text="Back to Main Menu", highlightbackground='LightBlue3',command=MainPg)
    btnback.place(relx=0.10,rely=0.82, relwidth=0.8, relheight=0.08)
    btnback['font'] = helvbold

### FINE MAIN
def FineMain():
    global btnReservation, canv
    # destroy
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    canv.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    btn6.destroy()

    #photo
    canv = Canvas(root, width=1000, height=1000, bg='white')
    canv.grid(row=0, column=0)
    resized_image2=Image.open("fine-clipart.jpeg").resize((400,430), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized_image2)
    canv.create_image(100, 175, anchor=NW, image=image2)
    labelimg = Label(image=image2)
    labelimg.image = image2

    #heading 
    canv.create_text(500, 100, text="Fines", fill="black", font=('Roman 70 bold'))
    canv.pack()
    canv.create_text(750, 300, text="Please select an option:", fill="black", font=('Helvetica 20 bold'))
    canv.pack()

    #Buttons
    btnReservation = Button(root,text="Fine Payment",bg='black', fg='black',command=finePayment)
    btnReservation.place(relx=0.6,rely=0.45, relwidth=0.3, relheight=0.1)
    btnReservation['font'] = helv30

    btnback = Button(root,text="Back to Main Menu", highlightbackground='LightBlue3',command=MainPg)
    btnback.place(relx=0.10,rely=0.82, relwidth=0.8, relheight=0.08)
    btnback['font'] = helvbold

    

### REPORTS MAIN
def ReportsMain():
    global btn3, btn4, btn5, btn6, btn7, canv
    # destroy
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    canv.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    btn6.destroy()
    
    canv = Canvas(root, width=1000, height=1000, bg='white')
    canv.grid(row=0, column=0)

    #heading 
    canv.create_text(500, 100, text="  Reports Generator ", fill="black", font=('Roman 70 bold'))
    canv.pack()

    #Buttons
    btn3 = Button(root,text="Display Books On Loan",fg='black', command=ViewLoaned)
    btn3.place(relx=0.15,rely=0.3, relwidth=0.3,relheight=0.15)

    btn4 = Button(root,text="Display Books Reserved",fg='black', command=ViewReserved)
    btn4.place(relx=0.15,rely=0.50, relwidth=0.3,relheight=0.15)

    btn5 = Button(root,text="Display Outstanding Fines", fg='black', command=ViewFined)
    btn5.place(relx=0.55,rely=0.3, relwidth=0.3,relheight=0.15)

    btn6 = Button(root,text="On Loan To Member",fg='black', command=ViewLoanMember)
    btn6.place(relx=0.55,rely=0.50, relwidth=0.3,relheight=0.15)

    btn7 = Button(root,text="Book Search",fg='black', command=Search)
    btn7.place(relx=0.15,rely=0.70, relwidth=0.7,relheight=0.08)


    btnback = Button(root,text="Back to Main Menu", highlightbackground='LightBlue3',command=MainPg)
    btnback.place(relx=0.10,rely=0.82, relwidth=0.8, relheight=0.08)
    btnback['font'] = helvbold


### MAIN CONTENT PAGE
def MainPg():
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,btn3,btn4,btn5,btn6,canv
    btn1.destroy()
    canv.destroy()
    
    #photos
    canv = Canvas(root, width=1000, height=1000, bg='white')
    canv.grid(row=2, column=3)
    resized_image1=Image.open("People-clipart-9.png").resize((250,230), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(resized_image1)
    canv.create_image(100, 150, anchor=NW, image=image1)
    label1 = Label(image=image1)
    label1.image = image1

    resized_image2=Image.open("Stack-of-Books-Clipart.jpeg").resize((260,210), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized_image2)
    canv.create_image(375, 150, anchor=NW, image=image2)
    label2 = Label(image=image2)
    label2.image = image2

    resized_image3=Image.open("book-borrow-clipart.png").resize((260,180), Image.ANTIALIAS)
    image3 = ImageTk.PhotoImage(resized_image3)
    canv.create_image(650, 170, anchor=NW, image=image3)
    label3 = Label(image=image3)
    label3.image = image3

    resized_image4=Image.open("calendar-clip-art.png").resize((250,190), Image.ANTIALIAS)
    image4 = ImageTk.PhotoImage(resized_image4)
    canv.create_image(100, 450, anchor=NW, image=image4)
    label4 = Label(image=image4)
    label4.image = image4
    
    resized_image5=Image.open("fine-clipart.jpeg").resize((250,190), Image.ANTIALIAS)
    image5 = ImageTk.PhotoImage(resized_image5)
    canv.create_image(390, 450, anchor=NW, image=image5)
    label5 = Label(image=image5)
    label5.image = image5

    resized_image6=Image.open("report-cipart.png").resize((250,190), Image.ANTIALIAS)
    image6 = ImageTk.PhotoImage(resized_image6)
    canv.create_image(650, 450, anchor=NW, image=image6)
    label6 = Label(image=image6)
    label6.image = image6

    #library heading
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.2,rely=0.04,relwidth=0.6,relheight=0.10)

    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="Library", fg='black')
    headingLabel.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.8)
    headingLabel.config(font=helvbold)

    #buttons
    btn1 = Button(root,text="Membership",fg='black',command=MembershipMain)
    btn1.place(relx=0.12,rely=0.45, relwidth=0.2, relheight=0.075)

    btn2 = Button(root,text="Books", fg='black',command=BooksMain)
    btn2.place(relx=0.40,rely=0.45, relwidth=0.2, relheight=0.075)

    btn3 = Button(root,text="Loans", fg='black',command=LoansMain)
    btn3.place(relx=0.67,rely=0.45, relwidth=0.2, relheight=0.075)

    btn4 = Button(root,text="Reservations", fg='black',command=ReservationMain)
    btn4.place(relx=0.12,rely=0.85, relwidth=0.2, relheight=0.075)

    btn5 = Button(root,text="Fines", fg='black',command=FineMain)
    btn5.place(relx=0.40,rely=0.85, relwidth=0.2, relheight=0.075)

    btn6 = Button(root,text="Reports", fg='black',command=ReportsMain)
    btn6.place(relx=0.67,rely=0.85, relwidth=0.2, relheight=0.075)

### MAIN TO ENTER
canv = Canvas(root, width=1000, height=1000, bg='white')
canv.grid(row=2, column=3)

btn1 = Button(root,text="Welcome to ALS!",fg='black',command=MainPg)
btn1.place(relx=0.22,rely=0.22, relwidth=0.5, relheight=0.5)
btn1['font'] = helv30

root.mainloop()

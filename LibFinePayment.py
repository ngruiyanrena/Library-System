from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from tkinter import font

###main
##root = Tk()
##root.title("Library")
##helv30 = font.Font(family='Helvetica', size=30)
##helv23 = font.Font(family='Helvetica', size=23)
##
###photo
##canv = Canvas(root, width=1000, height=1000, bg='white')
##canv.grid(row=0, column=0)
##resized_image2=Image.open("fine-clipart.jpeg").resize((500,550), Image.ANTIALIAS)
##image2 = ImageTk.PhotoImage(resized_image2)
##canv.create_image(100, 175, anchor=NW, image=image2)
##
###heading 
##canv.create_text(500, 100, text="Fines", fill="black", font=('Roman 70 bold'))
##canv.pack()
##
##canv.create_text(750, 300, text="Please select an option:", fill="black", font=('Helvetica 20 bold'))
##canv.pack()
##
##
###FUNCTIONS
##def Back():
##    textentry = Entry(root, width = 20)
##    textentry.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.8)

#FINEPAYMENT
def finePayment():
    global en1, en2, en3, Canvas1, connection, cursor, bookTable, root
    
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
    headingLabel = Label(headingFrame1, text="Fine Payment", bg="white", fg="black", font=('Courier',30))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Frame for form
    LabelFrame1 = Frame(root, bg="RosyBrown1")
    LabelFrame1.place(relx=0.03, rely=0.3, relwidth=1, relheight=0.6)

    lb = Label(LabelFrame1, text="To pay a fine, please enter the required information below: ", bg="RosyBrown1", fg="black")
    lb.place(relx=0, rely=0, relheight=0.08)
    lb.config(font=("Courier", 14))

    # Frame for form
    LabelFrame = Frame(root, bg="RosyBrown3")
    LabelFrame.place(relx=0.1, rely=0.37, relwidth=0.8, relheight=0.4)

    # Membership ID  
    lb1 = Label(LabelFrame, text="Membership ID: ", bg="RosyBrown3", fg="black")
    lb1.place(relx=0.05, rely=0.2, relheight=0.15)
    # Entry label for Membership ID  
    en1 = Entry(LabelFrame)
    en1.place(relx=0.35, rely=0.2, relwidth=0.62, relheight=0.15)

    # Payment Date
    lb2 = Label(LabelFrame, text="Payment Date \n (YYYY-MM-DD): ", bg="RosyBrown3", fg="black")
    lb2.place(relx=0.05, rely=0.4, relheight=0.15)
    # Entry label for Payment Date
    en2 = Entry(LabelFrame)
    en2.place(relx=0.35, rely=0.4, relwidth=0.62, relheight=0.15)

    # Payment Amount 
    lb3 = Label(LabelFrame, text="Payment Amount: ", bg="RosyBrown3", fg="black")
    lb3.place(relx=0.05, rely=0.6, relheight=0.15)
    # Entry label for Payment Amount
    en3 = Entry(LabelFrame)
    en3.place(relx=0.35, rely=0.6, relwidth=0.62, relheight=0.15)
    
    # Submit Button
    SubmitBtn = Button(root, text="Pay Fine", bg="#d1ccc0", fg="black", command=confirmFineDetails)
    SubmitBtn.place(relx=0.17, rely=0.85, relwidth=0.25, relheight=0.09)

    # Quit Button
    QuitBtn = Button(root, text="Back to \n Fines Menu", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.60, rely=0.85, relwidth=0.25, relheight=0.09)
    
    root.mainloop()

#CONFIRMFINEDETAILS
def confirmFineDetails():
    global root
    root = Tk()
    root.title("library")
    root.minsize(width=400, height=400)
    root.geometry("250x200")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="RosyBrown1")
    Canvas1.pack(expand=True, fill=BOTH)

    MemberID = en1.get()
    PaymentDate = en2.get()
    PaymentAmountStr = en3.get()

    try:
        cursor.execute("SELECT * FROM Fine WHERE MemberID = '" + MemberID + "'")
        records = cursor.fetchall()
        ActualFineAmount = records[0][1]
    except:
        messagebox.showinfo("Error", "Invalid Membership ID.")
        root.withdraw()
    
    try: 
        PaymentAmountInt = int(en3.get())
        ActualFineAmount = records[0][1]

        if ActualFineAmount == 0:
            messagebox.showinfo("Error!", "Member has no fine")
            root.withdraw()
            
        elif PaymentAmountInt != ActualFineAmount:
            messagebox.showinfo("Error!", "Incorrect fine payment amount")
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

            lb1 = Label(LabelFrame, text="Member ID: " + MemberID, bg="RosyBrown3", fg="black")
            lb1.place(relx=0.01, rely=0.05)
            lb1.config(font=("Courier", 11))

            lb2 = Label(LabelFrame, text="Payment Amount: " + PaymentAmountStr, bg="RosyBrown3", fg="black")
            lb2.place(relx=0.01, rely=0.2)
            lb2.config(font=("Courier", 11))

            lb3 = Label(LabelFrame, text="Payment Date (YYYY-MM-DD): " + PaymentDate, bg="RosyBrown3", fg="black")
            lb3.place(relx=0.01, rely=0.35)
            lb3.config(font=("Courier", 11))
            
            Confirm = Button(root, text="Confirm Payment", bg="RosyBrown3", fg="black", command=confirmPayment)
            Confirm.place(relx=0.04, rely=0.86, relwidth=0.35, relheight=0.10)

            Back = Button(root, text="Return to \n Payment Function", bg="#f7f1e3", fg="black", command=root.destroy)
            Back.place(relx=0.52, rely=0.86, relwidth=0.45, relheight=0.10)
    except:
        messagebox.showinfo("Error", "Invalid Payment Amount.")
        root.withdraw()
    
    
        
    
    root.mainloop()

#CONFIRMPAYMENT
def confirmPayment():
    MemberID = en1.get()
    PaymentDate = en2.get()
    
    try:
        # Update Fine Amount & DatePaid 
        sql_update_query = """Update Fine SET Amount = 0, DatePaid = %s WHERE MemberID = %s"""
        val = (PaymentDate, MemberID)
        cursor.execute(sql_update_query,val)
        connection.commit()
    
        messagebox.showinfo("Success!", "Payment successfully made")

    except:
        # Checking for invalid payment date input 
        messagebox.showinfo("Error", "Invalid Payment Date. Please key in YYYY-MM-DD format.")
        root.withdraw()
    
    root.mainloop()
    
###Buttons
##btnReservation = Button(root,text="Fine Payment",bg='black', fg='black',command=finePayment)
##btnReservation.place(relx=0.6,rely=0.45, relwidth=0.3, relheight=0.1)
##btnReservation['font'] = helv30
##
##btnBack = Button(root,text="Back to Main Menu",bg='black', fg='black',command=Back)
##btnBack.place(relx=0.4,rely=0.925, relwidth=0.2, relheight=0.05)
##
##root.mainloop()

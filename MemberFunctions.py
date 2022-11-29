from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from tkinter import font


### REGISTER MEMBER (DB)
def MemberRegister():
    memberID = en1.get()
    name = en2.get()
    faculty = en3.get()
    phonenum = en4.get()
    email = en5.get()

        
    insertMember = "insert into "+memberTable+" values ('"+memberID+"','"+name+"','"+faculty+"','"+phonenum+"','"+email+"');"
    insertFine = "insert into "+fineTable+" (MemberID, Amount) values ('"+memberID+"', 0)"

    if memberID!="" and name!="" and faculty !="" and phonenum!="" and email!="":
        try:
            cur.execute(insertMember)
            con.commit()
            cur.execute(insertFine)
            con.commit()
            messagebox.showinfo("Success!","ALS Membership created.")
        except:
            messagebox.showinfo("Error","Member already exist; Missing or Incomplete fields")
    else:
        messagebox.showinfo("Error","Member already exist; Missing or Incomplete fields!!!")
        
    root.destroy()


### MEMBER CREATION WINDOW
def MemberCreation():
    global en1, en2, en3, en4, en5, Canvas1, cur, con, memberTable, fineTable, root
    
    root = Tk()
    root.title("Member Creation")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "-"
    mydatabase="library"

    con = pymysql.connect(host="localhost",user="root",password="pw",database="library")
    cur = con.cursor()

    # Enter Table Names here
    memberTable = "Member" # Member Table
    fineTable = "Fine"

    #create the canvas for info
    Canvas1 = Canvas(root)
    Canvas1.config(bg="LightBlue1")
    Canvas1.pack(expand=True, fill=BOTH)

    #add a heading Frame
    headingFrame1 = Frame(root, bg="LightBlue1", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Create Membership", bg="white", fg="black", font=('Courier',24))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #frame for form
    LabelFrame1 = Frame(root, bg="LightBlue1")
    LabelFrame1.place(relx=0.03, rely=0.3, relwidth=1, relheight=0.6)

    lb = Label(LabelFrame1, text="To create membership, please enter the required information below: ", bg="LightBlue1", fg="black")
    lb.place(relx=0., rely=0, relheight=0.08)
    lb.config(font=("Courier", 14))

    ##Entry labels
    #frame for form
    LabelFrame = Frame(root, bg="LightBlue3")
    LabelFrame.place(relx=0.1, rely=0.37, relwidth=0.8, relheight=0.4)
    
    #Membership ID
    lb1 = Label(LabelFrame, text="Membership ID: ", bg="LightBlue3", fg="black")
    lb1.place(relx=0.05, rely=0.17, relheight=0.1)
    #Entry for Membership ID
    en1 = Entry(LabelFrame)
    en1.place(relx=0.35, rely=0.17, relwidth=0.62, relheight=0.1)

    #Name
    lb2 = Label(LabelFrame, text="Name: ", bg="LightBlue3", fg="black")
    lb2.place(relx=0.05, rely=0.35, relheight=0.1)
    #Entry for Name
    en2 = Entry(LabelFrame)
    en2.place(relx=0.35, rely=0.35, relwidth=0.62, relheight=0.1)

    #Faculty
    lb3 = Label(LabelFrame, text="Faculty: ", bg="LightBlue3", fg="black")
    lb3.place(relx=0.05, rely=0.5, relheight=0.1)
    #entry
    en3 = Entry(LabelFrame)
    en3.place(relx=0.35, rely=0.5, relwidth=0.62, relheight=0.1)
    
    #phone num
    lb4 = Label(LabelFrame, text="Phone number: ", bg="LightBlue3", fg="black")
    lb4.place(relx=0.05, rely=0.65, relheight=0.1)
    #entry
    en4 = Entry(LabelFrame)
    en4.place(relx=0.35, rely=0.65, relwidth=0.62, relheight=0.1)
    
    #email address
    lb5 = Label(LabelFrame, text="Email address: ", bg="LightBlue3", fg="black")
    lb5.place(relx=0.05, rely=0.83, relheight=0.1)
    #entry
    en5 = Entry(LabelFrame)
    en5.place(relx=0.35, rely=0.83, relwidth=0.62, relheight=0.1)


    #Submit Button
    SubmitBtn = Button(root, text="Create member", bg="#d1ccc0", fg="black", command=MemberRegister)
    SubmitBtn.place(relx=0.17, rely=0.85, relwidth=0.25, relheight=0.09)

    #Quit button
    QuitBtn = Button(root, text="Return to Members menu", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.60, rely=0.85, relwidth=0.3, relheight=0.09)

    root.mainloop()









### MEMBER DELETE (DB)
def MemberDelete():
    memberID = en1.get()

    cur.execute("SELECT * FROM Fine WHERE MemberID='"+memberID+"'")
    fineRecords = cur.fetchall()
    cur.execute("SELECT * FROM Book WHERE Reserved_MemberID='"+memberID+"' OR Borrowed_MemberID='"+memberID+"'")
    loansRecords = cur.fetchall()
        
    if len(loansRecords)!=0 or fineRecords[0][1]!=0:
        messagebox.showinfo("Error", "Member has loans, reservations or outstanding fines.")
    else:    
        try:
            cur.execute("DELETE FROM Member WHERE MemberID='"+memberID+"'")
            con.commit()
            messagebox.showinfo("Success", "Member Deleted Successfully")
        except:
            messagebox.showinfo("Error", "Member has loans, reservations or outstanding fines!")
            
    print(memberID)
    en1.delete(0, END)
    root.destroy()


### MEMBER DELETE DETAILS TO CONFIRM
def MemberDetails():

    global Canvas1, root, cur, con
    root = Tk()
    root.title("Member Details")
    root.minsize(width=400, height=400)
    root.geometry("250x200")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="SeaGreen1")
    Canvas1.pack(expand=True, fill=BOTH)

    #connect to DB
    con = pymysql.connect(host="localhost",user="root",password="pw",database="library")
    cur = con.cursor()
    
    #get info from DB
    sql_select_Query = "select * FROM Member"
    cur.execute(sql_select_Query)
    records = cur.fetchall()

    memberID = en1.get()
    name = ""
    faculty = ""
    phonenum = ""
    email = ""
    breaked = False

    for row in records:
        if row[0]==memberID:
            name= row[1]
            faculty= row[2]
            phonenum= row[3]
            email= str(row[4])
            breaked = True
        else:
            continue

    #to display the info
    ID ="Member ID: "
    ID += memberID
    
    NA = "Name: "
    NA += name

    FA = "Faculty: "
    FA += faculty
    
    PN = "Phone Number: "
    PN += phonenum
    
    EA = "Email Address: "
    EA += email
    
    if breaked:
        headingFrame1 = Frame(root, bg="SeaGreen1", bd=5)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

         #add a leabel to heading Frame
        headingLabel = Label(headingFrame1, text="Confirm details", bg="white", fg="black", font=('Courier',15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        #add a label frame to canvas to give a lebl insite it to delete book
        LabelFrame = Frame(root, bg="SeaGreen1")
        LabelFrame.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.4)
        
        lb1 = Label(LabelFrame, text=ID, bg="SeaGreen1", fg="black")
        lb1.place(relx=0.01, rely=0.05)
        lb1.config(font=("Courier", 11))

        lb2 = Label(LabelFrame, text=NA, bg="SeaGreen1", fg="black")
        lb2.place(relx=0.01, rely=0.2)
        lb2.config(font=("Courier", 11))

        lb3 = Label(LabelFrame, text=FA, bg="SeaGreen1", fg="black")
        lb3.place(relx=0.01, rely=0.35)
        lb3.config(font=("Courier", 11))

        lb4 = Label(LabelFrame, text=PN, bg="SeaGreen1", fg="black")
        lb4.place(relx=0.01, rely=0.5)
        lb4.config(font=("Courier", 11))

        lb5 = Label(LabelFrame, text=EA, bg="SeaGreen1", fg="black")
        lb5.place(relx=0.01, rely=0.65)
        lb5.config(font=("Courier", 11))   


        Confirm = Button(root, text="Confirm Deletion", bg="#f7f1e3", fg="black", command=MemberDelete)
        Confirm.place(relx=0.04, rely=0.86, relwidth=0.35, relheight=0.08)

        Back = Button(root, text="Return to Delete Function", bg="#f7f1e3", fg="black", command=root.destroy)
        Back.place(relx=0.52, rely=0.86, relwidth=0.45, relheight=0.08)

    else:
        messagebox.showinfo("Error","Invalid MemberID")
        root.withdraw()

    root.mainloop()




### MEMBER DELETION WINDOW
def MemberDeleteMenu():
    global en1, Canvas1, root

    root = Tk()
    root.title("Member Deletion")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    #create the canvas for info
    Canvas1 = Canvas(root)
    Canvas1.config(bg="LightBlue1")
    Canvas1.pack(expand=True, fill=BOTH)

    #add a heading Frame
    headingFrame1 = Frame(root, bg="LightBlue1", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Delete Membership", bg="white", fg="black", font=('Courier',24))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #frame for form
    LabelFrame1 = Frame(root, bg="LightBlue1")
    LabelFrame1.place(relx=0.03, rely=0.3, relwidth=1, relheight=0.6)

    lb = Label(LabelFrame1, text="To delete membership, please enter membership ID below (case sensitive): ", bg="LightBlue1", fg="black")
    lb.place(relx=0., rely=0, relheight=0.08)
    lb.config(font=("Courier", 14))


    ##Entry labels
    #frame for form
    LabelFrame = Frame(root, bg="LightBlue3")
    LabelFrame.place(relx=0.1, rely=0.37, relwidth=0.8, relheight=0.4)
    
    #Membership ID
    lb1 = Label(LabelFrame, text="Membership ID: ", bg="LightBlue3", fg="black")
    lb1.place(relx=0.1, rely=0.3)
    lb1.config(font=("Courier", 15))
    #Entry for Membership ID
    en1 = Entry(LabelFrame)
    en1.place(relx=0.1, rely=0.45, relwidth=0.62)


    #Submit Button
    SubmitBtn = Button(root, text="Delete member", bg="#d1ccc0", fg="black", command=MemberDetails)
    SubmitBtn.place(relx=0.17, rely=0.85, relwidth=0.25, relheight=0.09)

    #Quit button
    QuitBtn = Button(root, text="Return to Members menu", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.60, rely=0.85, relwidth=0.3, relheight=0.09)

    root.mainloop()








### MEMBER UPDATE (DB)
def MemberUpdate():
    memberID = en1.get()
    name = en2.get()
    faculty = en3.get()
    phonenum = en4.get()
    email = en5.get()
    
    #connect to DB
    con = pymysql.connect(host="localhost",user="root",password="pw",database="library")
    cur = con.cursor()
        
    updateMember = "UPDATE Member SET Name='"+name+"',Faculty='"+faculty+"',PhoneNumber='"+phonenum
    updateMember = updateMember+"', Email='"+email+"' WHERE MemberID='"+memberID+"'"
    
    if name!="" and faculty !="" and phonenum!="" and email!="":
        try:
            cur.execute(updateMember)
            con.commit()
            messagebox.showinfo("Success!","ALS Membership updated.")
            en1.delete(0, END)
            en2.delete(0, END)
            en3.delete(0, END)
            en4.delete(0, END)
            en5.delete(0, END)
        except:
            messagebox.showinfo("Error","Missing or Incomplete fields")
    else:
        messagebox.showinfo("Error","Missing or Incomplete fields!")
        
    root.destroy()

def MemberUpdateCfm():
    global Canvas1, root 
    root = Tk()
    root.title("Member Details")
    root.minsize(width=400, height=400)
    root.geometry("250x200")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="SeaGreen1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="SeaGreen1", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="Confirm details", bg="white", fg="black", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas 
    LabelFrame = Frame(root, bg="SeaGreen1")
    LabelFrame.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.4)

    #to display the info
    ID ="Member ID: "
    ID += en1.get()
    
    NA = "Name: "
    NA += en2.get()

    FA = "Faculty: "
    FA += en3.get()
    
    PN = "Phone Number: "
    PN += en4.get()
    
    EA = "Email Address: "
    EA += en5.get()
    
    lb1 = Label(LabelFrame, text=ID, bg="SeaGreen1", fg="black")
    lb1.place(relx=0.01, rely=0.05)
    lb1.config(font=("Courier", 11))

    lb2 = Label(LabelFrame, text=NA, bg="SeaGreen1", fg="black")
    lb2.place(relx=0.01, rely=0.2)
    lb2.config(font=("Courier", 11))

    lb3 = Label(LabelFrame, text=FA, bg="SeaGreen1", fg="black")
    lb3.place(relx=0.01, rely=0.35)
    lb3.config(font=("Courier", 11))

    lb4 = Label(LabelFrame, text=PN, bg="SeaGreen1", fg="black")
    lb4.place(relx=0.01, rely=0.5)
    lb4.config(font=("Courier", 11))

    lb5 = Label(LabelFrame, text=EA, bg="SeaGreen1", fg="black")
    lb5.place(relx=0.01, rely=0.65)
    lb5.config(font=("Courier", 11))   


    Confirm = Button(root, text="Confirm Update", bg="#f7f1e3", fg="black", command=MemberUpdate)
    Confirm.place(relx=0.04, rely=0.86, relwidth=0.35, relheight=0.08)

    Back = Button(root, text="Return to Update Function", bg="#f7f1e3", fg="black", command=root.destroy)
    Back.place(relx=0.52, rely=0.86, relwidth=0.45, relheight=0.08)

    root.mainloop()
        


def MemberUpdateEntryPg():
    global en2, en3, en4, en5, Canvas1, root

    #connect to DB
    con = pymysql.connect(host="localhost",user="root",password="pw",database="library")
    cur = con.cursor()

    #get info from DB
    cur.execute("select * FROM Member WHERE MemberID='"+en1.get()+"'")
    records = cur.fetchall()

    if len(records)==0:
        messagebox.showinfo("Error", "Invalid Member ID")
    else:
        root = Tk()
        root.title("Member Update")
        root.minsize(width=400,height=400)
        root.geometry("600x500")

        #create the canvas for info
        Canvas1 = Canvas(root)
        Canvas1.config(bg="LightBlue1")
        Canvas1.pack(expand=True, fill=BOTH)
        
        
        #add a heading Frame
        headingFrame1 = Frame(root, bg="LightBlue1", bd=5)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
        headingLabel = Label(headingFrame1, text="Update Membership", bg="white", fg="black", font=('Courier',24))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        #frame for form
        LabelFrame1 = Frame(root, bg="LightBlue1")
        LabelFrame1.place(relx=0.03, rely=0.3, relwidth=1, relheight=0.6)

        lb = Label(LabelFrame1, text="To update membership, please enter the required information below: ", bg="LightBlue1", fg="black")
        lb.place(relx=0., rely=0, relheight=0.08)
        lb.config(font=("Courier", 14))

        ##Entry labels
        #frame for form
        LabelFrame = Frame(root, bg="LightBlue3")
        LabelFrame.place(relx=0.1, rely=0.37, relwidth=0.8, relheight=0.4)
        
        #Membership ID
        lb1 = Label(LabelFrame, text="Membership ID: ", bg="LightBlue3", fg="black")
        lb1.place(relx=0.05, rely=0.17, relheight=0.1)
        lbid = Label(LabelFrame, text=en1.get(), bg="LightBlue3", fg="black")
        lbid.place(relx=0.35, rely=0.17, relwidth=0.62, relheight=0.1)

        #Name
        lb2 = Label(LabelFrame, text="Name: ", bg="LightBlue3", fg="black")
        lb2.place(relx=0.05, rely=0.35, relheight=0.1)
        #Entry for Name
        en2 = Entry(LabelFrame)
        en2.place(relx=0.35, rely=0.35, relwidth=0.62, relheight=0.1)
        en2.insert(END, records[0][1])

        #Faculty
        lb3 = Label(LabelFrame, text="Faculty: ", bg="LightBlue3", fg="black")
        lb3.place(relx=0.05, rely=0.5, relheight=0.1)
        #entry
        en3 = Entry(LabelFrame)
        en3.place(relx=0.35, rely=0.5, relwidth=0.62, relheight=0.1)
        en3.insert(END, records[0][2])
        
        #phone num
        lb4 = Label(LabelFrame, text="Phone number: ", bg="LightBlue3", fg="black")
        lb4.place(relx=0.05, rely=0.65, relheight=0.1)
        #entry
        en4 = Entry(LabelFrame)
        en4.place(relx=0.35, rely=0.65, relwidth=0.62, relheight=0.1)
        en4.insert(END, records[0][3])
        
        #email address
        lb5 = Label(LabelFrame, text="Email address: ", bg="LightBlue3", fg="black")
        lb5.place(relx=0.05, rely=0.83, relheight=0.1)
        #entry
        en5 = Entry(LabelFrame)
        en5.place(relx=0.35, rely=0.83, relwidth=0.62, relheight=0.1)
        en5.insert(END, records[0][4])


        #Submit Button
        SubmitBtn = Button(root, text="Update member", bg="#d1ccc0", fg="black", command=MemberUpdateCfm)
        SubmitBtn.place(relx=0.17, rely=0.85, relwidth=0.25, relheight=0.09)

        #Quit button
        QuitBtn = Button(root, text="Return to Members menu", bg="#f7f1e3", fg="black", command=root.destroy)
        QuitBtn.place(relx=0.60, rely=0.85, relwidth=0.3, relheight=0.09)

        root.mainloop()



### MEMBER UPDATE WINDOW
def MemberUpdateMenu():
    
    global en1, Canvas1, root
    root = Tk()
    root.title("Member Update")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    #create the canvas for info
    Canvas1 = Canvas(root)
    Canvas1.config(bg="LightBlue1")
    Canvas1.pack(expand=True, fill=BOTH)

    #add a heading Frame
    headingFrame1 = Frame(root, bg="LightBlue1", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Update Membership", bg="white", fg="black", font=('Courier',24))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #frame for form
    LabelFrame1 = Frame(root, bg="LightBlue1")
    LabelFrame1.place(relx=0.03, rely=0.3, relwidth=1, relheight=0.6)

    lb = Label(LabelFrame1, text="To update a member, please enter membership ID (case sensitive): ", bg="LightBlue1", fg="black")
    lb.place(relx=0., rely=0, relheight=0.08)
    lb.config(font=("Courier", 14))


    ##Entry labels
    #frame for form
    LabelFrame = Frame(root, bg="LightBlue3")
    LabelFrame.place(relx=0.1, rely=0.37, relwidth=0.8, relheight=0.4)
    
    #Membership ID
    lb1 = Label(LabelFrame, text="Membership ID: ", bg="LightBlue3", fg="black")
    lb1.place(relx=0.1, rely=0.3)
    lb1.config(font=("Courier", 15))
    #Entry for Membership ID
    en1 = Entry(LabelFrame)
    en1.place(relx=0.1, rely=0.45, relwidth=0.62)


    #Submit Button
    SubmitBtn = Button(root, text="Update member", bg="#d1ccc0", fg="black", command=MemberUpdateEntryPg)
    SubmitBtn.place(relx=0.17, rely=0.85, relwidth=0.25, relheight=0.09)

    #Quit button
    QuitBtn = Button(root, text="Return to Members menu", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.60, rely=0.85, relwidth=0.3, relheight=0.09)

    root.mainloop()





    
    

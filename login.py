from tkinter import *
from tkinter import messagebox as ms
import sqlite3

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('address_book.db') as db:
    c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS`Customer1` (`Customer_id` INT NOT NULL ,`c_name` varchar(255) NOT NULL,`c_phone` varchar(255) NOT NULL,`email_id` varchar(255) NOT NULL,
`password` varchar(255) NOT NULL,PRIMARY KEY (`Customer_id`))""")
db.commit()
db.close()

#main Class
class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.email_id = StringVar()
        self.password = StringVar()
        self.n_email_id = StringVar()
        self.n_password = StringVar()
        self.n_c_name=StringVar()
        self.n_c_phone=StringVar()
        self.n_Customer_id=StringVar()
        self.n_delete_id=StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('address_book.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM Customer1 WHERE email_id = ? and password = ?')
        c.execute(find_user,[(self.n_email_id.get()),(self.n_password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.email_id.get() + '\n Loged In'
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('address_book.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM Customer1 WHERE email_id = ?')
        c.execute(find_user,[(self.email_id.get())])        
        if c.fetchall():
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO Customer1 (c_name,c_phone,email_id,password,Customer_id) VALUES(?,?,?,?,?)'
        c.execute(insert,[(self.n_email_id.get()),(self.n_password.get()),(self.n_c_name.get()),(self.n_c_phone.get()),(self.n_Customer_id.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.email_id.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_email_id.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
    def query(self):
        
        with sqlite3.connect('address_book.db') as db:
            c = db.cursor()
        c.execute("SELECT * ,Customer_id FROM  Customer1")
        records=c.fetchall()
        print(records)

        print_records=" "
        for record in records:
           
            print_records += str(records)+"\n"
        db.commit()
    def delete(self):
        with sqlite3.connect('address_book.db') as db:
            c = db.cursor()

        c.execute("DELETE from Customer1 WHERE Customer_id= "+self.n_delete_id.get())
        db.commit()
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ("times new roman","50","italic"),pady = 100,fg="midnight blue")
        self.head.pack(side=TOP)
        self.logf = Frame(self.master,padx = 0 ,pady = 0,bg="navajowhite",borderwidth=10,relief=SUNKEN)
        
        Label(self.logf,text = 'Username: ',bg="navajowhite",font = ('comic sans ms',20,"italic"),pady=10,padx=10).grid(sticky = W)
        Entry(self.logf,textvariable = self.email_id,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',bg="navajowhite",font = ('comic sans ms',20,"italic"),pady=10,padx=10).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10,bg="PeachPuff4",borderwidth=10,relief=SUNKEN)
        Label(self.crf,text="Name:",font=('comic sans ms',20,"italic"),bg="navajowhite",pady=5,padx=5).grid(sticky=W)
        Entry(self.crf,textvariable = self.n_c_name,bd=5,font=('',15)).grid(row=0,column=1)
        Label(self.crf,text="Phone_no:",font=('comic sans ms',20,"italic"),bg="navajowhite",pady=5,padx=5).grid(sticky=W)
        Entry(self.crf,textvariable = self.n_c_phone,bd=5,font=('',15)).grid(row=1,column=1)
        Label(self.crf,text = 'Username: ',font=('comic sans ms',20,"italic"),pady=5,padx=5,bg="navajowhite").grid(sticky = W)
        Entry(self.crf,textvariable = self.n_email_id,bd = 5,font = ('',15)).grid(row=2,column=1)
        Label(self.crf,text = 'Password: ',font =('comic sans ms',20,"italic"),pady=5,padx=5,bg="navajowhite").grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=3,column=1)
        Label(self.crf,text="Enter number:",font=('comic sans ms',20,"italic"),pady=5,padx=5,bg="navajowhite").grid(sticky=W)
        Entry(self.crf,textvariable = self.n_Customer_id,bd=5,font=('',15)).grid(row=4,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,bg="gray",command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,bg="snow4",command=self.log).grid(row=5,column=1)
        Button(self.crf,text="query",bd=3,font=('',15),padx=5,pady=5,bg="snow4",command=self.query).grid(row=6,column=0)
        Button(self.crf,text="delete record",bd=3,font=('',15),padx=5,pady=5,bg="gray",command=self.delete).grid(row=7,column=0)
        Label(self.crf,text="enter id",font=('comic sans ms',20,"italic"),pady=5,padx=5,bg="navajowhite").grid(sticky=W)
        Entry(self.crf,textvariable=self.n_delete_id,bd=5,font=('',15)).grid(row= 8,column=1)
#create window and application object
root = Tk()
root.title("Login Form")
main(root)
root.mainloop()
 

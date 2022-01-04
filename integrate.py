from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as ms
import sqlite3
root = Tk()
root.title("Account Login")
root.geometry("1000x1000")


def login_page():


    # make database and users (if not exists already) table at programme start up
    with sqlite3.connect('address_book.db') as db:
        c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS`Customer2` (`Customer_id` INT NOT NULL ,`c_name` varchar(255) NOT NULL,`c_phone` varchar(255) NOT NULL,`email_id` varchar(255) NOT NULL,
    `password` varchar(255) NOT NULL)""")
    db.commit()
    db.close()

    # main Class
    class main:
        def __init__(self, master):
            # Window
            self.master = master
            # Some Usefull variables
            self.email_id = StringVar()
            self.password = StringVar()
            self.n_email_id = StringVar()
            self.n_password = StringVar()
            self.n_c_name = StringVar()
            self.n_c_phone = StringVar()
            self.n_Customer_id = StringVar()
            self.n_delete_id = StringVar()
            # Create Widgets
            self.widgets()

        # Login Function
        def login(self):
            # Establish Connection
            with sqlite3.connect('address_book.db') as db:
                c = db.cursor()

            # Find user If there is any take proper action
            find_user = ('SELECT * FROM Customer2 WHERE email_id = ? and password = ?')
            c.execute(find_user, [(self.n_email_id.get()), (self.n_password.get())])
            result = c.fetchall()
            if result:
                self.logf.pack_forget()
                self.head['text'] =to.get() + '\n you are successfully logged in !'
                self.head['pady'] = 150
            else:
                ms.showerror('Oops!', 'Username Not Found.')

        def new_user(self):
            # Establish Connection
            with sqlite3.connect('address_book.db') as db:
                c = db.cursor()

            # Find Existing username if any take proper action
            find_user = ('SELECT * FROM Customer2 WHERE email_id = ?')
            c.execute(find_user, [(self.email_id.get())])
            if c.fetchall():
                ms.showinfo('Success!', 'Account Created!')
                self.log()
            # Create New Account
            c.execute("INSERT INTO Customer2 VALUES(:c_name,:c_ph,:pass,:email,:id)",
                      {
                          'c_name':yo.get(),
                          'c_ph':po.get(),
                          'pass':fr.get(),
                          'email':en.get(),
                          'id':hu.get(),
                         # 'id1':pi.get()
                        
                          
                
                    
                      })

            db.commit()

            # Frame Packing Methords

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
            c.execute("SELECT *  FROM  Customer2")
            records = c.fetchall()
            print(records)

            print_records = " "
            for record in records:
                print_records += str(records) + "\n"
            db.commit()

        def delete(self):
            with sqlite3.connect('address_book.db') as db:
                c = db.cursor()

            c.execute("DELETE from Customer2 WHERE Customer_id= " + self.n_delete_id.get())
            db.commit()

        # Draw Widgets
        def widgets(self):
            global yu
            global to
            global yo
            global pn
            global en
            global fr
            global hu
            global pi
            global po
            #global yu

            
            self.head = Label(self.master, text='LOGIN', font=("arial black", "40"), pady=30,
                              fg="midnight blue")
            self.head.pack(side=TOP)

            self.logf = Frame(self.master, padx=0, pady=0, bg="SteelBlue1", borderwidth=10, relief=RIDGE)
            #self.image1 = Image.open("l1.jpg")
            #self.photo1 = ImageTk.PhotoImage(self.image1)
            self.lbl1 = Label(self.logf, borderwidth=5, relief=RIDGE, padx=200, pady=50).grid(
                padx=150, pady=30)

            Label(self.logf, text='Username:', fg="midnight blue", font=('lucida handwriting', 20, "bold")).grid(
                sticky=W)
            to=Entry(self.logf, textvariable=self.email_id, bd=5, font=('', 14))
            to.grid(row=1, column=0, padx=5)
            Label(self.logf, text='Password: ', fg="midnight blue", font=('lucida handwriting', 20, "bold")).grid(
                sticky=W, row=3)
            yu=Entry(self.logf, textvariable=self.password, bd=5, font=('', 14), show='*')
            yu.grid(row=3, column=0)
            Button(self.logf, text=' Login ', bd=3, font=('lucida handwriting', 15), padx=5, pady=5,
                   command=self.login).grid()
            Label(self.logf, text='if not login yet: ', bg="SteelBlue1", fg="midnight blue", padx=5, pady=10,
                  font=('lucida handwriting', 15, "bold")).grid(row=8)
            Button(self.logf, text='Create Account', bd=3, font=('lucida handwriting', 15,), padx=5, pady=5,
                   command=self.cr).grid()
            self.logf.pack(side=TOP)

            self.crf = Frame(self.master, padx=10, pady=10, bg="SteelBlue1", borderwidth=10, relief=SUNKEN)
            Label(self.crf, text="Name:", font=('lucida handwriting', 20, "bold"), pady=5, padx=5, fg="midnight blue",
                  bg="SteelBlue1").grid(
                sticky=W)
            yo=Entry(self.crf, textvariable=self.n_c_name, bd=5, font=('', 15))
            yo.grid(row=0, column=1)
            Label(self.crf, text="Phone_no:", font=('lucida handwriting', 20, "bold"), pady=5, padx=5,
                  fg="midnight blue", bg="SteelBlue1").grid(
                sticky=W)
            po=Entry(self.crf, textvariable=self.n_c_phone, bd=5, font=('', 15))
            po.grid(row=1, column=1)
            Label(self.crf, text='Username: ', font=('lucida handwriting', 20, "bold"), pady=5, padx=5,
                  fg="midnight blue", bg="SteelBlue1").grid(
                sticky=W)
            en=Entry(self.crf, textvariable=self.n_email_id, bd=5, font=('', 15))
            en.grid(row=2, column=1)
            Label(self.crf, text='Password: ', font=('lucida handwriting', 20, "bold"), pady=5, padx=5,
                  fg="midnight blue", bg="SteelBlue1").grid(
                sticky=W)
            fr=Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*')
            fr.grid(row=3, column=1)
            Label(self.crf, text="Enter number:", font=('lucida handwriting', 20, "bold"), pady=5, padx=5,
                  fg="midnight blue", bg="SteelBlue1").grid(sticky=W)
            hu=Entry(self.crf, textvariable=self.n_Customer_id, bd=5, font=('', 15))
            hu.grid(row=4, column=1)
            Button(self.crf, text='Create Account', bd=3, font=('lucida handwriting', 20), padx=5, pady=5,
                   command=self.new_user,
                   bg="gray").grid()
            Button(self.crf, text='Go to Login', bd=3, font=('lucida handwriting', 20), padx=5, pady=5,
                   command=self.log, bg="snow4").grid(
                row=5, column=1)
            Button(self.crf, text="query", bd=3, font=('lucida handwriting', 20), padx=5, pady=5, command=self.query,
                   bg="snow4").grid(row=7,
                                    column=1)
            Button(self.crf, text="delete record", bd=3, font=('lucida handwriting', 20), padx=5, pady=5,
                   command=self.delete,
                   bg="gray").grid(row=7, column=0)
            Label(self.crf, text="enter id", font=('lucida handwriting', 20, "bold"), pady=5, padx=5,
                  fg="midnight blue", bg="SteelBlue1").grid(
                sticky=W)
            pi=Entry(self.crf, textvariable=self.n_delete_id, bd=5, font=('', 15))
            pi.grid(row=8, column=1)

    # create window and application object
    root = Tk()
    root.title("Login Form")
    main(root)
    root.mainloop()


photo = PhotoImage(file="mo2.PNG")

lab = Label(image=photo)
lab.pack()
root.config(bg="white")

name = Label(root, text="Movies Galore", font=("ROG Fonts", 40, "bold"),bg="white")
name.pack()
quote = Label(root, text="“Go ahead, make your day.”", font=("Georgia", 20, "bold", "italic"),bg="white")
quote.pack(pady=(10, 80))

# create Login Button
Button(text="Login", height="5", width="50",font=("Georgia", 10, "normal"),bg="grey",relief=SUNKEN,command=login_page).pack(pady=(20, 50))



root.mainloop()

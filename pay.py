from tkinter import*
from tkinter import messagebox as ms
import sqlite3

conn=sqlite3.connect('address_book.db')
            
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS`Paymentpay`

(`payment_id` INT(10) ,
`mode_of_payment` varchar(255),
`amount_payable` varchar(255) ,
'account_no' varchar(20),
PRIMARY KEY (`payment_id`))""")


class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        self.account_no1=StringVar()
        self.amount=StringVar()
        self.widgets()
   
    def submit(self):
        conn=sqlite3.connect('address_book.db')    
        c = conn.cursor()
        c.execute("INSERT INTO Paymentpay VALUES(:pay_id,:mop,:accountno1,:amount)",
            
                  {
                      'pay_id':ifsc.get(),
                      'mop':cv.get(),
                      'accountno1':accountno1.get(),
                      'amount':amount.get()
                     
                  })
        conn.commit()
        conn.close()
        accountno1.delete(0,END)
        ifsc.delete(0,END)
        cv.delete(0,END)
        exp.delete(0,END)
        amount.delete(0,END)
        
        
        
    def query(self):
        conn=sqlite3.connect('address_book.db')    
        c = conn.cursor()
        c.execute("SELECT amount_payable,account_no FROM Paymentpay")
        records=c.fetchall()
        print(records)
        print_records=''
        for record in records:
            print_records=str(record)+"\n"
        query_label=Label(self.crf,text=("CONGRATS FOR BOOKING! YOUR INFO IS:",print_records,"THANK YOU!!!"),font=("times new roman","30","italic"))
        query_label.grid(row=6,column=0)

          
        conn.commit()
        conn.close()
        

       
        
    def click(self):
        global accountno1
        global amount
        global ifsc
        global cv
        global exp
        
        self.crf=Tk()
        self.crf.title("Pay it.. and enjoy your day!")
        self.crf.geometry("700x600")
        accountlabel=Label(self.crf,text = 'Account no.',font = ("times new roman","20","italic"),pady = 30,fg="midnight blue").grid(row=0,column=0)
        accountno1=Entry(self.crf,bd=5,font=('',10))
        accountno1.grid(row=0,column=2)
        ifsclabel=Label(self.crf,text = 'IFSC CODE',font = ("times new roman","20","italic"),pady = 30,fg="midnight blue").grid(row=1,column=0)
        ifsc=Entry(self.crf,bd=5,font=('',10))
        ifsc.grid(row=1,column=2)
        cvlabel=Label(self.crf,text = 'C.V.C',font = ("times new roman","20","italic"),pady = 30,fg="midnight blue").grid(row=2,column=0)
        cv=Entry(self.crf,bd=5,font=('',10))
        cv.grid(row=2,column=2)
        explabel=Label(self.crf,text = 'Expiry',font = ("times new roman","20","italic"),pady = 30,fg="midnight blue").grid(row=3,column=0)
        exp=Entry(self.crf,bd=5,font=('',10)).grid(row=3,column=2)
        amtlabel=Label(self.crf,text = 'Enter  amount',font = ("times new roman","20","italic"),pady = 30,fg="midnight blue").grid(row=4,column=0)
        amount=Entry(self.crf,bd=5,font=('',10))
        amount.grid(row=4,column=2)
        Button(self.crf,text = 'SUBMIT',bd = 3 ,font = ('',10),padx=5,pady=5,bg="snow4",command=self.submit).grid(row=5,column=0)
        Button(self.crf,text = 'DISPLAY',bd = 3 ,font = ('',10),padx=5,pady=5,bg="snow4",command=self.query).grid(row=5,column=1)
        



    def widgets(self):
        Label(self.master,text = 'PAYMENT',font = ("times new roman","70","italic"),pady = 50,fg="midnight blue").grid(row=0,column=5)
        #Entry(root,bd=5,font=('',15)).grid(row=1,column=1)
        Label(self.master,text = 'Price',font = ("times new roman","40","italic"),pady = 50,fg="midnight blue").grid(row=1,column=4)
        Label(self.master,text = '--:   120/- per  person ',font = ("times new roman","40","italic"),pady = 50,fg="midnight blue").grid(row=1,column=5)
        #Entry(root,bd=5,font=('',15)).grid(row=3,column=1)
        Label(self.master,text = 'MODE OF PAYMENT',font = ("times new roman","30","italic"),pady = 50,fg="midnight blue").grid(row=2,column=4)
        
        Label(self.master,text = '--:',font = ("times new roman","20","italic"),pady = 50,fg="midnight blue").grid(row=2,column=5)
        Button(root,text = 'CARD',bd = 3 ,font = ('',15),padx=5,pady=5,bg="snow4",command=self.click).grid(row=2,column=6)

        #self.logf = Frame(self.master,padx = 0 ,pady = 0,bg="navajowhite",borderwidth=5,relief=SUNKEN)
        
        #email_id_label=Label(root,text="UserName",bg="orange"
conn.commit()
conn.close()
        
root = Tk()
#root.title("Login Form")
main(root)
root.mainloop()
 

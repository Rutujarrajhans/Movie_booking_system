
from tkinter import*
from tkinter import messagebox as ms
import sqlite3
from PIL import Image , ImageTk
#import enail



conn=sqlite3.connect('address_book.db')

c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS`Paymentpayfast`

(`payment_id` INT(10) ,
`mode_of_payment` varchar(255),
`amount_payable` varchar(255) ,
'account_no' varchar(20),
'info' varchar(10),
PRIMARY KEY (`payment_id`))""")
class mainn:
    def __init__(self,master):
        

        
       # Window
        self.click()
        #self.root1=root1
        self.master=master
        nno_of_seats=IntVar()
    
    def widgets(self):
        global nno_of_seats
        global amount
        global accountno1
       # global amount
        global ifsc
        global cv
        global exp
        self.crf=Tk()
        self.crf.title("Pay it.. and enjoy your day!")
        self.crf.geometry("700x600")
        self.crf.configure(bg='#49A')
        #global nno_of_seats
        #global amount
        accountlabel=Label(self.crf,text = 'Account no.',font = ("lucida handwriting","20","bold"),pady = 30,fg="midnight blue").grid(row=0,column=0)
        accountno1=Entry(self.crf,bd=5,font=('',10))
        accountno1.grid(row=0,column=2)
        ifsclabel=Label(self.crf,text = 'IFSC CODE',font = ("lucida handwriting","20","bold"),pady = 30,fg="midnight blue").grid(row=1,column=0)
        ifsc=Entry(self.crf,bd=5,font=('',10))
        ifsc.grid(row=1,column=2)
        cvlabel=Label(self.crf,text = 'C.V.C',font = ("lucida handwriting","20","bold"),pady = 30,fg="midnight blue").grid(row=2,column=0)
        cv=Entry(self.crf,bd=5,font=('',10))
        cv.grid(row=2,column=2)
        explabel=Label(self.crf,text = 'Expiry',font = ("lucida handwriting","20","bold"),pady = 30,fg="midnight blue").grid(row=3,column=0)
        exp=Entry(self.crf,bd=5,font=('',10))
        exp.grid(row=3,column=2)
        amtlabel=Label(self.crf,text = 'Enter  amount',font = ("lucida handwriting","20","bold"),pady = 30,fg="midnight blue").grid(row=4,column=0)
        amount=Entry(self.crf,bd=5,font=('',10))
        amount.grid(row=4,column=2)
        eq=Label(self.crf,text = 'Enter no of seats',font = ("lucida handwriting","20","bold"),pady = 30,fg="midnight blue").grid(row=5,column=0)
        nno_of_seats=Entry(self.crf,bd=5,font=('',10))
        nno_of_seats.grid(row=5,column=2)    
        Button(self.crf,text = 'SUBMIT',bd = 3 ,font = ('lucida handwriting',10,"bold"),padx=5,pady=5,bg="snow4",command=self.submit,borderwidth=10).grid(row=6,column=0)
        Button(self.crf,text = 'DISPLAY',bd = 3 ,font = ('lucida handwriting',10,"bold"),padx=5,pady=5,bg="snow4",command=self.query,borderwidth=10).grid(row=6,column=1)  
        Button(self.crf,text = 'info ',bd = 3 ,font = ('lucida handwriting',10,"bold"),padx=5,pady=5,bg="snow4",command=self.info,borderwidth=10).grid(row=6,column=2)
        Button(self.crf,text = 'TO mail yourself ,click here!!',bd = 3 ,font = ('lucida handwriting',10,"bold"),padx=5,pady=5,bg="snow4",command=self.next,borderwidth=10).grid(row=6,column=3)
    
    def submit(self):
        conn=sqlite3.connect('address_book.db')
        c = conn.cursor()
        c.execute("INSERT INTO Paymentpayfast VALUES(:pay_id,:mop,:accountno1,:amount,:nno_of_seats)",

                  {
                      'pay_id':ifsc.get(),
                      'mop':cv.get(),
                      'accountno1':accountno1.get(),
                      'amount':amount.get(),
                      'nno_of_seats':nno_of_seats.get()


                  })
        conn.commit()
        conn.close()
        accountno1.delete(0,END)
        ifsc.delete(0,END)
        cv.delete(0,END)
        exp.delete(0,END)
        amount.delete(0,END)
        nno_of_seats.delete(0,END)
    def info(self):
         
         i=int(nno_of_seats.get())
        
         for x in range(1,(i+1)):
            
             price=int('120')* x
         print ("you have to pay",price)
         x=int(price)
         y=int(amount.get())
         remain=int((x)-(y))
         print(remain)
         if(remain==0):
             query_label2=Label(self.crf,text=("u  paid",price),font=("lucida handwriting","20","bold"),fg="midnight blue")
             query_label2.grid(row=11,column=0)
         else:
             query_label1=Label(self.crf,text=("u have 2 pay",remain,"more"),font=("lucida handwriting","20","bold"),fg="midnight blue")
             query_label1.grid(row=10,column=0)
        
        

    def query(self):
        #global n_no_of_seats
        #from h import MainApp.make_seats
        #hh.MainApp.make_seats.n_no_of_seats.get()
    
        
        #amt=amount.get()
        #if amt != query_label1:
          #  print("sorry")
            
         
        #else:
        conn=sqlite3.connect('address_book.db')
        c = conn.cursor()
        c.execute("SELECT amount_payable,account_no,info FROM Paymentpayfast")
        records=c.fetchall()
        print(records)
        print_records=''
        for record in records:
                
            print_records=str(record)+"\n"
        query_label=Label(self.crf,text=("congrats!your booking is successfully completed,details:",print_records,"THANK YOU!!!"),font=("lucida handwriting","20","bold"),fg="midnight blue")
        query_label.grid(row=8,column=0)
        conn.commit()
        conn.close()
        

        #conn.commit()
        #conn.close()
    def next(self):
        self.crf.destroy()
        import enail



    def click(self):

        Label(root1, text='PAYMENT', font=("lucida handwriting", "40", "bold"), borderwidth="10",
              bg="midnight blue", pady=0, padx=10, fg="LightBlue1", relief=SUNKEN).grid(padx=600, pady=10)
        # Entry(root,bd=5,font=('',15)).grid(row=1,column=1)
        self.image2 = Image.open("card.jpg")
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.lbl3 = Label(root1, image=self.photo2, borderwidth=5, relief=RIDGE)
        self.lbl3.grid(row=1,column=0)


        #Label(self.master,text = 'PAYMENT',font = ("lucida handwriting","40","bold"),borderwidth="10",bg="midnight blue",pady = 30,padx=30,fg="LightBlue1",relief=SUNKEN).grid(padx=600,pady=50)
        #Entry(root,bd=5,font=('',15)).grid(row=1,column=1)
        Label(root1,text = 'price for each ticket is 120 /-',font = ("lucida handwriting","40","bold"),pady = 20,fg="midnight blue").grid(padx=50)
        #Label(self.master,text = '120/- per  person ',font = ("times new roman","40","italic"),pady = 50,fg="midnight blue").grid(row=1,column=5)
        #Entry(root,bd=5,font=('',15)).grid(row=3,column=1)
        Label(root1,text = 'mode of payment : card is the only option',font = ("lucida handwriting","30","bold"),fg="midnight blue").grid(padx=50)


        Button(root1,text = 'click here for payment details',bd = 3 ,font = ('comic sans ms',15),padx=5,pady=5,bg="grey",fg="black",borderwidth=10,command=self.widgets).grid(pady=50)
        
        #self.logf = Frame(self.master,padx = 0 ,pady = 0,bg="navajowhite",borderwidth=5,relief=SUNKEN)

        #email_id_label=Label(root,text="UserName",bg="orange"


conn.commit()
conn.close()
def main():
    global root1
    root1=Tk()
    root1.title("Payment")
    root1.configure(bg='#49A')
    mainn(root1)
    root1.mainloop()
if __name__ == '__main__':
    main()
    
    
   


       

import tkinter as tk
from tkinter import ttk
from tkinter import *
import rohit
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import sqlite3


with sqlite3.connect('address_book.db') as db:
    c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS `Seats3` (
   `no_of_seats` INT(255) 
   )"""
          )
db.commit()
db.close()

root=Tk()
image1 = Image.open("yo.jpg")
photo1 = ImageTk.PhotoImage(image1)
lbl1 = Label(root, image=photo1, borderwidth=5, relief=RIDGE, pady=10).grid(row=6, column=0)


image2 = Image.open("to.jpg")
photo2 = ImageTk.PhotoImage(image2)
lbl2 = Label(root, image=photo2, borderwidth=5, relief=RIDGE, pady=10).grid(row=6, column=1)


class MainApp(ttk.Frame):

    def __init__(self):
        
        no_of_seats=tk.StringVar()
      
       # self.parent=parent
        self.gen_layout()
        ttk.Frame.__init__(self)
        

       # self.n_no_of_seats = StringVar()

        #ttk.Frame.__init__(self, parent)
       # self.parent = parent
        #self.gen_layout()

    def gen_layout(self):
        self.make_seats()

    def click(self):
        #
        b1.config(state=DISABLED)

    def click1(self):
        # global b1
        b2.config(state=DISABLED)

    def click2(self):
        # global b1
        b3.config(state=DISABLED)

    def click3(self):
        # global b1
        b4.config(state=DISABLED)

    def click4(self):
        # global b1
        b5.config(state=DISABLED)

    def click5(self):
        # global b1
        b6.config(state=DISABLED)

    def click6(self):
        # global b1
        b7.config(state=DISABLED)

    def click7(self):
        # global b1
        b8.config(state=DISABLED)

    def click8(self):
        # global b1
        b9.config(state=DISABLED)

    def click9(self):
        # global b1
        b10.config(state=DISABLED)

    def click10(self):
        # global b1
        b11.config(state=DISABLED)
    def click11(self):
        # global b1
        b14.config(state=DISABLED)
    def click12(self):
        # global b1
        b15.config(state=DISABLED)
        
    def next(self):
        root.destroy()
        rohit.main()
        
      

    def submit(self):
        with sqlite3.connect('address_book.db') as db:
            c = db.cursor()
        c.execute("INSERT INTO Seats3 VALUES(:no_of_seat)",
                  {
                      'no_of_seat' : no_of_seat.get()
                      })

       # print(self.n_no_of_seats,"booked")

        db.commit()
        db.close()

    def query(self):
        with sqlite3.connect('address_book.db') as db:
            c = db.cursor()
        c.execute("SELECT no_of_seats FROM  Seats3")
        records = c.fetchall()
        print(records, " ", "seats booked")
        # print_records=" "
        # for record in records:

        # print_records += str(records)+ "\n"
        db.commit()

    def make_seats(self):
        global b1
        global b2
        global b3
        global b4
        global b5
        global b6
        global b7
        global b8
        global b9
        global b10
        global b11
        global b14
        global b15
        global no_of_seat
      
        global seatid
        #global n_no_of_seats
      

        self.f1 = Frame(root, borderwidth=6, relief=RAISED, bg="red4")
        self.f1.grid(row=4, column=0, padx=10, pady=10)

        self.lbl2 = Label(self.f1, text="     click here for the seat you want to book    ", bg="red4",
                          font=("lucida handwriting", 10, "bold"), padx=10, pady=10, fg="black")
        self.lbl2.grid(row=0, column=0, sticky=W)

        b1 = Button(self.f1, text='  1  ', bd=3, font=('', 15), padx=5, pady=5, bg="tomato3", command=self.click)
        b1.grid(row=0, column=2, padx=10, pady=10)
        b2 = Button(self.f1, text='  2  ', bd=3, font=('', 15), padx=5, pady=5, bg="tomato3", command=self.click1)
        b2.grid(row=0, column=3, padx=10, pady=1)
        b3 = Button(self.f1, text='  3  ', bd=3, font=('', 15), bg="tomato3", padx=5, pady=5, command=self.click2)
        b3.grid(row=0, column=4, padx=10, pady=10)
        b4 = Button(self.f1, text='  4  ', bd=3, font=('', 15), padx=5, pady=5, bg="tomato3", command=self.click3)
        b4.grid(row=0, column=5, padx=10, pady=10)

        b5 = Button(self.f1, text='  5  ', bd=3, font=('', 15), padx=5, pady=5, bg="tomato3", command=self.click4)
        b5.grid(row=1, column=2, padx=10, pady=10)
        b6 = Button(self.f1, text='  6  ', bd=3, font=('', 15), bg="tomato3", padx=5, pady=5, command=self.click5)
        b6.grid(row=1, column=3, padx=10, pady=10)
        b7 = Button(self.f1, text='  7  ', bd=3, font=('', 15), bg="tomato3", padx=5, pady=5, command=self.click6)
        b7.grid(row=1, column=4, padx=10, pady=10)
        b8 = Button(self.f1, text='  8  ', bd=3, font=('', 15), bg="tomato3", padx=5, pady=5, command=self.click7)
        b8.grid(row=1, column=5, padx=10, pady=10)

        b9 = Button(self.f1, text='  9  ', bd=3, font=('', 15), bg="tomato3", padx=5, pady=5, command=self.click8)
        b9.grid(row=2, column=2, padx=10, pady=10)
        b10 = Button(self.f1, text=' 10 ', bd=3, font=('', 15), bg="tomato3", padx=5, pady=5, command=self.click9)
        b10.grid(row=2, column=3, padx=10, pady=10)
        b11 = Button(self.f1, text=' 11 ', bd=3, font=('', 15), bg="tomato3", padx=5, pady=5, command=self.click10)
        b11.grid(row=2, column=4, padx=10, pady=10)
        b12 = Button(self.f1, text=' 12 ', bd=3, font=('', 15), bg="tomato3", padx=5, pady=5,state=DISABLED)
        b12.grid(row=2, column=5, padx=10, pady=10)

        b13 = Button(self.f1, text=' 13 ', bd=3, bg="tomato3", font=('', 15), padx=5, pady=5, state=DISABLED)
        b13.grid(row=3, column=2, padx=10, pady=10)
        b14 = Button(self.f1, text=' 14 ', bd=3, bg="tomato3", font=('', 15), padx=5, pady=5, command=self.click11)
        b14.grid(row=3, column=3, padx=10, pady=10)
        b15 = Button(self.f1, text=' 15 ', bd=3, font=('', 15), bg="tomato3", padx=5, pady=5, command=self.click12)
        b15.grid(row=3, column=4, padx=10, pady=10)
        b16 = Button(self.f1, text=' 16 ', bd=3, font=('', 15), padx=5, pady=5, bg="tomato3", state=DISABLED)
        b16.grid(row=3, column=5, padx=10, pady=10)

        Label(self.f1, text='       Enter no of seats    :   ', font=('lucida handwriting', 15, "bold"),
              bg="red4").grid(row=1, column=0, sticky=W)
        no_of_seat = tk.Entry(self.f1, bd=10, font=('', 10))
        no_of_seat.grid(row=1, column=1)
        Button(self.f1, text='CLICK', bd=3, font=('lucida handwriting', 15), padx=5, pady=5, command=self.submit).grid(
            sticky=W, padx=10, row=3)
        Button(self.f1, text="query", bd=3, font=('lucida handwriting', 15), padx=5, pady=5, bg="grey",
               command=self.query).grid(sticky=W, row=3, column=1)
        Button(self.f1, text="NEXT", bd=3, font=('lucida handwriting', 15), padx=5, pady=5, bg="grey",command=self.next).grid(sticky=W, row=4, column=1)

      


def main():
    global root
    root=tk.Tk()
    MainApp()
    root.mainloop()
    
if __name__ == '__main__':
    
    main()
    
    


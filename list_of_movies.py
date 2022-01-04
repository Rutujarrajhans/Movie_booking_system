from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as msg
import sqlite3
import integrate

conn=sqlite3.connect('address_book.db')

c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS`Movie`

('movie_name' varchar(24))""")

root = Tk()
root.title("Movies")
root.config(bg="light blue")
def book1():
    a = msg.showinfo("Movie", "Movie 'MY SPY' is selected");


def book2():
    a = msg.showinfo("Movie", "Movie 'TROLLS WORLD TOUR' is selected");


def book3():
    a = msg.showinfo("Movie", "Movie 'BLACK WIDOW' is selected");


def book4():
    a = msg.showinfo("Movie", "Movie 'SCOOB!' is selected");


def book5():
    a = msg.showinfo("Movie", "Movie 'BHOOL BHULAIYAA - 2' is selected");


def book6():
    a = msg.showinfo("Movie", "Movie 'JHUND' is selected");


def book7():
    a = msg.showinfo("Movie", "Movie 'JAGAME TANTRAM' is selected");
def submit():
    
    
    
    conn=sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO Movie VALUES(:movie_n)",

                  {
                      'movie_n':e1.get()

                  })
    print("movie is",e1.get())

    conn.commit()
    conn.close()
    e1.delete(0,END)
  #  print(e1.get())

def next2():
    import the

def win1():
    w1 = Tk()
    w1.geometry("1000x1000")
    w1.config(bg="light grey")
    Label(w1, text="MY SPY", font=("Mongolian Baiti", 25, "bold"), bg="light grey").pack()
    Label(w1, text="Category  ", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w")
    Label(w1, text="English", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w1, text="Genre", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                   pady=(20, 0))
    Label(w1, text="Action , Drama", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w1, text="SYNOPSIS", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                      pady=(20, 0))
    Label(w1, text="A CIA operative finds his career on the line when his cover"
                   "is blown by a nine-year-old girl during \na surveillance operation."
                   "In exchange for her silence, he agrees to teach the precocious girl\n how"
                   "to become a cool spy.The unlikely partnership will change both their "
                   "lives for the better.", font=("Lucida Sans Unicode", 15, "normal"), bg="light grey").pack(
        anchor="w")
    Label(w1, text="CAST", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w1, text="Dave Bautista\nKristen Schaal\n"
                   "Ken Jeong\nGreg Bryk", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w1, text="CREW", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w1, text="Producer : Dave Bautista\nDirector : Peter Sagal\n"
                   "Writer : Erich Hoeber", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
   


def win2():
    w2 = Tk()
    w2.geometry("1000x1000")
    w2.config(bg="light grey")
    Label(w2, text="TROLLS WORLD TOUR", font=("Mongolian Baiti", 25, "bold"), bg="light grey").pack()
    Label(w2, text="Category  ", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w")
    Label(w2, text="English", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w2, text="Genre", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                   pady=(20, 0))
    Label(w2, text="Drama", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w2, text="SYNOPSIS", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                      pady=(20, 0))
    Label(w2, text="In this sequel, Poppy and Branch discover six other Troll tribes over six different\n"
                   "lands. Each one of them is devoted to a different form of music, including Pop, Funk,\n"
                   "Classical, Techno, Country and Rock. But Queen Barb is determined to destroy all other\n"
                   "kinds of music in favour of Rock. Poppy and Branch set out to unite all\n "
                   "the trolls in the hope of stopping her. But can they do it in time?",
          font=("Lucida Sans Unicode", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w2, text="CAST", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w2, text="Justin Timberlake\nAnna Kendrick", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(
        anchor="w")
    Label(w2, text="CREW", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w2, text="Director : Mike Mitchell", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")


def win3():
    w3 = Tk()
    w3.geometry("1000x1000")
    w3.config(bg="light grey")
    Label(w3, text="BLACK WIDOW", font=("Mongolian Baiti", 25, "bold"), bg="light grey").pack()
    Label(w3, text="Category  ", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w")
    Label(w3, text="English", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w3, text="Genre", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                   pady=(20, 0))
    Label(w3, text="Drama", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w3, text="SYNOPSIS", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                      pady=(20, 0))
    Label(w3, text="Set after the events of Captain America: Civil War, Natasha Romanoff finds herself\n "
                   "returning to her roots and her family before the Avengers, ready to face the past. Together,\n"
                   " they confront the Taskmaster a mercenary recruiting and brainwashing young girls\n"
                   " into becoming assassins.", font=("Lucida Sans Unicode", 15, "normal"), bg="light grey").pack(
        anchor="w")
    Label(w3, text="CAST", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w3, text="Scarlett Johansson\nDaid Harbour"
                   "\nFlorence Pugh", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w3, text="CREW", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w3, text="Producer : Kevin Feige\nDirector : Cate Shortland\n"
                   "Writer : Jac Schaeffer", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")


def win4():
    w4 = Tk()
    w4.geometry("1000x1000")
    w4.config(bg="light grey")
    Label(w4, text="SCOOB!", font=("Mongolian Baiti", 25, "bold"), bg="light grey").pack()
    Label(w4, text="Category  ", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w")
    Label(w4, text="English", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w4, text="Genre", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                   pady=(20, 0))
    Label(w4, text="Animation/Comedy", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w4, text="SYNOPSIS", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                      pady=(20, 0))
    Label(w4, text="With hundreds of cases solved and adventures shared, Scooby and the gang face their biggest,\n"
                   " most challenging mystery ever a plot to unleash the ghost dog Cerberus upon the world. As they\n "
                   "race to stop this global dog-pocalypse, the gang discovers that Scooby has a secret legacy and an\n "
                   "epic destiny greater than anyone could have imagined.",
          font=("Lucida Sans Unicode", 15, "normal"), bg="light grey").pack(anchor="w")

    Label(w4, text="CREW", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w4, text="Producer : Allison Abbate, Pam Coats\nDirector : Tony Cervone",
          font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")


def win5():
    w5 = Tk()
    w5.geometry("1000x1000")
    w5.config(bg="light grey")
    Label(w5, text="BHOOL BHULAIYAA - 2", font=("Mongolian Baiti", 25, "bold"), bg="light grey").pack()
    Label(w5, text="Category  ", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w")
    Label(w5, text="Hindi", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w5, text="Genre", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                   pady=(20, 0))
    Label(w5, text="Horror", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w5, text="SYNOPSIS", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                      pady=(20, 0))
    Label(w5, text="Bhool Bhulaiyaa 2 is a 2020 Indian Hindi language comedy horror film directed by Anees Bazmee\n"
                   " and backed by Web3Point Studios, Cine1 Studios and T-Series. It is a spiritual sequel to\n"
                   " the 2007 film Bhool Bhulaiyaa directed by Priyadarshan",
          font=("Lucida Sans Unicode", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w5, text="CAST", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w5, text="Kartik Aaryan\nKiara  Advani"
                   "\nRajpal Yadav", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w5, text="CREW", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w5, text="Producer :  Anees Bazmee, Krishan Kumar\nDirector : Anees Bazmee\n",
          font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")


def win6():
    w6 = Tk()
    w6.geometry("1000x1000")
    w6.config(bg="light grey")
    Label(w6, text="JHUND", font=("Mongolian Baiti", 25, "bold"), bg="light grey").pack()
    Label(w6, text="Category  ", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w")
    Label(w6, text="Hindi", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w6, text="Genre", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                   pady=(20, 0))
    Label(w6, text="Sports , Drama", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w6, text="SYNOPSIS", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                      pady=(20, 0))
    Label(w6, text="Jhund is an upcoming Indian Hindi-language sports film based on the life of Vijay Barse,\n "
                   "the founder of NGO Slum Soccer.", font=("Lucida Sans Unicode", 15, "normal"), bg="light grey").pack(
        anchor="w")
    Label(w6, text="CAST", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w6, text="Akash Thosar\nRinku  Rajguru"
                   "\nAmitabh Bachchan", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w6, text="CREW", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w6, text="Producer : Nagraj Manjule, Savita Raj Hiremath, Bhushan Kumar\nDirector :  Nagraj Manjule\n"
          , font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")


def win7():
    w7 = Tk()
    w7.geometry("1000x1000")
    w7.config(bg="light grey")
    Label(w7, text="JAGAME THANDHIRAM", font=("Mongolian Baiti", 25, "bold"), bg="light grey").pack()
    Label(w7, text="Category  ", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w")
    Label(w7, text="Tamil", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w7, text="Genre", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                   pady=(20, 0))
    Label(w7, text="Mystery  , Adventure", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w7, text="SYNOPSIS", font=("Comic Sans MS", 20, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                      pady=(20, 0))
    Label(w7, text="Jagame Thandhiram is an upcoming Indian Tamil-language action thriller film written and\n"
                   " directed by Karthik Subbaraj and produced by Y NOT Studios",
          font=("Lucida Sans Unicode", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w7, text="CAST", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w7, text="Dhanush\nSanchana Natarajan"
                   "\nAishwarya Lekshmi", font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
    Label(w7, text="CREW", font=("Comic Sans MS", 15, "bold", "underline"), bg="light grey").pack(anchor="w",
                                                                                                  pady=(20, 0))
    Label(w7, text="Producer :  S. Sashikanth\nDirector : Karthik Subbaraj\n"
         , font=("Comic Sans MS", 15, "normal"), bg="light grey").pack(anchor="w")
 

Label(text="Select your movie ", font=("Comic Sans MS", 20, "bold", "underline"), bg="light blue").grid(column=26)

image1 = Image.open("11.PNG")
image1 = image1.resize((200, 300), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image1)
Label(image=photo1).grid(row=3, column=0)
Button(text="View", font=("comicsans", 15, "normal"), command=win1, bg="light blue").grid(row=7, column=0, pady=10)
Button(text="Book", font=("comicsans", 15, "normal"),command=book1, bg="light blue").grid(row=8, column=0, pady=5)

image2 = Image.open("12.PNG")
image2 = image2.resize((200, 300), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)
Label(image=photo2).grid(row=3, column=6)
Button(text="View", font=("comicsans", 15, "normal"), command=win2, bg="light blue").grid(row=7, column=6, pady=10)
Button(text="Book", font=("comicsans", 15, "normal"),command=book2, bg="light blue").grid(row=8, column=6, pady=5)

image3 = Image.open("13.PNG")
photo3 = ImageTk.PhotoImage(image3)
Label(image=photo3).grid(row=3, column=16)
Button(text="View", font=("comicsans", 15, "normal"), command=win3, bg="light blue").grid(row=7, column=16, pady=10)
Button(text="Book", font=("comicsans", 15, "normal"),command=book3, bg="light blue").grid(row=8, column=16, pady=5)

image5 = Image.open("18.PNG")
photo5 = ImageTk.PhotoImage(image5)
Label(image=photo5).grid(row=3, column=26)
Button(text="View", font=("comicsans", 15, "normal"), command=win5, bg="light blue").grid(row=7, column=26, pady=10)
Button(text="Book", font=("comicsans", 15, "normal"), command =book4,bg="light blue").grid(row=8, column=26, pady=5)

image6 = Image.open("19.PNG")
photo6 = ImageTk.PhotoImage(image6)
Label(image=photo6).grid(row=3, column=36)
Button(text="View", font=("comicsans", 15, "normal"), command=win7, bg="light blue").grid(row=7, column=36, pady=10)
Button(text="Book", font=("comicsans", 15, "normal"),command=book5, bg="light blue").grid(row=8, column=36, pady=5)
Label(text = 'Movie name',font = ("Comic Sans MS","20","bold"),pady = 30,fg="light blue").grid(row=9,column=36)

image4 = Image.open("14.PNG")
photo4 = ImageTk.PhotoImage(image4)
Label(image=photo4).grid(row=3, column=46)
Button(text="View", font=("comicsans", 15, "normal"), command=win4, bg="light blue").grid(row=7, column=46, pady=10)
Button(text="Book", font=("comicsans", 15, "normal"), command=book6,bg="light blue").grid(row=8, column=46, pady=5)
#Label(text = 'Movie name',font = ("lucida handwriting","20","bold"),pady = 30,fg="midnight blue").grid(row=9,column=46)
e1=Entry(bd=5,font=('',10))
e1.grid(row=9,column=46)


image10 = Image.open("20.PNG")
photo10 = ImageTk.PhotoImage(image10)
Label(image=photo10).grid(row=3, column=56)
Button(text="View", font=("comicsans", 15, "normal"), command=win6, bg="light blue").grid(row=7, column=56, pady=10)
Button(text="Book", font=("comicsans", 15, "normal"),command=book7, bg="light blue").grid(row=8, column=56, pady=5)
Button(text="Submit", font=("comicsans", 15, "normal"),command=submit, bg="light blue").grid(row=9, column=56, pady=5)





Label(text="Upcoming Movies ", font=("Comic Sans MS", 20, "bold", "underline"), bg="light blue").grid(row=11, column=26)
image7 = Image.open("15.PNG")
photo7 = ImageTk.PhotoImage(image7)
Label(image=photo7).grid(row=13, column=6)

image8 = Image.open("16.PNG")
photo8 = ImageTk.PhotoImage(image8)
Label(image=photo8).grid(row=13, column=26)

image9 = Image.open("17.PNG")
photo9 = ImageTk.PhotoImage(image9)
Label(image=photo9).grid(row=13, column=46)
root.mainloop()

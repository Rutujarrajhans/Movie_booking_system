from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import sqlite3
from PIL import Image, ImageTk 
#import h
with sqlite3.connect('address_book.db') as db:
    c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS `Show1` (
	`show_id` INT ,
	`start_time` TIME,
	`end_time` TIME ,
	`language` varchar(255) ,`show_date` DATE ,
	`movie_id` INT,
	PRIMARY KEY (`show_id`))"""
)



db.commit()
db.close()
class DateWindow:


    
    def __init__(self):
         #tkinter can't take jpg so Imagetk module
        self.var1_root = Tk()

        self.canvas = Canvas(self.var1_root,width = 600,height= 400,bg="white")
        self.canvas.pack(expand=YES, fill=BOTH)

        self.var1_root.geometry("500x500")  #for width and height
        self.var1_root.title("Date")
        self.frame1()
        self.frame2()

    def frame1(self):
        self.frame = Frame(self.var1_root,height=290,width=230,bg="white")
        self.frame.place(x=650, y= 50)

        x,y = 0,0

        self.photo = PhotoImage(file="C:\\Users\\shree\\Downloads\\c1.png")
        self.lab2 = Label(self.frame,image=self.photo)
        self.lab2.place(x=x+0, y=y+0)

        self.phototitle = Label(self.frame,text="Select a Date")
        self.phototitle.config(font=("Arial",20,"bold"))
        self.phototitle.place(x=20,y=y+250)


    def frame2(self):
        self.frameb = Frame(self.var1_root,height=200,width=1150,bg="red",relief = RAISED,borderwidth = 10)
        self.frameb.place(x=180, y= 500)

        self.myFont = font.Font(size=15)
        self.font2 =  font.Font(size = 13)

        self.menubutton1 = Menubutton(self.var1_root, text = "21/04/2020",activebackground="orange" , relief = RAISED,width=10,height=5,bg="grey",fg="white")  
        self.menubutton1.menu = Menu(self.menubutton1)  
        self.menubutton1['font'] = self.myFont
        self.menubutton1["menu"]=self.menubutton1.menu  
        self.menubutton1.menu.add_checkbutton(label = "10:00 AM", variable=IntVar(),font= self.font2,command=lambda : print("21/04/2020 - 10:00 AM"))
        #messagebox.showinfo("thanks")
        self.menubutton1.menu.add_checkbutton(label = "12:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("21/04/2020 - 12:00 PM"))
        self.menubutton1.menu.add_checkbutton(label = "2:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("21/04/2020 - 2:00 PM"))
        self.menubutton1.menu.add_checkbutton(label = "5:00 PM",font= self.font2 , variable = IntVar(),command=lambda : print("21/04/2020 - 5:00 PM"))  
        self.menubutton1.place(x=200,y=550)
        
        self.menubutton2 = Menubutton(self.var1_root, text = "22/04/2020",activebackground="orange" , relief = RAISED,width=10,height=5,bg="grey",fg="white")  
        self.menubutton2.menu = Menu(self.menubutton2)  
        self.menubutton2['font'] = self.myFont
        self.menubutton2["menu"]=self.menubutton2.menu  
        self.menubutton2.menu.add_checkbutton(label = "10:00 AM",font= self.font2, variable=IntVar(),command=lambda : print("22/04/2020 - 10:00 AM"))  
        self.menubutton2.menu.add_checkbutton(label = "12:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("22/04/2020 - 12:00 PM"))
        self.menubutton2.menu.add_checkbutton(label = "2:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("22/04/2020 - 2:00 PM"))
        self.menubutton2.menu.add_checkbutton(label = "5:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("22/04/2020 - 5:00 PM"))  
        self.menubutton2.place(x=400,y=550)

        self.menubutton3 = Menubutton(self.var1_root, text = "23/04/2020",activebackground="orange" , relief = RAISED,width=10,height=5,bg="grey",fg="white")  
        self.menubutton3.menu = Menu(self.menubutton3)  
        self.menubutton3['font'] = self.myFont
        self.menubutton3["menu"]=self.menubutton3.menu  
        self.menubutton3.menu.add_checkbutton(label = "10:00 AM",font= self.font2, variable=IntVar(),command=lambda : print("23/04/2020 - 10:00 AM"))  
        self.menubutton3.menu.add_checkbutton(label = "12:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("23/04/2020 - 12:00 PM"))
        self.menubutton3.menu.add_checkbutton(label = "2:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("23/04/2020 - 2:00 PM"))
        self.menubutton3.menu.add_checkbutton(label = "5:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("23/04/2020 - 5:00 PM"))  
        self.menubutton3.place(x=600,y=550)

        self.menubutton4 = Menubutton(self.var1_root, text = "24/04/2020",activebackground="orange" , relief = RAISED,width=10,height=5,bg="grey",fg="white")  
        self.menubutton4.menu = Menu(self.menubutton4)  
        self.menubutton4['font'] = self.myFont
        self.menubutton4["menu"]=self.menubutton4.menu  
        self.menubutton4.menu.add_checkbutton(label = "10:00 AM",font= self.font2, variable=IntVar(),command=lambda : print("2404/2020 - 10:00 AM"))  
        self.menubutton4.menu.add_checkbutton(label = "12:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("24/04/2020 - 12:00 PM"))
        self.menubutton4.menu.add_checkbutton(label = "2:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("24/04/2020 - 2:00 PM"))
        self.menubutton4.menu.add_checkbutton(label = "5:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("24/04/2020 - 5:00 PM"))  
        self.menubutton4.place(x=800,y=550)

        self.menubutton5 = Menubutton(self.var1_root, text = "25/04/2020",activebackground="orange" , relief = RAISED,width=10,height=5,bg="grey",fg="white")  
        self.menubutton5.menu = Menu(self.menubutton5)  
        self.menubutton5['font'] = self.myFont
        self.menubutton5["menu"]=self.menubutton5.menu  
        self.menubutton5.menu.add_checkbutton(label = "10:00 AM",font= self.font2, variable=IntVar(),command=lambda : print("25/04/2020 - 10:00 AM"))  
        self.menubutton5.menu.add_checkbutton(label = "12:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("25/04/2020 - 12:00 PM"))  
        self.menubutton5.menu.add_checkbutton(label = "2:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("25/04/2020 - 2:00 PM"))
        self.menubutton5.menu.add_checkbutton(label = "5:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("25/04/2020 - 5:00 PM"))
        self.menubutton5.place(x=1000,y=550)
          
        self.menubutton6 = Menubutton(self.var1_root, text = "26/04/2020",activebackground="orange" ,relief = RAISED,width=10,height=5,bg="grey",fg="white")  
        self.menubutton6.menu = Menu(self.menubutton6)  
        self.menubutton6['font'] = self.myFont
        self.menubutton6["menu"]=self.menubutton6.menu  
        self.menubutton6.menu.add_checkbutton(label = "10:00 AM",font= self.font2, variable=IntVar(),command=lambda : print("26/04/2020 - 10:00 AM"))  
        self.menubutton6.menu.add_checkbutton(label = "12:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("26/04/2020 - 12:00 PM")) 
        self.menubutton6.menu.add_checkbutton(label = "2:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("26/04/2020 - 2:00 PM"))
        self.menubutton6.menu.add_checkbutton(label = "5:00 PM",font= self.font2, variable = IntVar(),command=lambda : print("26/04/2020 - 5:00 PM")) 
        self.menubutton6.place(x=1180,y=550)
        Button(self.var1_root,text="submit",font=('',15),command=self.submit).pack()
        Button(self.var1_root,text="NEXT",font=('',15),command=self.next).pack()
    def submit(self):
        messagebox.showinfo("thanks")
        



       # self.var1_root.mainloop()
    def next(self):
        self.var1_root.destroy()
        import h
       # global parent
        h.MainApp()
    

if __name__ == "__main__":
    k = DateWindow()
    k.frame1()
    k.frame2()
    

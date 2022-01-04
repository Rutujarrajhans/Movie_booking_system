from tkinter import *
from PIL import Image , ImageTk
import list_of_movies
import ru

root = Tk()
root.geometry("600x600")
root.title("theatre options")


def t():
    root.destroy()
    ru.DateWindow()
    



b5=Button(root ,text = 'NEXT ',bd = 3 ,command=t,font = ('comic sans ms',15,"italic"))
b5.pack()




    #ru.DateWindow
def h():
    pass
    

f1=Frame(root,borderwidth=6,relief=FLAT)
l1=Label(f1,text="*cinemas near you*",font=("times new roman", 50 ,"bold"),padx=10,pady=10,bg="black",fg="turquoise1")
l1.pack()
f1.pack(side=TOP)



f2=Frame(root,bg="grey",borderwidth=6,relief=RIDGE,padx=10,pady=10)


lbl1=Label(f2,text="ashok anil multiplex",font=("comic sans ms",20,"italic"),bg="grey")
lbl1.pack()
image1=Image.open("aa.jpg")
photo=ImageTk.PhotoImage(image1)
lbl3=Label(f2,image=photo,borderwidth=5,relief=RIDGE)
lbl3.pack()

b1=Button(f2 ,text = ' click for seats ',bd = 3 ,command=h,font = ('comic sans ms',15,"italic"))

b1.pack()


f2.pack(side=LEFT,padx=30,pady=30)

f3=Frame(root,bg="grey",borderwidth=6,relief=RIDGE,padx=10,pady=10)
lbl2=Label(f3,text="inox",font=("comic sans ms",20,"italic"),bg="grey")
lbl2.pack()
image2=Image.open("inox.jpg")
photo2=ImageTk.PhotoImage(image2)
lbl3=Label(f3,image=photo2,borderwidth=5,relief=RIDGE)
lbl3.pack(side=TOP,anchor="n")

b2=Button(f3 ,text = ' click for seats ',bd = 3 ,command=h,font = ('comic sans ms',15,"italic"))
b2.pack()



f3.pack(side=LEFT,padx=30,pady=30)


f4=Frame(root,bg="grey",borderwidth=6,relief=RIDGE,padx=10,pady=10)
lb4=Label(f4,text="cinepolis",font=("comic sans ms",20,"italic"),bg="grey")
lb4.pack()
image3=Image.open("cine.jpg")
photo3=ImageTk.PhotoImage(image3)
lb5=Label(f4,image=photo3,borderwidth=5,relief=RIDGE)
lb5.pack()

b3=Button(f4 ,text = ' click for seats ',bd = 3 ,command=h,font = ('comic sans ms',15,"italic"))
b3.pack()



f4.pack(side=LEFT,padx=30,pady=30)

f5=Frame(root,bg="grey",borderwidth=6,relief=RIDGE,padx=10,pady=25)
lb6=Label(f5,text="PVR cinemas",font=("comic sans ms",20,"italic"),bg="grey")
lb6.pack()
image4=Image.open("download.jpg")
photo4=ImageTk.PhotoImage(image4)
lb7=Label(f5,image=photo4,borderwidth=5,relief=RIDGE)
lb7.pack()

b4=Button(f5 ,text = ' click for seats ',bd = 3 ,command=h,font = ('comic sans ms',15,"italic"))
b4.pack()



f5.pack(side=LEFT,padx=30,pady=30)


root.mainloop()

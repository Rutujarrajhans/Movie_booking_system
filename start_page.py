from tkinter import *
from PIL import Image , ImageTk
root = Tk()
root.title("Account Login")
root.geometry("1000x1000")
root.config(bg="white")

photo = PhotoImage(file="mo2.PNG")

lab = Label(image=photo)
lab.pack()

name = Label(root, text="Movies Galore", font=("ROG Fonts", 40, "bold"),bg="white")
name.pack()
quote = Label(root, text="“Go ahead, make your day.”", font=("Georgia", 20, "bold", "italic"),bg="white")
quote.pack(pady=(10, 80))

# create Login Button
Button(text="Login", height="5", width="50",font=("Georgia", 10, "normal"),bg="grey",relief=SUNKEN).pack(pady=(20, 50))



root.mainloop()

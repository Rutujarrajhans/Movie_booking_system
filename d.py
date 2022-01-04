import smtplib
from tkinter import *

root=Tk()

v=StringVar()
entry=Entry(root, textvariable=v)


sender = "email@email.com.au"
receiver = [v]
message = """From: <email@email.com.au>
To: email@email.com 
Subject: I made a code to send this!
Hello i made a code to send this!"""

try:    
    session = smtplib.SMTP('mail.optusnet.com.au',25)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(sender,'passwrd')
    session.sendmail(sender,receiver,message)
    session.quit()

except smtplib.SMTPException as e:
    print(e)
root.mainloop()

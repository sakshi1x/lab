from tkinter import Tk,LEFT ,BOTH
import tkinter
from tkinter.constants import LEFT
root = tkinter.Tk()
root.geometry("500x500")
root.config(background="#E6E6FA")
c = tkinter.Label(root, text="registration").pack()
first_var = tkinter.StringVar()
second_var = tkinter.StringVar()
email_var = tkinter.StringVar()
password_var = tkinter.StringVar()
def submit():
    first = first_var.get()
    second = second_var.get()
    email = email_var.get()
    password = password_var.get()
    print("your first name is : " + first)
    print("your second name is : "+ second)
    print("your email is : "+ email)
    print("your password is : "+ password)
    first_var.set("")
    second_var.set("")
    email_var.set("")
    
    password_var.set("")
f = tkinter.Label(root,text = "first name : ").pack()
f1=tkinter.Entry(root,textvariable = first_var).pack()
s = tkinter.Label(root,text = "second name : ").pack()
s2=tkinter.Entry(root,textvariable = second_var).pack()

e =tkinter.Label(root,text = "email : ").pack()
e2=tkinter.Entry(root,textvariable = email_var).pack()
p =tkinter.Label(root,text = "password : ").pack()

p2=tkinter.Entry(root,textvariable = password_var).pack()
b = tkinter.Button(root,text = "submit", command=submit).pack()
root.mainloop()





from tkinter import Tk
import tkinter

root = tkinter.Tk()
root.geometry("500x500")
root.config(background="#E6E6FA")
c = tkinter.Label(root, text="registration").grid(row = 0, column=0)
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
f = tkinter.Label(root,text = "first name : ").grid(row = 1, column=1)
f1=tkinter.Entry(root,textvariable = first_var).grid(row = 1, column=2)
s = tkinter.Label(root,text = "second name : ").grid(row = 2, column=1)
s2=tkinter.Entry(root,textvariable = second_var).grid(row = 2, column=2)

e =tkinter.Label(root,text = "email : ").grid(row = 3, column=1)
e2=tkinter.Entry(root,textvariable = email_var).grid(row = 3, column=2)
p =tkinter.Label(root,text = "password : ").grid(row = 4, column=1)

p2=tkinter.Entry(root,textvariable = password_var).grid(row = 4, column=2)
b = tkinter.Button(root,text = "submit", command=submit).grid(row = 5, column=1)
root.mainloop()
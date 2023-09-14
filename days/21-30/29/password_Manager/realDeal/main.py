from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from passwordGenerator import generatePassword as passs
from pyperclip import copy
def newPassword():
    new = passs(4,4,4)
    password.delete(0,END)
    password.insert(0,new)
    copy(new)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    line = ""
    space = " | "
    for i in [s.get() for s in [email, password, website]]:
        if(i==""):
            messagebox.showinfo("Hi", "Please fill in all the boxes.")
            return
    with open("data.txt", "a") as f:
        f.write(f"{website.get()} | {email.get()} | {password.get()}")

    messagebox.showinfo("Hi", "Password Created.")
    website.delete(0,END)
    password.delete(0,END)

    with open("data.txt", "a") as f:
        f.write(f"{line}\n\n")


# ---------------------------- UI SETUP ------------------------------- #

r = Tk()
#r.geometry("500x500")

# Creates the logo
r.config(padx=50,pady=50)
logo = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
logo.create_image(100, 95, image=image)
logo.grid(row=0, column=1)

# Website
label = Label(text="Website: ")
label.grid(row=1,column=0)

website = Entry(width=35)
website.grid(row=1, column=1, columnspan=2)
website.focus()

# Email/Username
label = Label(text="Email/Username: ")
label.grid(row=2,column=0)
email = Entry(width=35)
email.grid(row=2, column=1, columnspan=2)
email.insert(0, "leo@orr.nu")

# Password
label = Label(text="Password: ")
label.grid(row=3,column=0)
password = Entry(width=21)
password.grid(row=3, column=1, sticky="w", padx=(50,0))

generatePassword = Button(text="Generate Password")
generatePassword.grid(row=3, column=2, sticky="w")
generatePassword["command"] = newPassword

# Add
add = Button(text="Add", width=36)
add.grid(row=4, column=1, columnspan=2)
add["command"] = save

r.mainloop()

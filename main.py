# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
def gen_password():
   letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
   symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
   
   print("Welcome to the PyPassword Generator!")
   nr_letters = random.randint(5,7)
   nr_symbols = random.randint(2,4)
   nr_numbers = random.randint(2,4)

  # Create an empty list
   password_list = []


   for _ in range(nr_letters):
    password_list.append(random.choice(letters))


   for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))


   for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

   random.shuffle(password_list)#important step to shuffle list

# Join the list into a string
   password = ''.join(password_list)
   password_entry.insert(0,password)
   pyperclip.copy(password)


   
   


          

# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
def add_password():

    if len(password_entry.get())==0 or len(email_entry.get())==0 or len(password_entry.get())==0:
       messagebox.showinfo(title="OOPS",message="Please fill in the required details.")
    else:
        is_ok=messagebox.askokcancel(title=website_entry.get(),message=f"These are the details entered: \n Website:{website_entry.get()} \n Email:{email_entry.get()} \n Password:{password_entry.get()} \n Is it ok?")
        if is_ok:
         with open("Passwords.txt", "a") as data_file:
          data_file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n ")
          website_entry.delete(0,END)
          password_entry.delete(0,END)
       
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Password manager")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200,)
lock_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

#labels
website_label=Label(text="Website:")
website_label.grid(row=1,column=0 )
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"tanish.sthalekar@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button=Button(text="Generate  Password",command=gen_password)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=add_password)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()
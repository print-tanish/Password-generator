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

import json
 
   


         

# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
def add_password():
    email=email_entry.get() 
    password=password_entry.get()
    new_password={
       website_entry.get():{
        "email": email,
        "password":password 
  }}

    if len(password_entry.get())==0 or len(email_entry.get())==0 or len(password_entry.get())==0:
       messagebox.showinfo(title="OOPS",message="Please fill in the required details.")
    else:
        
     try:   
      with open("Passwords.json", "w") as data_file:
        data=json.load(new_password)
        
     except FileNotFoundError:
       with open("data.json","w") as data_file:
         json.dump(new_password,data_file,indent=4)
         
     else:
       data.update(new_password)
       with open("Passwords.json", "r") as data_file:
         json.dump(new_password,data_file,indent=4)
     finally:
        website_entry.delete(0,END)
        password_entry.delete(0,END)
def find_password():
  website=website_entry.get()
  try:
   with open("Passwords.json") as data_file:
    data=json.load(data_file)
  except FileNotFoundError:
    messagebox.showinfo(title="Error",message="no data file found.")
  else:  
    if website in data:
      email=data[website]["email"]
      password=data[website]["password"]
      messagebox.showinfo(title=website,message=f"Email: {email}\n Password: {password} ")
    else:
      messagebox.showinfo(title="error",message=f"No details for {website} exists.")
  
          
     
       
       
      
       
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
website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1)
email_entry.insert(0,"tanish.sthalekar@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button=Button(text="Generate  Password",command=gen_password)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=add_password)
add_button.grid(row=4,column=1,columnspan=2)
search_button=Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2,columnspan=2)


window.mainloop()
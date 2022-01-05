from tkinter import *
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
final_passwd = []
window = Tk()
#window.config(height=800,width=800,padx=40,pady=40,)
window.config(padx=20,pady=20,bg="black")
window.title("Password Manager")
canvas = Canvas(width=200,height=200,highlightthickness=0,bg="black")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=1)


def add():
    with open("datafile.txt","w") as datafile:
        datafile.write(f"{web_entry.get()} | {user_entry.get()} | {pass_entry.get()} \n")
    datafile.close()
def generate():
    pass_entry.delete(0,END)
    for char in range(1, 5):
        final_passwd.append(random.choice(letters))
    for char in range(1, 5):
        final_passwd.append(random.choice(numbers))
    for char in range(1, 5):
        final_passwd.append(random.choice(symbols))
    random.shuffle(final_passwd)
    pass_entry.insert(0,final_passwd)
    final_passwd.clear()

web_entry = Entry(width=35)
web_entry.grid(columnspan=2,row=2,column=1)

web_label = Label(text="Website:    ",bg="white")
web_label.grid(row=2,column=0)

user_label = Label(text="User/Email:",bg="white")
user_label.grid(row=3,column=0)

user_entry = Entry(width=35)
user_entry.grid(row=3,column=1,columnspan=2)

user_entry.insert(0,"your_email@gmail.com")
password_label = Label(text="Password:  ",bg="white")
password_label.grid(row=4,column=0)

pass_entry = Entry(width=35)
pass_entry.grid(row=4,column=1,columnspan=2)

generate_button = Button(text="Generate Password",width=21,command=generate)
generate_button.grid(row=4,column=3)

add_button = Button(text="Add",width=36,command=add).grid(row=5,column=1,columnspan=2)















window.mainloop()

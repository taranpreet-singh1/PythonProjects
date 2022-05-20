#Thanks to Data-flair training for this project idea and support

#Using Tkinter(GUI Library), pyperclip, random and string

from tkinter import *
import random, string


#initialize window

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("DataFlair - PASSWORD GENERATOR")

#heading
heading = Label(root, text = 'Password Generator', font ='arial 20 bold').pack()
Label(root, text= 'DataFlair', font = 'arial 15 bold').pack(side = BOTTOM)

#select password length label
pass_label = Label(root, text = 'Password Length', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32, textvariable = pass_len, width = 15).pack()

#Random number generator function
pass_str = StringVar()

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()-4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        pass_str.set(password)

#button
Button(root, text = "Generate Password", command = Generator).pack(pady=5)

Entry(root, textvariable = pass_str).pack()



#loop to run program
root.mainloop()
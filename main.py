from tkinter import *

import time

# Creating a new window and configurations
window = Tk()
window.title("Disappearing Text")
window.minsize(width=800, height=600)
window.config(bg='skyblue')


def deleteText():
    entryField.after(1000, clearText())

def clearText():
    # textField.config(state='normal')
    entryField.delete(0, 'end')
    # textField.config(state='disabled')

#Create a frame for the label for 'Disappearing Text'
label_frame = Frame(master=window, width=80, height=20, bg='grey')
label_frame.pack()

# Label for title
Label(master=label_frame, text="Disappearing Text",
      font=("Times New Roman", 20, "bold")).pack()

# Entry for entering text
entryField = Entry(window, width=80, bd="3", relief="solid")

entryField.bind('<Key>', lambda e: e.widget.after(20000, clearText))
entryField.bind('<Return>', lambda e: e.widget.after(20000, clearText))
entryField.pack(padx=30, pady=30, ipadx=50, ipady=50)

window.mainloop()

import tkinter
import os

mainwindow = tkinter.Tk()
mainwindow.geometry("680x480+350+200")
mainwindow.title("This is my first application")

label = tkinter.Label(mainwindow, text="This is label 1")
label.place(x=400, y=30, width=200, height=50)

listbox = tkinter.Listbox(mainwindow)
listbox.place(x=20, y=30, width=300, height=400)

scrollbar = tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command=listbox.yview)
scrollbar.place(x=310, y=30, width=30, height=400)

listbox['yscrollcommand'] = scrollbar.set

for value in os.listdir(r"C:\Users\evsairn\Desktop\Mar 2021\Files"):
    listbox.insert(tkinter.END, value)


mainwindow.mainloop()

import tkinter
import os
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

mainwindow = tkinter.Tk()

mainwindow.title("Grid Demo")
mainwindow.geometry("650x450+380+170")
mainwindow['padx'] = 8

lframe = tkinter.Frame(mainwindow, relief='raised', borderwidth=3, bg='orange')
lframe.place(x=0, y=0, width=650, height=60)

label = tkinter.Label(lframe, text="Tkinter Place Demo", font='ariel')
label.place(x=240, y=12)

listbox = tkinter.Listbox(mainwindow)
listbox.place(x=2, y=70, width=110, height=270)

for zone in os.listdir('/windows/System32'):
    listbox.insert(tkinter.END, zone)

scrollbar = tkinter.Scrollbar(mainwindow, orient= tkinter.VERTICAL, command= listbox.yview)
scrollbar.place(x=110, y=70, width=20, height=270)

listbox['yscrollcommand'] = scrollbar.set

optionframe = tkinter.LabelFrame(mainwindow, text="File Details")
optionframe.place(x=270, y=70, width=170, height=150)

rbvalue = tkinter.IntVar()
rbvalue.set(3)

radiobutton1 = tkinter.Radiobutton(optionframe, text='Filename', value=1, variable=rbvalue)
radiobutton2 = tkinter.Radiobutton(optionframe, text='Path', value=2, variable=rbvalue)
radiobutton3 = tkinter.Radiobutton(optionframe, text='Timestap', value=3, variable=rbvalue)
radiobutton1.place(x=2, y=7)
radiobutton2.place(x=2, y=27)
radiobutton3.place(x=2, y=45)


def clickme():
    if rbvalue.get() == 2:
        messagebox.showinfo("Alert", "You have selected {}".format(rbvalue))
    else:
        messagebox.showinfo("Selection", "You have not selected the option 2")


# def clickme(event):
#     msgbox = tkinter.Message(mainwindow, text="Hey, you clicked me!!")
#     msgbox.place(x=270, y=200)
#     messagebox.showinfo("Confirmation","Hello Coder!")

resultlabel = tkinter.Label(mainwindow, text="Result")
resultlabel.place(x=135, y=300)

entry = tkinter.Entry(mainwindow)
entry.place(x=135, y=320, width=70, height=20)

# button1 = tkinter.Button(mainwindow, text='Run', relief='raised', command=clickme)
# #button1.bind("<Enter>", clickme)
# button1.place(x=270, y=270, width=100, height=35)

timeframe = tkinter.LabelFrame(mainwindow, text="Time")
timeframe.place(x=2, y=350,width=150, height=50)

hourspinbox = tkinter.Spinbox(timeframe, value=tuple(range(0,24)))
minspinbox = tkinter.Spinbox(timeframe, from_=0, to=59)
secondsspinbox = tkinter.Spinbox(timeframe, from_=0, to=59)
hourspinbox.place(x=15, y=5, width=35, height=20)
minspinbox.place(x=50, y=5, width=35, height=20)
secondsspinbox.place(x=85, y=5, width=35,height=20)

dateframe = tkinter.Frame(mainwindow)
dateframe.place(x=2,y=400, width=150, height=100)

tkinter.Label(dateframe, text="Day").place(x=2, y=6)
tkinter.Label(dateframe, text="Month").place(x=28, y=6)
tkinter.Label(dateframe, text="Year").place(x=70, y=6)

dayspinbox = tkinter.Spinbox(dateframe, from_=1, to=31)
monthspinbox = tkinter.Spinbox(dateframe, value=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
yearspinbox = tkinter.Spinbox(dateframe, from_=2000, to=2099)
dayspinbox.place(x=2, y=26, width=35, height=20)
monthspinbox.place(x=36, y=26, width=35, height=20)
yearspinbox.place(x=75, y=26, width=40, height=20)

def selcted(event):
    mylabel = tkinter.Label(mainwindow, text=clicked.get()).place(x=200, y=300, width=100, height=20)

options = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
]

clicked = tkinter.StringVar()
clicked.set(options[0])

drop = tkinter.OptionMenu(mainwindow, clicked, *options, command=selcted)
drop.place(x=200, y=200)


def test3():
    if mycombo.get() == "Wed":
        messagebox.showinfo("Hello","Today is wednesday")
    else:
        messagebox.showinfo("Hello1","Today is Tuesday")


def clickevent(event):
    if mycombo.get() == "Wed":
        messagebox.showinfo("Sucess", "Wednesday")
    else:
        messagebox.showwarning("ok", "Tuesday")


button1 = tkinter.Button(mainwindow, text='Run', relief='raised', command=test3)
#button1.bind("<Enter>", clickme)
button1.place(x=270, y=270, width=100, height=35)

mycombo = ttk.Combobox(mainwindow, value=("Mon","Tues","Wed"))
mycombo.bind("<<ComboboxSelected>>", clickevent)
mycombo.place(x=300, y=400)


def mybrowse():
    bowse = filedialog.askopenfilename(initialdir=r"C:\Users\evsairn\Desktop", title="Please choose your file", filetypes=(("Excel file","*.xlsx"),("All files","*.*")))


browse = tkinter.Button(mainwindow, text="Browse", relief="raised", command=mybrowse)
browse.place(x=430, y=270, width=100, height=35)

quitbutton = tkinter.Button(mainwindow, text="Quit", relief="raised", command=mainwindow.quit)
quitbutton.place(x=540, y=270, width=100, height=35)

mainwindow.update()
mainwindow.minsize(mainwindow.winfo_width(), mainwindow.winfo_height())
mainwindow.maxsize(mainwindow.winfo_width(), mainwindow.winfo_height())
mainwindow.mainloop()

# def printing():
#     print("Hello World")

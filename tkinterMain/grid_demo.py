import tkinter

mainwindow = tkinter.Tk()

mainwindow.title("Hello world")
mainwindow.geometry('640x480-8-200')

label = tkinter.Label(mainwindow, text="Hello Wold")
#label.grid(row=0, column=0)
label.place(x=20,y=50)

leftframe = tkinter.Frame(mainwindow)
leftframe.grid(row=1,column=1)

canvas = tkinter.Canvas(leftframe, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)
#canvas.place(x=20, y=30)

rightframe = tkinter.Frame(mainwindow)
rightframe.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(rightframe, text="button1")
button2 = tkinter.Button(rightframe, text="button2")
button3 = tkinter.Button(rightframe, text="button3")
button1.grid(row=1, column=0)
button2.grid(row=2, column=0)
button3.grid(row=3, column=0)

mainwindow.columnconfigure(0,weight=1)
mainwindow.columnconfigure(1,weight=1)
mainwindow.columnconfigure(2, weight=1)

leftframe.config(relief='sunken', borderwidth=1)
rightframe.config(relief='sunken', borderwidth=1)
leftframe.grid(sticky='ns')
rightframe.grid(sticky='new')
rightframe.columnconfigure(0,weight=1)

button2.grid(sticky='ew')

mainwindow.mainloop()

# mainwindow = tkinter.Tk()
#
# mainwindow.title("Login form")
# mainwindow.geometry('350x150+550+300')
#
# label = tkinter.Label(mainwindow, text="Ericsson IDM Portal Bot")
# label.grid(row=0,column=0)
#
# frame1 = tkinter.Frame(mainwindow)
# frame1.grid(row=1, column=0, sticky='nw')
#
# frame1.config(borderwidth=5)
#
# label2 = tkinter.Label(frame1, text="User Name")
# label2.grid(row=0, column=0)
#
# entry1 = tkinter.Entry(frame1)
# entry1.grid(row=0, column=1)
#
# label3 = tkinter.Label(frame1, text="Password")
# label3.grid(row=1, column=0)
#
# entry2 = tkinter.Entry(frame1)
# entry2.grid(row=1, column=1)
#
# button1 = tkinter.Button(frame1, text="Run")
# button1.grid(row=2, column=1)
#
# frame1.columnconfigure(0, weight=1)
# frame1.columnconfigure(1, weight=1)
#
# button1.grid(sticky='ew')
#
# mainwindow.mainloop()
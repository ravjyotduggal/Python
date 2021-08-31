import tkinter
import os
mainwindow = tkinter.Tk()

mainwindow.title("Grid Demo")
mainwindow.geometry('640x480-8-200')
mainwindow['padx'] = 8

label= tkinter.Label(mainwindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

mainwindow.columnconfigure(0, weight=100)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=1000)
mainwindow.columnconfigure(3, weight=600)
mainwindow.columnconfigure(4, weight=1000)

mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=10)
mainwindow.rowconfigure(2, weight=1)
mainwindow.rowconfigure(3, weight=3)
mainwindow.rowconfigure(4, weight=3)

fileList= tkinter.Listbox(mainwindow)
fileList.grid(row=1, column=0, sticky='nsew',rowspan=2)
fileList.config(relief='sunken', border=2)

for zone in os.listdir('/windows/System32'):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainwindow, orient= tkinter.VERTICAL, command= fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

optionFrame = tkinter.LabelFrame(mainwindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

rbvalue = tkinter.IntVar()
rbvalue.set(3)

#Radiobuttons

radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbvalue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbvalue)
radio3 = tkinter.Radiobutton(optionFrame, text="TimeStamp", value=3, variable=rbvalue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

resultlabel = tkinter.Label(mainwindow, text="Result")
resultlabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainwindow)
result.grid(row=2,column=2, sticky='sw')

#Frame for the timespinners

timeframe = tkinter.LabelFrame(mainwindow, text="Time")
timeframe.grid(row=3, column=0, sticky='new')

#Timespinners
hourspinenr = tkinter.Spinbox(timeframe, width=2, values=tuple(range(0,24)))
minutespinner = tkinter.Spinbox(timeframe, width= 2, from_=0, to=59)
secondsspinner = tkinter.Spinbox(timeframe, width=2, from_=0, to=59)
hourspinenr.grid(row=0, column=0)
tkinter.Label(timeframe,text=":").grid(row=0, column=1)
minutespinner.grid(row=0,column=2)
tkinter.Label(timeframe,text=":").grid(row=0,column=3)
secondsspinner.grid(row=0, column=4)
timeframe['padx'] = 36

#Frame for date spinners
dateFrame = tkinter.Frame(mainwindow)
dateFrame.grid(row=4,column=0, sticky='new')
#Data lables
daylabel = tkinter.Label(dateFrame, text="Day")
monthlabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")
daylabel.grid(row=0, column= 0, sticky='w')
monthlabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0,column=2, sticky='w')

#DataSpinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan","Feb","Mar","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpin.grid(row=1,column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

okButton = tkinter.Button(mainwindow, text="OK")
cancelButton = tkinter.Button(mainwindow, text="Cancel", command=mainwindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainwindow.mainloop()

#print(rbvalue.get())
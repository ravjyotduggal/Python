import shutil
import pandas as pd
import tkinter
from tkinter import filedialog
from tkinter import messagebox


def file_transfer():
    global filetransferred
    global filenottransferred
    filecount= 0
    filenf = 0
    source = []
    destination = []

    df = pd.read_excel(r"{}".format(basefile))

    file_source = r"{}".format(folderselection)

    for filename in df["Report_Name"]:
        source.append(filename)

    for destname in df["Destination"]:
        destination.append(destname)

    for number, files in enumerate(source):
        # print(source[number])
        # print(destination[number])
        try:
            final_file = "{}/{}.xlsb".format(file_source,source[number])
            print(final_file)
            shutil.copy(final_file, destination[number])
        except:
            final_file = "{}/{}.xlsx".format(file_source,source[number])
            print(final_file)
            try:
                shutil.copy(final_file, destination[number])
            except:
                print("File not found - {}".format(files))
                filenf += 1
        filecount += 1

    filetransferred.set(filecount)
    filenottransferred.set(filenf)
    messagebox.showinfo(title="Success", message="File Transferred Successfully!")

def uplaodbasefile():
    global basefile
    basefile = filedialog.askopenfilename(initialdir="Desktop://", title="Please choose Base file", filetypes=(("Excel File", "*xlsx"),("All File","*.*")))
    ublabel.set(basefile)


def sourcefolder():
    global folderselection
    folderselection = filedialog.askdirectory(title="Please choose the source folder")
    folderlabelname.set(folderselection)

root = tkinter.Tk()
root.title("File Transfer Application")
root.geometry("650x450+400+180")

basefile = ""
folderselection = ""
filetransferred = tkinter.IntVar()
filenottransferred = tkinter.IntVar()

label1 = tkinter.Label(root, background="grey", text="File Transfer", fg="white", font="Ariel 12 bold")
label1.place(x=0, y=0, width=650, height=50)

labelframe = tkinter.LabelFrame(root, text="Directory", font="Ariel 9")
labelframe.place(x=20, y=70, width=600, height=130)

datasetbutton = tkinter.Button(labelframe, text="Upload Base File", command=uplaodbasefile)
datasetbutton.place(x=5, y=10, width=120, height=30)

ublabel = tkinter.StringVar()

datasetlabel = tkinter.Label(labelframe, relief="solid", textvariable=ublabel)
datasetlabel.place(x=150, y=10, width=300, height=30)

soucefolderbutton = tkinter.Button(labelframe, text="Folder Source", command=sourcefolder)
soucefolderbutton.place(x=5, y=60, width=120, height=30)

folderlabelname = tkinter.StringVar()

folderlabel = tkinter.Label(labelframe, relief="solid", textvariable=folderlabelname)
folderlabel.place(x=150, y=60, width=300, height=30)

runbutton = tkinter.Button(root, text="Run", relief="raised", command=file_transfer)
runbutton.place(x=180, y=220, width=120, height=30)

quitbutton = tkinter.Button(root, text="Quit", relief="raised", command=root.quit)
quitbutton.place(x=350, y=220, width=120, height=30)

statsframe = tkinter.LabelFrame(root, text="Statistics", font="Ariel 9")
statsframe.place(x=150, y=280, width=350, height=100)

tkinter.Label(statsframe, text="Total Files Copied", font="Ariel 8 bold").place(x=20,y=8, width=100, height=38)
tkinter.Label(statsframe, text="Files Not Found", font="Ariel 8 bold").place(x=16,y=35, width=100, height=38)
tkinter.Label(statsframe, font="Ariel 8 bold", relief="solid", textvariable=filetransferred).place(x=130,y=18, width=50, height=20)
tkinter.Label(statsframe, font="Ariel 8 bold", relief="solid", textvariable=filenottransferred).place(x=130,y=45, width=50, height=20)

root.update()

root.minsize(root.winfo_width(), root.winfo_height())
root.maxsize(root.winfo_width(), root.winfo_height())

root.mainloop()





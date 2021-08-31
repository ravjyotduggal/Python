from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculator")
root.geometry('400x350+480+230')
#root.iconbitmap(r"C:\Users\evsairn\Desktop\Macro Tools\ericsson_econ.png")
root['padx'] = 8

def test():
    if entry.get() == "Ravjyot":
        messagebox.showinfo("Hello", "Hello Ravjyot")

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=200)
#while True:
entry= Entry(root)
entry.place(x=2, y=4, width=200, height=30)
Button(root, text='C', relief='raised', command=Entry(root).select_clear).place(x=2, y=35, width=30, height=35)
Button(root, text="CE", relief='raised').place(x=33, y=35, width=30, height=35)
Button(root, text='7', relief='raised').place(x=2, y=70, width=30, height=35)
Button(root, text='8', relief='raised').place(x=33, y=70, width=30, height=35)
Button(root, text='9', relief='raised').place(x=63, y=70, width=30, height=35)
Button(root, text='+', relief='raised').place(x=93, y=70, width=30, height=35)
Button(root, text='4', relief='raised').place(x=2, y=106, width=30, height=35)
Button(root, text='5', relief='raised').place(x=33, y=106, width=30, height=35)
Button(root, text='6', relief='raised').place(x=63, y=106, width=30, height=35)
Button(root, text='-', relief='raised').place(x=93, y=106, width=30, height=35)
Button(root, text='1', relief='raised').place(x=2, y=142, width=30, height=35)
Button(root, text='2', relief='raised').place(x=33, y=142, width=30, height=35)
Button(root, text='3', relief='raised').place(x=63, y=142, width=30, height=35)
Button(root, text='*', relief='raised').place(x=93, y=142, width=30, height=35)
Button(root, text='0', relief='raised').place(x=2, y=180, width=30, height=35)
Button(root, text='=', relief='raised').place(x=33, y=180, width=60, height=35)
Button(root, text='/', relief='raised').place(x=93, y=180, width=30, height=35)

Button(root, text="Quit",command= root.destroy).place(x=300, y=200, width=80, height=30)
Button(root, text="test1", command= test).place(x=300, y=300, width=80, height=30)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.maxsize(root.winfo_width(), root.winfo_height())





root.mainloop()


import tkinter as obj
from tkinter import ttk
win=obj.Tk()
# menubar=obj.Menu(win)
def func():
    print("Save")
# menubar.add_command(label='Save',command=func)

# Creating SubMEnu 


menubar=obj.Menu(win)
submenu=obj.Menu(menubar,tearoff=0)
submenu.add_command(label='Save',command=func)
submenu.add_command(label='Save As',command=func)
submenu.add_separator()
menubar.add_cascade(label='File',menu=submenu)

win.config(menu=menubar)
win.mainloop()
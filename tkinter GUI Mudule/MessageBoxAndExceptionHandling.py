import tkinter as obj
from tkinter import ttk
from tkinter import messagebox as m_box
win=obj.Tk()
input1=obj.StringVar()
ttk.Entry(win,width=14,textvariable=input1).grid(row=1,column=0,padx=4,pady=4)
input2=obj.StringVar()
ttk.Entry(win,width=16,textvariable=input2).grid(row=1,column=1,padx=4,pady=4)
def action():
    name_var=input1.get()
    age_var=input2.get()
    if name_var=='' or age_var=='' :
        m_box.showinfo('title','Empety')
    else:
        try:
            age_var=int(age_var)
        except ValueError:
            m_box.showerror('title',"Age Can't be String")
ttk.Button(win,text='Submit', command=action).grid(row=2,column=2)
win.mainloop()
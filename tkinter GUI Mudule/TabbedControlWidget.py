import tkinter as obj
from tkinter import ttk
win=obj.Tk()
win.title('Tab Control')
nb=ttk.Notebook(win)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text='one')
nb.add(page2,text='two')
nb.pack(expand=True,fill='both')

ttk.Label(page1,text='This is First Page').grid(row=1,column=0)
ttk.Entry(page1,text='Submut').grid(row=2,column=0)
ttk.Label(page2,text='This is Second Page').grid(row=1,column=0)
ttk.Entry(page2,text='Submut').grid(row=2,column=0)
win.mainloop()
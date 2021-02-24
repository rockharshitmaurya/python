import tkinter as obj
from tkinter import ttk
win=obj.Tk()
win.title("Loop widgets")
labels=['Name','Class','City','NO']
for item in range(len(labels)):
    lable='Lables'+str(item)
    ttk.Label(win,text=labels[item]).grid(row=item,column=0,sticky=obj.W)
entry_box={
    'Name':obj.StringVar(),
    'Class':obj.StringVar(),
    'City':obj.StringVar(),
    'No':obj.StringVar()
}
counter=0
for i in entry_box:
    variableC="entryVar"+i
    ttk.Entry(win,width=16,textvariable=entry_box[i]).grid(row=counter,column=1)
    counter+=1
def action():
    for v in entry_box:
        print(entry_box[v].get())
ttk.Button(win,text='Submit',command=action).grid(row=6,column=1)

win.mainloop()
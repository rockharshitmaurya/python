import tkinter as obj
from tkinter import ttk
from csv import DictWriter
import os
win=obj.Tk()
#----addTitle
win.title('GUI TEsting')
#-----addLable

ttk.Label(win,text='Enter You name').grid(row=0,column=0,sticky=obj.W) #pack() #grid(row=0,colonm=2)
#-------takingInput and store to a variable
name_input=obj.StringVar()
ttk.Entry(win,width=16,textvariable=name_input).grid(row=0,column=1,sticky=obj.W)
#----addLable

ttk.Label(win,text='What Is Your Age').grid(row=1,column=0,sticky=obj.W) #both lable are not in same line so vo use sticky
age_input=obj.StringVar()
ttk.Entry(win,width=16,textvariable=age_input).grid(row=1,column=1,sticky=obj.W)

ttk.Label(win,text='Enter You E-Mail').grid(row=2,column=0,sticky=obj.W)
email_input=obj.StringVar()
ttk.Entry(win,width=16,textvariable=email_input).grid(row=2,column=1)


# Creating Combo Button 


ttk.Label(win,text='Select Your Gender').grid(row=3,column=0)
gender_value=obj.StringVar()
varGender=ttk.Combobox(win,width=14,textvariable=gender_value,values=('Male','Female','Others'),state='readonly')
varGender.grid(row=3,column=1)
varGender.configure(foreground='red')
varGender.current(0)

# Creat Radio Buttoon

userType=obj.StringVar()
ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=userType).grid(row=4,column=0)
ttk.Radiobutton(win,text='Student',value='Student',variable=userType).grid(row=4,column=1)


#creat Check Box


checkBoxValue=obj.IntVar()
ttk.Checkbutton(win,text='Please Subscirbe Our newsLetter',variable=checkBoxValue).grid(row=6,columnspan=3)


#write to CSV File 

def action():
    with open('file1.csv','a',newline='') as f:
       dict_writer=DictWriter(f,fieldnames=['userName','userAge','userEmail','userGender','userType'])
       if os.stat('file1.csv').st_size==0 :
         dict_writer.writeheader()


       dict_writer.writerow({
           'userName':name_input.get(),
            'userAge':age_input.get(),
            'userEmail':email_input.get(),
            'userGender':gender_value.get(),
            'userType':userType.get()   
       })
# def action():
    # print(name_input.get())
    # name_input.set('')
    # print(age_input.get())
    # print(email_input.get())
    # print(gender_value.get())
    # print(userType.get())
    # if(checkBoxValue.get()==0):
    #     print('Yes')
    # else:
    #     print('NO')
    
    # with open('file.txt','a') as f:
    #     f.write(f"{name_input.get()},{age_input.get()},{email_input.get()},{gender_value.get()},{userType.get()}\n")
    
    varGender.delete(0,obj.END)
ttk.Button(win,text='Submit',command=action).grid(row=7,column=0)
win.mainloop()
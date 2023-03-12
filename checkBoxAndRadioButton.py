from tkinter import *
from  tkinter import ttk
#from tkinter import messagebox
def myfun():
    #massage box
    #messagebox.showinfo('Hello Message','It is My Message')
    discount = int(spn.get())
    subject = 0
    if(ch1.get()):
        subject += 1
    if(ch2.get()):
        subject += 1
    if(ch3.get()):
        subject += 1


    if(opt.get() == 1):
        subject = subject * 300
        if (cmb.get() == 'Sir Ali'):
            subject = subject + 500
        if (cmb.get() == 'Sir Raza'):
            subject = subject + 1000
        if (cmb.get() == 'Sir Allahdad'):
            subject = subject + 1500
        if(spn.get()):
            subject -= subject * discount/100
        lbl.configure(text=f'Total Fees = {subject}')
    if(opt.get() == 2):
        subject = subject * 500
        if (cmb.get() == 'Sir Ali'):
            subject += 500
        if (cmb.get() == 'Sir Raza'):
            subject += 1000
        if (cmb.get() == 'Sir Allahdad'):
            subject += 1500
        if (spn.get()):
            subject -= subject * discount / 100
        lbl.configure(text=f'Total Fees = {subject}')


win = Tk()
win.geometry('600x400')

# MainManu = Menu()
# New_project = Menu ()
# New_project.add_command(Label='New_project',command=myfun)
# MainManu.add_cascade(label='File',menu=New_project)
# win.config(menu=MainManu)

#drop down or combobox
lst = ['Sir Ali','Sir Raza','Sir Allahdad']
cmb = ttk.Combobox(value = lst,stat ='readonly' )
cmb.place(x=10,y=100)

#
spn=Spinbox(from_=1,to=15,stat ='readonly')
spn.place(x=10,y=150)

lbl =Label(text='Total Fees',font=('Arial',20))
lbl.place(x=10,y=200)

# Check Box
ch1 = BooleanVar()
ch2 = BooleanVar()
ch3 = BooleanVar()
chk1 = Checkbutton(text='Java', var = ch1)
chk1.place(x=10,y=10)
chk2 = Checkbutton(text='Python', var = ch2)
chk2.place(x=100,y=10)
chk3 = Checkbutton(text='Flutter', var = ch3)
chk3.place(x=200,y=10)

#Radio Button
opt =IntVar()
rad1 = Radiobutton(text='Morning',value=1,variable= opt)
rad1.place(x=10,y=50)
rad2 = Radiobutton(text='Evening',value=2,variable= opt)
rad2.place(x=100,y=50)

tab_obj= ttk.Notebook(width=200,height=150)
tab1 = ttk.Frame()
tab_obj.add(tab1,text='my Tab1')

tab2 = ttk.Frame()
tab_obj.add(tab2,text='my Tab2')

tab_obj.place(x=300,y=100)
lbl1 =Label(tab1,text='Muhammad Ali',font=('Arial',20),foreground='red',background='Yellow')
lbl1.place(x=10,y=10)

lbl1 =Label(tab2,text='Muzammil Ali',font=('Arial',20),foreground='red',background='green')
lbl1.place(x=10,y=10)

btn = Button(text='Submit',
       font=('Arial',20),
       foreground='black',
       background='Yellow',
       command=myfun
             )
btn.place(x=100,y=300)


win.mainloop()